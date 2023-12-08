
# coding=utf-8
#!/bin/python

import os
import sys
import time
import psutil
import imp

def rom(info):
    OS = info['OS']
    i=0
    retlist1=[]
    rom=0
    romname = ""
    disks=1
    if OS == "Linux":
        romsh = os.popen("LANG=en_US df -h")
        list = romsh.read().split("\n")
        ilen = len(list)
        while i < ilen:
            if list[i] == "":
                i += 1
            elif list[i].split(" ")[0] == "Filesystem":
                i += 1
            elif list[i].split(" ")[0] == "udev":
                i += 1
            elif list[i].split(" ")[0] == "tmpfs":
                i += 1
            elif list[i].split(" ")[0] == "devtmpfs":
                i += 1
            elif list[i].split(" ")[0] == "overlay":
                i += 1
            elif list[i].split(" ")[0][:-1] == "/dev/zram":
                i += 1
            elif list[i].split(" ")[0][:-1] == "/dev/loop":
                i += 1
            else:

                diskinfo = int(list[i].split("%")[0].split(" ")[-1])

                if rom < diskinfo:
                    rom = diskinfo
                    romname = list[i].split(" ")[0]
                i=i+1
                disks += 1
    else:
        list = psutil.disk_partitions()
        ilen = len(list)
        while i < ilen:
            if list[i].mountpoint == "/boot":
                i += 1
            else:
                try:
                    diskinfo = psutil.disk_usage(list[i].mountpoint)
                    if rom < diskinfo.percent:
                        rom = diskinfo.percent
                        romname = list[i].mountpoint
                except Exception as e:
                    if(len(e.args) == 2):
                        if e.args[1] != '设备未就绪。':
                            print(e.args)   
                    else:
                        print(e.args)   
                i=i+1
                disks += 1
    return str(rom),romname

def todax(data):
    rams = ''
    if data < 1024:
        rams = str(data)
        rams = rams.split('.')
        rams = rams[0] + '.' + rams[1][:2] + "B" 
    elif data < (1024 * 1024):
        rams = str(data / 1024)
        rams = rams.split('.')
        rams = rams[0] + '.' + rams[1][:2] + "KB"
    elif data < (1024 * 1024 * 1024):
        rams = str(data / 1024 / 1024)
        rams = rams.split('.')
        rams = rams[0] + '.' + rams[1][:2] + "MB"
    else:
        rams = str(data / 1024 / 1024 / 1024)
        rams = rams.split('.')
        rams = rams[0] + '.' + rams[1][:2] + "GB"
    return rams

def catdisk(OS):
    res = b''
    diskfo = psutil.disk_partitions() 
    fo = len(diskfo)
    ii = 0
    for i in range(fo):
        if diskfo[i].device[:len("/dev/loop")] != "/dev/loop":
            ii += 1
    fo = ii
    res = res + (('"diskfo":"' + str(fo) + '","disk":[\r\n').encode("utf-8"))
    for i in range(fo):
        device = diskfo[i].mountpoint
        if diskfo[i].device[:len("/dev/loop")] != "/dev/loop":
            if diskfo[i].fstype == '':
                rams = "0B"
                ramall = "0B"
                diskinfo = ''
                if OS == "Windows":
                    name = diskfo[i].device[:-2]
                    diskinfo = " " + diskfo[i].fstype + ' ' + rams + ' / ' + ramall
                else:
                    name = diskfo[i].device
                if i == (fo - 1):
                    res = res + (('{"name":"' + name + '","minidiskinfo":"' + rams + ' / ' + ramall + '","diskinfo":"' + diskinfo + '","disk":"' + str(100)[:-2] + '"}\r\n').encode("utf-8"))
                else:
                    res = res + (('{"name":"' + name + '","minidiskinfo":"' + rams + ' / ' + ramall + '","diskinfo":"' + diskinfo + '","disk":"' + str(100)[:-2] + '"},\r\n').encode("utf-8"))
            else:
                ram = psutil.disk_usage(device)
                ramall = todax(ram.total)
                rams = todax(ram.used)
                #if len(ramstmp) == 2:
                #    rams = ramstmp[0] + '.' + ramstmp[1][:2] + ramstmp[1][-2:]
                #cpu = psutil.cpu_percent(i + 1)
                diskinfo = " " + diskfo[i].fstype + ' ' + rams + ' / ' + ramall
                lenmax = len(diskinfo) + len(device)
                if OS == "Windows":
                    device = device[:-1]
        #        if lenmax > 35:
        #            lenmax = len(device) - len(diskinfo) - 3 - 10
        #            diskinfo = device[:10] + '...' + device[lenmax:] + diskinfo
        #        else:    
                diskinfo = device + diskinfo 
                if OS == "Windows":
                    name = diskfo[i].device[:-2]
                    diskinfo = " " + diskfo[i].fstype + ' ' + rams + ' / ' + ramall
                else:
                    name = diskfo[i].device
                if i == (fo - 1):
                    res = res + (('{"name":"' + name + '","minidiskinfo":"' + rams + ' / ' + ramall + '","diskinfo":"' + diskinfo + '","disk":"' + str(ram.percent)[:-2] + '"}\r\n').encode("utf-8"))
                else:
                    res = res + (('{"name":"' + name + '","minidiskinfo":"' + rams + ' / ' + ramall + '","diskinfo":"' + diskinfo + '","disk":"' + str(ram.percent)[:-2] + '"},\r\n').encode("utf-8"))
    fo = os.popen('ls /sys/kernel/debug/mmc*/mmc*/ext_csd 2>/dev/null').read()
    #fo = os.popen('ls .tmp/mmc*/mmc*/ext_csd 2>/dev/null').read().split('\n')
    res = res + (('],\r\n').encode("utf-8"))
    if fo == '':
        res = res + (('"disksmfo":"' + str(0) + '","disksm":[\r\n{}').encode("utf-8"))
    else:
        fo = fo.split('\n')
        res = res + (('"disksmfo":"' + str(len(fo) - 1) + '","disksm":[\r\n').encode("utf-8"))
        for i in range(len(fo) - 1):
            data = os.popen('cat ' + fo[i]).read()
            name = os.popen('cat /sys/class/mmc_host/' + fo[i].split('/')[-2].split(':')[0] + '/' + fo[i].split('/')[-2] + '/name').read().split('\n')[0]
            #print('cat ' + fo[i])
            #print('cat /sys/class/mmc_host/' + fo[i].split('/')[-2].split(':')[0] + '/' + fo[i].split('/')[-2] + '/name')
            sm = '0'
            if data[536:538] == '00':
                sm = '不支持'
            elif data[536:538] == '01':
                sm = '10'
            elif data[536:538] == '02':
                sm = '20'
            elif data[536:538] == '03':
                sm = '30'
            elif data[536:538] == '04':
                sm = '40'
            elif data[536:538] == '05':
                sm = '50'
            elif data[536:538] == '06':
                sm = '60'
            elif data[536:538] == '07':
                sm = '70'
            elif data[536:538] == '08':
                sm = '80'
            elif data[536:538] == '09':
                sm = '90'
            elif data[536:538] == '0a':
                sm = '100'
            elif data[536:538] == '0b':
                sm = '耗尽'
            else:
                sm = data[536:538]
            diskinfo = '/dev/mmcblk' + fo[i].split('/')[-2].split(':')[0][-1] + ' name: ' + name + ' 寿命:' + sm + '%'
            if i == (len(fo) - 2):
                res = res + (('{"name":"' + name + '","minidiskinfo":"' + '","diskinfo":"' + diskinfo + '","disk":"' + sm + '"}\r\n').encode("utf-8"))
            else:
                res = res + (('{"name":"' + name + '","minidiskinfo":"' + '","diskinfo":"' + diskinfo + '","disk":"' + sm + '"},\r\n').encode("utf-8"))
#'/sys/class/mmc_host/mmc2/mmc2\:0001/name'

    return res

def catother(OS):
    other = ''

def catcpu(OS):
    res = b''
    fo = psutil.cpu_count()
    if OS == "Windows":
        shell = os.popen(bin + "wmic cpu get Name")
        bash = shell.read().split('\n')
        cpuname = bash[2]#.split(')')[-1][1:]

    else:
        shell = os.popen("cat /proc/cpuinfo | grep 'Hardware'")
        bash = shell.read().split('\n')
        
        if len(bash) == 1:
            shell = os.popen("cat /proc/cpuinfo | grep 'model name'")
            bash = shell.read().split('\n')
            if len(bash) == 1:
                shell = os.popen("lscpu | grep 'Model name'")
                bash = shell.read().split('\n')
                cpuname = bash[0].split(':')[1][1:]
                shell = os.popen("lscpu | grep 'CPU max MHz'")
                bash = shell.read().split('\n')
                cpuname = cpuname + ' @ ' + bash[0].split(':')[1][1:] + 'M'
            else:
                cpuname = bash[0].split(':')[1][1:]
        else:
            cpuname = bash[0].split(':')[1][1:]
    cputemp = '--'
    if os.path.exists("/sys/devices/virtual/thermal/thermal_zone0/temp") == True:
        shell = os.popen("cat /sys/devices/virtual/thermal/thermal_zone0/temp")
        bash = shell.read().split('\n')
        if len(bash) == 2:
            cputemp = bash[0][:-3]
    elif os.path.exists("/sys/class/hwmon/hwmon0/temp1_input") == True:
        shell = os.popen("cat /sys/class/hwmon/hwmon0/temp1_input")
        bash = shell.read().split('\n')
        if len(bash) == 2:
            cputemp = bash[0][:-3]
    res = res + (('"cputemp":"' + cputemp + '","cpufo":"' + str(fo) + '","cpu":[\r\n').encode("utf-8"))
    #if len(cpuname) > 20:
    #    cpunam = cpuname.split('CPU')
    #    cpuname = cpunam[-1][1:]
    freq = psutil.cpu_freq(percpu=True)
    cpu = psutil.cpu_percent(percpu=True)
    if len(freq) != len(cpu):
        if len(freq) == 1:
            i = 0
            fff=''
            for i in range(fo):
                fff += str(freq[0].current) + '\t'
            freq = fff.split('\t')
    else:
        for i in range(fo):
            freq[i] = str(freq[i].current)
    for i in range(fo):
        #cpu = psutil.cpu_percent(i + 1)
        if i == (fo - 1):
            res = res + (('{"name":"CPU ' + str(i) + '","cpuname":"' + cpuname + '","freq":"' + freq[i] + '","cpu":"' + str(cpu[i])[:-2] + '"}\r\n').encode("utf-8"))
        else:
            res = res + (('{"name":"CPU ' + str(i) + '","cpuname":"' + cpuname + '","freq":"' + freq[i] + '","cpu":"' + str(cpu[i])[:-2] +  '"},\r\n').encode("utf-8"))
    return res

def catram():
    res = b''
    res = res + (('"ramfo":"' + str(2) + '","ram":[\r\n').encode("utf-8"))
    ram = psutil.virtual_memory()
    if ram.total < 1024:
        ramall = str(ram.total)[:4] + "B" 
    elif ram.total < (1024 * 1024):
        ramall = str(ram.total / 1024)[:4] + "KB"
    elif ram.total < (1024 * 1024 * 1024):
        ramall = str(ram.total / 1024 / 1024)[:4] + "MB"
    elif ram.total < (1024 * 1024 * 1024 * 1024):
        ramall = str(ram.total / 1024 / 1024 / 1024)[:4] + "GB"
    #ramalltmp = ramall.split('.')
    #if len(ramalltmp) == 2:
    #    ramall = ramalltmp[0] + '.' + ramalltmp[1][:2] + ramalltmp[1][-2:]
    if ram.used < 1024:
        rams = str(ram.used)[:4] + "B" 
    elif ram.used < (1024 * 1024):
        rams = str(ram.used / 1024)[:4] + "KB"
    elif ram.used < (1024 * 1024 * 1024):
        rams = str(ram.used / 1024 / 1024)[:4] + "MB"
    elif ram.used < (1024 * 1024 * 1024 * 1024):
        rams = str(ram.used / 1024 / 1024 / 1024)[:4] + "GB"
    #ramstmp = rams.split('.')
    #if len(ramstmp) == 2:
    #    rams = ramstmp[0] + '.' + ramstmp[1][:2] + ramstmp[1][-2:]
    res = res + (('{"name":"内存","raminfo":"' + rams + ' / ' + ramall + '","ram":"' + str(ram.percent) + '"},\r\n').encode("utf-8"))

    ram = psutil.swap_memory()
    if ram.total < 1024:
        ramall = str(ram.total)[:4] + "B" 
    elif ram.total < (1024 * 1024):
        ramall = str(ram.total / 1024)[:4] + "KB"
    elif ram.total < (1024 * 1024 * 1024):
        ramall = str(ram.total / 1024 / 1024)[:4] + "MB"
    elif ram.total < (1024 * 1024 * 1024 * 1024):
        ramall = str(ram.total / 1024 / 1024 / 1024)[:4] + "GB"
    #ramalltmp = ramall.split('.')
    #if len(ramalltmp) == 2:
    #    ramall = ramalltmp[0] + '.' + ramalltmp[1][:2] + ramalltmp[1][-2:]
    if ram.used < 1024:
        rams = str(ram.used)[:4] + "B" 
    elif ram.used < (1024 * 1024):
        rams = str(ram.used / 1024)[:4] + "KB"
    elif ram.used < (1024 * 1024 * 1024):
        rams = str(ram.used / 1024 / 1024)[:4] + "MB"
    elif ram.used < (1024 * 1024 * 1024 * 1024):
        rams = str(ram.used / 1024 / 1024 / 1024)[:4] + "GB"
    ramstmp = rams.split('.')
    #if len(ramstmp) == 2:
    #    rams = ramstmp[0] + '.' + ramstmp[1][:2] + ramstmp[1][-2:]
    res = res + (('{"name":"交换空间","raminfo":"' + rams + ' / ' + ramall + '","ram":"' + str(ram.percent) + '"}\r\n').encode("utf-8"))
    return res

def main(new_client_socket,post,Headers,info,user):

    OS = info['OS']
    bin = ''
    cpuname = ''
    cpufo = 0

    res = b'{\r\n'
    res = res + (('"cpumain": "'+str(psutil.cpu_percent(None))+'",\r\n').encode("utf-8"))
    rr,rrr = rom(info)
    res = res + (('"rommain": "'+rr+'",\r\n').encode("utf-8"))
    res = res + (('"romnamemain": "'+rrr+'",\r\n').encode("utf-8"))
    bat = '0'
    if os.path.exists("/sys/class/power_supply"):
        dirn = os.listdir("/sys/class/power_supply/") 
        for d in dirn:
            if os.path.exists("/sys/class/power_supply/" + d + "/type"):
                if os.path.exists("/sys/class/power_supply/" + d + "/capacity"):
                    cat = os.popen("cat /sys/class/power_supply/" + d + "/type").read().split('\n')[0]
                    bat = os.popen("cat /sys/class/power_supply/" + d + "/capacity").read().split('\n')[0]
    res = res + (('"bat": "'+bat+'",\r\n').encode("utf-8"))
            #    break

    res = res + catcpu(OS)

    res = res + (('],\r\n').encode("utf-8"))
    res = res + catram()
    
    res = res + (('],\r\n').encode("utf-8"))
    res = res + catdisk(OS)
    
    res = res + ((']}').encode("utf-8"))
    res = res + (('').encode("utf-8"))

    
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res,"application/json",Headers,info)

