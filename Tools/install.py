# coding=utf-8
#!/bin/python

import os
import sys
import imp
import platform
import shutil
import binascii
import hashlib
import locale

install_diri = b"C:\jcm"
install_porti = 8888
install_booti = b"yes"
pwd = os.getcwd()

text = {}
text["name"] = "# JCM (jiang Cluster Management) Installer#"
text["insdir"] = "install dir: "
text["port"] = "port: "
text["boot"] = "boot: "
text["qr"] = "Confirm the information, enter the exit exit installation"
text["oserr"] = "Get OS name error"
text["init"] = "init"
text["osname"] = "OS Name:"
text["devname"] = "Host Name:"

try:
    language = locale.getdefaultlocale()
    language = language[0]
    #language = "zh_CN"
    run = imp.load_source('run',"language/Tools/install.py/" + language + ".py")
    for textname in text.keys():
        try:
            textval = run.text[textname]
            text[textname] = textval
        except Exception as e:
            print(e.args)
except Exception as e:
    print(e.args)

def pr(new_client_socket,data):
    print(data.decode("utf-8"),end='')

OS_ = platform.system()
if OS_ == 'Windows':
#    os.system("echo %PATH%")
#    os.system("ls")
#    os.system("pwd")
    install_diri = b"C:\jcm"
else:
    install_diri = b"/usr/jcm"

print(text["name"])
install_dir = input(text["insdir"] + "[" + install_diri.decode("utf-8") + "] ").encode("utf-8")
if install_dir == b'':
    install_dir = install_diri
install_port = input(text["port"] + "[" + str(install_porti) + "] ")
if install_port == '':
    install_port = install_porti
else:
    install_port = int(install_port)
install_boot = input(text["boot"] + "[" + install_booti.decode("utf-8") + "] ").encode("utf-8")
if install_boot == b'y' or install_boot == b'yes' or install_boot == b'':
    install_boot = install_booti
print("#############################")
print(text["insdir"] + "" + install_dir.decode("utf-8"))
print(text["port"] + "" + str(install_port))
print(text["boot"] + "" + install_boot.decode("utf-8"))
print("#############################")

if OS_ == 'Windows':
    os.environ['PATH'] = os.environ['PATH'] + ';' + install_dir.decode("utf-8") + "\\Tools\\.bash\\bin"
install_ = input(text["qr"]).encode("utf-8")
if install_ != b'exit':
    OS_ = platform.system()
    OS = ''
    if OS_ == 'Windows':
        sh = os.popen("systeminfo")
        shell = sh.read().split('\n')
        for sh in range(len(shell)):
            #print('[' + str(sh) + '] ' + shell[sh])
            sh = shell[sh].split('  ')
            if sh[0] == text["osname"]:
                OS = sh[-1]
            if sh[0] == text["devname"]:
                dev_name = sh[-1]
        if OS == '':
            print(text["oserr"])
            OS = 'Windows'
    else:
        if os.path.exists('/etc/os-release'):
            sh = os.popen("cat /etc/os-release | grep PRETTY_NAME")
            shell = sh.read().split('"')
            OS = shell[1]
        else:
            sh = os.popen("uname -n")
            shell = sh.read()
            OS = shell[:-1]
        sh = os.popen('cat /etc/hostname')
        dev_name = sh.read().split('\n')[0]
    if os.path.exists(install_dir.decode("utf-8") + "") == False:
        os.mkdir(install_dir.decode("utf-8") + "")
    if os.path.exists(install_dir.decode("utf-8") + "/server") == False:
        os.mkdir(install_dir.decode("utf-8") + "/server")
    if os.path.exists(install_dir.decode("utf-8") + "/Tools") == False:
        os.mkdir(install_dir.decode("utf-8") + "/Tools")
    if os.path.exists(install_dir.decode("utf-8") + "/web") == False:
        os.mkdir(install_dir.decode("utf-8") + "/web")
    if OS_ == 'Windows':
        print("install 7-zip")
        if os.path.exists(install_dir.decode("utf-8") + "/Tools/7z") == False:
            os.mkdir(install_dir.decode("utf-8") + "/Tools/7z")
            shutil.copyfile("lib/7z/7z.dll",install_dir.decode("utf-8") + "/Tools/7z/7z.dll")
            shutil.copyfile("lib/7z/7z.exe",install_dir.decode("utf-8") + "/Tools/7z/7z.exe")
    else:
        #print("echo install 7-zip")
        OSs = OS.split(' ')
        #if OSs[0] == 'Ubuntu':
        #    os.system('sudo apt update')
    os.chdir(install_dir.decode("utf-8"))
    if OS_ == 'Windows':
        osss = OS.split('Windows 1')
        if len(osss) == 2:
            print("install python3")
            if os.path.exists(install_dir.decode("utf-8") + "/Tools/.python") == False:
                #os.remove(install_dir.decode("utf-8") + "/Tools/.python")
                os.system(install_dir.decode("utf-8") + "/Tools/7z/7z.exe x " + pwd + "\\lib\\python-3.10.5.7z -r -o" + install_dir.decode("utf-8") + "\\ -aoa >>log.log")
        else:
            if os.path.exists(install_dir.decode("utf-8") + "\\Tools\\NET") == False:
                print("install NET")
                os.mkdir(install_dir.decode("utf-8") + "\\Tools\\NET")
                os.system(pwd + '\\lib\\NET.exe /norestart /showfinalerror /passive')
            print("install python3")
            if os.path.exists(install_dir.decode("utf-8") + "\\Tools\\.python") == False:
                os.mkdir(install_dir.decode("utf-8") + "\\Tools\\.python")
            os.system(pwd + "\\lib\\python-3.6.7 /passive  TargetDir=" + install_dir.decode("utf-8") + "\\Tools\\.python InstallAllUsers=1 PrependPath=0")
        print("install bash")
        if os.path.exists(install_dir.decode("utf-8") + "/Tools/.bash") == False:
            #os.remove(install_dir.decode("utf-8") + "/Tools/.bash")
            os.system(install_dir.decode("utf-8") + "/Tools/7z/7z.exe x " + pwd + "\\lib\\bash.zip -r -o" + install_dir.decode("utf-8") + "\\Tools -aoa >>log.log")
        #sh = pwd + "\\Tools\\install.bat pat " + install_dir.decode("utf-8") + "\\Tools\\.bash\\bin  >>log.log"
        
        #print(sh)
        #os.system(sh)
        os.chdir(install_dir.decode("utf-8"))
        if os.path.exists(install_dir.decode("utf-8") + "/lib") == False:
            os.mkdir(install_dir.decode("utf-8") + "/lib")
        os.system(pwd + "/lib/CopyX /Y \"" + pwd + "\\lib\" \"" + install_dir.decode("utf-8") + "\"")
        if os.path.exists(install_dir.decode("utf-8") + "/.out") == False:
            os.mkdir(install_dir.decode("utf-8") + "/.out")
        print("install main")
        sh = "tar xzf lib/pkg/main_V0.2.pkg " + "-C .out/main_V0.2.pkg/.out"
        #print(sh)
        #os.system("pwd")
        '''os.system(sh)
        sh = install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/.out/server/main/Package.py "
        sh = imp.load_source(sh,sh)
        sh.install("","","","","",pr)
        print("install APP")
        sh = "tar xzf lib/pkg/APP_V0.2.pkg " + "-C .out/APP_V0.2.pkg/.out"
        os.system(sh)
        sh = install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out/server/APP/Package.py "
        sh = imp.load_source(sh,sh)
        sh.install("","","","","",pr)
        '''
        fs = open(install_dir.decode("utf-8") + "\\run.bat","wb")
        fs.write(b"@cd " + install_dir + b"\n")
        fs.write(b"@Tools\\.python\\python server\\init.py")
        fs.close()
        fs = open(install_dir.decode("utf-8") + "\\boot.bat","wb")
        fs.write(b"@echo BOOT JCM\n")
        fs.write(b"@timeout /nobreak /t 20\n")
        fs.write(b"@if \"%1\" == \"v\" goto begin\n")
        fs.write(b'@mshta vbscript:createobject("wscript.shell").run("""%~0"" v",0)(window.close)&&exit\n')
        fs.write(b":begin\n")
        fs.write(b"@cd " + install_dir + b"\n")
        fs.write(b"@run")
        fs.close()
        if install_boot == b'yes':
            os.system(pwd + "/lib/CopyX /Y \"" + install_dir.decode("utf-8") + "\\boot.bat\" \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\"")
        
    else:
        #print("install python3")
        #OSs = OS.split(' ')
        #if OSs[0] == 'Ubuntu':
        #    os.system('sudo apt install -y python3')
        #os.system('mkdir -p ' + install_dir.decode("utf-8") + '/lib')
        #os.system('cp -rf ' + pwd + '/lib/pkg ' + install_dir.decode("utf-8") + '/lib/pkg')

        os.chdir(install_dir.decode("utf-8"))
        if os.path.exists(install_dir.decode("utf-8") + "/lib") == False:
            os.mkdir(install_dir.decode("utf-8") + "/lib")
        if os.path.exists(install_dir.decode("utf-8") + "/lib/pkg") == False:
            os.mkdir(install_dir.decode("utf-8") + "/lib/pkg")
        os.system("cp -rf \"" + pwd + "/lib/pkg\" \"" + install_dir.decode("utf-8") + "/lib\"")
        if os.path.exists(install_dir.decode("utf-8") + "/.out") == False:
            os.mkdir(install_dir.decode("utf-8") + "/.out")
        print("install main")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/main_V0.2.pkg")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/.out")
        sh = "tar xzf lib/pkg/main_V0.2.pkg " + "-C .out/main_V0.2.pkg/"

        #print(sh)
        #os.system("pwd")
        os.system(sh)
        sh = install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/.out/server/main/Package.py"
        sh = imp.load_source(sh,sh)
        sh.install("","","","","",pr)
        print("install APP")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out")
        sh = "tar xzf lib/pkg/APP_V0.2.pkg " + "-C .out/APP_V0.2.pkg/"
        os.system(sh)
        sh = install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out/server/APP/Package.py"
        sh = imp.load_source(sh,sh)
        sh.install("","","","","",pr)

        fs = open(install_dir.decode("utf-8") + "/run.sh","wb")
        fs.write(b"#!/bin/sh\n")
        fs.write(b"cd " + install_dir + b"\n")
        fs.write(b"python3 server/jcm.py")
        fs.close()
        os.system('chmod 777 ' + install_dir.decode("utf-8") + "/run.sh")
        if os.path.exists("/bin/systemctl"):
            fs = open(install_dir.decode("utf-8") + "/jcm.service","wb")
            fs.write(b"# It's not recommended to modify this file in-place, because it will be\n")
            fs.write(b"# overwritten during package upgrades.\n")
            fs.write(b"\n")
            fs.write(b"[Unit]\n")
            fs.write(b"Description=jcm server\n")
            fs.write(b"After=network.target\n")
            fs.write(b"\n")
            fs.write(b"[Service]\n")
            fs.write(b"Type=simple\n")
            fs.write(b"ExecStart=sh " + install_dir + b"/run.sh\n")
            fs.write(b"\n")
            fs.write(b"[Install]\n")
            fs.write(b"WantedBy=multi-user.target\n")
            fs.close()
        elif os.path.exists("/etc/rc.d"):
            os.system("cp run.sh /etc/rc.d/S99jcm")
       

        os.system('chmod 777 ' + install_dir.decode("utf-8") + "/jcm.service")
        os.system("cp  \"" + install_dir.decode("utf-8") + "/jcm.service\" \"/usr/lib/systemd/system/\"")
        if install_boot == b'yes':
            os.system("systemctl enable jcm.service")
            #os.system("systemctl status jcm.service")
        else:
            os.system("systemctl disable jcm.service")
            #os.system("systemctl status jcm.service")
        
    if OS_ == 'Windows':
        os.system("run.bat")
    else:
        os.system("sh run.sh")
