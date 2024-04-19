# coding=utf-8
#!/bin/python
import os
import sys
import imp
import time
import socket
import psutil
import threading 
from configparser import ConfigParser

def catinfo(conf,section,option):
    if conf.has_section(section):
        if conf.has_option(section, option):
            return conf[section][option]
    return ''
            
def setinfo(conf,section,option,value):
    if conf.has_section(section) == False:
        conf.add_section(section)
    conf.set(section, option, value)

def catio():
    global qemu_jcm_io
    io = os.popen("top -n 2 | grep 'wa,' | awk '{print $10}'").read()
    qemu_jcm_io = io.split("\n")

def main(data):
    global qemu_jcm_io
    new_client_socket = data["new_client_socket"]
    RUL_CS            = data["RUL_CS"]
    post_data         = data["post_data"]
    Headers           = data["Headers"]
    info              = data["info"]
    user              = data["user"]

    type = ""
    res = ""
    post = RUL_CS
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'type':
            type = tmp[1]
    res = '{"data":"ERROR"}'

    if type == "run":
        res = '{'
        re = ""
        p1 = threading.Thread(target=catio,args=())
        p1.start()
        #io = os.popen("top -n 2 | grep 'wa,' | awk '{print $10}'").read()
        fo = 0
        list = os.listdir(".config/qemu/config/")
        for i in list:
            fo = fo + 1
            conf = ConfigParser()
            conf.read(".config/qemu/config/" + i + "")
            dir = catinfo(conf,"qemu","qemu_dir")
            name = dir.split("/")[-1]
            if not os.path.exists(dir + "/qemu.ini"):
                re += '{"name":"' + name + '","api":"0","cpu":"0","ram":"0","soket":"qemu_' + name + '"},'
            else:
                if not os.path.exists("/run/jcm/qemu/pid/" + name + ".pid"):
                    re += '{"name":"' + name + '","api":"1","cpu":"0","ram":"0","soket":"qemu_' + name + '"},'
                else:
                    pid = open("/run/jcm/qemu/pid/" + name + ".pid","r").read()
                    p = psutil.Process(int(pid))
                    cpu = p.cpu_percent()
                    time.sleep(0.1)
                    cpu = p.cpu_percent()
                    cpu = str(cpu)[:5]
                    ram = p.memory_info()
                    ram = ram.rss / 1024 / 1024
                    rams = 0
                    conf.read(dir + "/qemu.ini")
                    value = catinfo(conf,"qemu","qemu_ram")
                    if value[-1] == 'g' or value[-1] == 'G':
                        rams += int(value[:-1])
                    elif value[-1] == 'm' or value[-1] == 'M':
                        rams += int(value[:-1])
                    else:
                        rams += int(value)
                    #ram = str(ram)[:5]
                    ram = '{:.2%}'.format(ram/rams)[:-1]
                    re += '{"name":"' + name + '","api":"2","cpu":"' + cpu + '","ram":"' + ram + '","soket":"qemu_' + name + '"},'
        res += '"fo":"' + str(fo) + '",'
        res += '"data":[' + re[:-1] + '],'
        #p1.join()
        io = qemu_jcm_io
        cpu = str(psutil.cpu_percent(None))
        ram = str(psutil.virtual_memory().percent)
        if int(io[0].split(".")[0]) < int(io[1].split(".")[0]):
            io[0] = io[1]
        res += '"cpu":"' + str(cpu) + '",'
        res += '"ram":"' + str(ram) + '",'
        res += '"io":"' + str(io[0]) + '"'
        #for i in io:
        res += '}'
    elif type == "stop":
        name = ""
        post = RUL_CS
        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'name':
                name = tmp[1]
        if os.path.exists("/run/jcm/qemu/qmp/" + name + ".qmp"): 
            qmp = socket.socket(family=socket.AF_UNIX,type=socket.SOCK_STREAM)
            qmp.connect("/run/jcm/qemu/qmp/" + name + ".qmp")
            time.sleep(0.5)
            data = qmp.recv(102400)
            qmp.send(b'{"execute":"qmp_capabilities"}')
            time.sleep(0.5)
            data = qmp.recv(102400)
            qmp.send(b'{ "execute": "system_powerdown" }')
            data = qmp.recv(102400)
            qmp.close()
            res = '{"data":"正在关机"}'
    elif type == "kill":
        name = ""
        post = RUL_CS
        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'name':
                name = tmp[1]
        if os.path.exists("/run/jcm/qemu/pid/" + name + ".pid"): 
            pid = open("/run/jcm/qemu/pid/" + name + ".pid","r").read()
            data = os.popen("kill " + pid).read()
            if data == "":
                data = "成功"
            res = '{"data":"' + data + '"}'
    elif type == "addpost":
        data = {}
        qemu_name = ""
        qemu_smp  = "" 
        qemu_ram  = ""
        qemu_disk  = ""
        try:
            for i in post:
                tmp = i.split('=')
                data[tmp[0]] = tmp[1]
                if tmp[0] == 'qemu_name':
                    qemu_name = tmp[1]
                if tmp[0] == 'qemu_smp':
                    qemu_smp = tmp[1]
                if tmp[0] == 'qemu_ram':
                    qemu_ram = tmp[1]
                if tmp[0] == 'qemu_disk':
                    qemu_disk = tmp[1]
            if os.path.exists(".config/qemu") == False:
                os.mkdir(".config/qemu")
            if os.path.exists(".config/qemu/config") == False:
                os.mkdir(".config/qemu/config")
            if os.path.exists(".config/qemu/config/" + qemu_name + ".ini"):
                res = '{"data":"存在此名称的虚拟机"}'
            else:
                res = ""
                try:
                    if qemu_ram[-1] == "m" or qemu_ram[-1] == "M" or qemu_ram[-1] == "G" or qemu_ram[-1] == "g":
                        ram = int(qemu_ram[:-1])
                    else:
                        ram = int(qemu_ram)
                except Exception as e:
                    res = '{"data":"' + "RAM is ERROR" + '"}'
                try:
                    smp = int(qemu_smp)
                except Exception as e:
                    res = '{"data":"' + "SMP is ERROR" + '"}'

                try:
                    if qemu_disk == "":
                        disk = 0
                    elif qemu_disk[-1] == "m" or qemu_disk[-1] == "M" or qemu_disk[-1] == "G" or qemu_disk[-1] == "g":
                        disk = int(qemu_disk[:-1])
                    else:
                        disk = int(qemu_disk)
                except Exception as e:
                    res = '{"data":"' + "DISK is ERROR" + '"}'

                if res == "":
                    conf = ConfigParser()
                    conf.read(".config/qemu/config/" + qemu_name + ".ini")
                    setinfo(conf,"qemu","qemu_dir",data["qemu_dir"])
                    dir = ""
                    for i in data["qemu_dir"].split("/")[1:]:
                        dir = dir + "/" + i
                        if not os.path.exists(dir):
                            os.mkdir(dir)
                    with open(".config/qemu/config/" + qemu_name + ".ini", 'w', encoding='utf-8') as file:
                        conf.write(file)  # 值写入配置文件
                    if not os.path.exists(dir + "/qemu.ini"):
                        conf = ConfigParser()
                        conf.read(dir + "/qemu.ini")
                        setinfo(conf,"qemu","qemu_name",data["qemu_name"])
                        setinfo(conf,"qemu","qemu_dir",data["qemu_dir"])
                        setinfo(conf,"qemu","qemu_smp",data["qemu_smp"])
                        setinfo(conf,"qemu","qemu_ram",data["qemu_ram"])
                        if disk != 0:
                            setinfo(conf,"qemu_sata_0","qemu_disk",data["qemu_disk"])
                            setinfo(conf,"qemu_sata_0","qemu_boot","")
                            os.system("qemu-img create -fqcow2 " + data["qemu_dir"] + "/" + data["qemu_name"] + ".qcow2 " + data["qemu_disk"])
                        with open(dir + "/qemu.ini", 'w', encoding='utf-8') as file:
                            conf.write(file)  # 值写入配置文件

                        res = '{"data":"' + "成功" + '"}'
                    else:
                        res = '{"data":"' + "存在虚拟机,注册" + '"}'


        except Exception as e:
            res = '{"data":"' + e.args[0] + '"}'
    elif type == "start":
        dir = ""
        name = ""
        post = RUL_CS
        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'name':
                name = tmp[1]
        conf = ConfigParser()
        conf.read(".config/qemu/config/" + name + ".ini")
        dir = catinfo(conf,"qemu","qemu_dir")
        if not os.path.exists(dir + "/qemu.ini"):
            res = '{"data":"' + '没找到虚拟机文件' + '"}'
        else:
            if not os.path.exists("/run"):
                os.mkdir("/run")
            if not os.path.exists("/run/jcm"):
                os.mkdir("/run/jcm")
            if not os.path.exists("/run/jcm/qemu"):
                os.mkdir("/run/jcm/qemu")
            if not os.path.exists("/run/jcm/qemu/qmp"):
                os.mkdir("/run/jcm/qemu/qmp")
            if not os.path.exists("/run/jcm/qemu/vnc"):
                os.mkdir("/run/jcm/qemu/vnc")
            if not os.path.exists("/run/jcm/qemu/pid"):
                os.mkdir("/run/jcm/qemu/pid")
            conf.read(dir + "/qemu.ini")
            value = ""
            cmd = "qemu-system-x86_64 -enable-kvm -cpu host "
            value = catinfo(conf,"qemu","qemu_name")
            cmd += " -name " + value
            value = catinfo(conf,"qemu","qemu_smp")
            cmd += " -smp " + value
            value = catinfo(conf,"qemu","qemu_ram")
            if value[-1] == 'g' or value[-1] == 'G':
                value = value
            elif value[-1] == 'm' or value[-1] == 'M':
                value = value
            else:
                value += 'M'
            cmd += " -m " + value

            
            cmd += "\
 -device pci-bridge,id=pci.1,chassis_nr=1,bus=pci.0,addr=0x1e \
 -device pci-bridge,id=pci.2,chassis_nr=2,bus=pci.0,addr=0x1f \
 -device pci-bridge,id=pci.3,chassis_nr=3,bus=pci.0,addr=0x5 "

            value = catinfo(conf,"qemu","qemu_uefi")
            if value == 'True':
                uefidir = info["dir"]
                uefidir = uefidir + "/Tools/qemu/OVMF_CODE.fd"
                cmd += " -boot order=dc,menu=on,strict=on,reboot-timeout=1000"
                cmd += " -drive if=pflash,unit=0,format=raw,readonly=on,file=" + uefidir
            value = catinfo(conf,"qemu","qemu_usb")
            if value == '3.0':
                cmd += " -device qemu-xhci,p2=15,p3=15,id=xhci,bus=pci.1,addr=0x1b"
                
            sata = ""
            data = conf.sections()
            for d in data:
                if d != "qemu":
                    d = d.split('_')
                    if d[1] == "sata":
                        bootino = catinfo(conf,d[0] + "_" + d[1] + "_" + d[2],"qemu_boot")
                        if sata == "":
                            cmd += " -device ahci,id=ahci0,multifunction=on,bus=pci.0,addr=0x7"
                            sata = "0"
                        cmd += " -device ide-hd,bus=ahci0." + d[2] + ",drive=drive-sata" + d[2] + ",id=sata" + d[2] + ""
                        diskdir = catinfo(conf,d[0] + "_" + d[1] + "_" + d[2],"qemu_dir")
                        if diskdir == '':
                            diskdir = dir + '/' + name + '.qcow2'
                            disklist = "qcow2"
                            cmd += " -drive file=" + diskdir + ",if=none,format=" + disklist + ",id=drive-sata" + d[2] + ""
                        else:
                            diskdisk = catinfo(conf,d[0] + "_" + d[1] + "_" + d[2],"qemu_disk")
                            if diskdisk == "disk":
                                disklist = "raw"
                                cmd += " -drive file=" + diskdir + ",if=none,format=" + disklist + ",id=drive-sata" + d[2] + ""
                            else:
                                hz = diskdir.split(".")[-1]
                                if hz == "qcow2":
                                    disklist = "qcow2"
                                    if diskdir[0] != "/":
                                        diskdir = dir + '/' + diskdir
                                    cmd += " -drive file=" + diskdir + ",if=none,format=" + disklist + ",id=drive-sata" + d[2] + ""
                                elif hz == "img":
                                    disklist = "raw"
                                    if diskdir[0] != "/":
                                        diskdir = dir + '/' + diskdir
                                    cmd += " -drive file=" + diskdir + ",if=none,format=" + disklist + ",id=drive-sata" + d[2] + ""
                                else:
                                    if diskdir[0] != "/":
                                        diskdir = dir + '/' + diskdir
                                    cmd += " -drive file=" + diskdir + ",if=none,id=drive-sata" + d[2] + ""
                    elif d[1] == "usb":
                        vid = catinfo(conf,d[0] + "_" + d[1] + "_" + d[2],"vid")
                        pid = catinfo(conf,d[0] + "_" + d[1] + "_" + d[2],"pid")
                        cmd += " -device usb-host,bus=xhci.0,port=1,vendorid=" + vid + ",productid=" + pid + ",id=usb0"
                    elif d[1] == "virtionet":
                        br  = catinfo(conf,d[0] + "_" + d[1] + "_" + d[2],"br")
                        mac = catinfo(conf,d[0] + "_" + d[1] + "_" + d[2],"mac")
                        cmd += " -netdev bridge,br=" + br + ",id=br0"
                        cmd += " -device virtio-net-pci,mac=" + mac + ",netdev=br0,bus=pci.0,addr=0x12,id=net0,rx_queue_size=1024,tx_queue_size=256"

            cmd += " -chardev socket,id=qmp,path=/run/jcm/qemu/qmp/" + name + ".qmp,server=on,wait=off "
            cmd += " -mon chardev=qmp,mode=control "
            cmd += " -pidfile /run/jcm/qemu/pid/" + name + ".pid "
            cmd += " -vnc unix:/run/jcm/qemu/vnc/" + name + ".vnc"
            #cmd += " -device ide-cd,bus=ahci0.1,drive=drive-sata1,id=sata1"
            #cmd += " -drive file=/home/jiang/edit/hassos/dsm/ubuntu-20.04.6-live-server-amd64.iso,if=none,id=drive-sata1,media=cdrom "
            cmd += " -daemonize 2>&1"
#scp -r jiang/SynologyDrive jiang@n2840.lan:~/edit/jcm/04130822/
            sh = os.popen(cmd).read()[:-1]
            

            if sh == "":
                res = '{"data":"' + 'Start' + '","soket":"qemu_' + name + '"}'
            else:
                res = '{"data":"' + sh + '","soket":"qemu_' + name + '"}'

    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json;charset=UTF-8",Headers,info)


    