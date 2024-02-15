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

cmd = sys.executable
cmd = cmd + " -m pip install requests"
os.system(cmd)
import requests
import urllib3
urllib3.disable_warnings()

gitrul = "https://github.com/XiaoXianNv-boot/jcm/raw/master"
mirrorrul = "https://jiang144.i234.me/data/jcm"

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

if os.path.exists("tmp") == False:
    os.mkdir("tmp")
if os.path.exists("lib") == False:
    os.mkdir("lib")
if os.path.exists("lib/pkg") == False:
    os.mkdir("lib/pkg")
if os.path.exists("language") == False:
    os.mkdir("language")
if os.path.exists("language/Tools") == False:
    os.mkdir("language/Tools")
if os.path.exists("language/Tools/install.py") == False:
    os.mkdir("language/Tools/install.py")
def pr(new_client_socket,data):
    print(data.decode("utf-8"),end='')

def progress_bar( nb_traits,name,d):
	sys.stdout.write('\r' + name + d + ' : Downloading [')
	for i in range(0, nb_traits):
		if i == nb_traits - 1:
			sys.stdout.write('>')
		else:
			sys.stdout.write('=')
	for i in range(0, 49 - nb_traits):
		sys.stdout.write(' ')
	sys.stdout.write(']')
	sys.stdout.flush()
#https://github.com/XiaoXianNv-boot/jcm/raw/master/language/Tools/install.py/en_US.py
#https://github.com/XiaoXianNv-boot/jcm/raw/master/language/install.py/en_US.py
def down(rul,dir,d): #
    sys.stdout.write(dir.split('/')[-1] + d + ' : Downloading...')
    sys.stdout.flush()
    bresp = requests.get(rul, stream=True, verify=False)
    if (bresp.status_code != 200): # When the layer is located at a custom URL
        if(bresp.status_code == 404):
            print('\rERROR: Cannot download layer {} [HTTP {}]'.format(dir.split('/')[-1], bresp.status_code, ""))
            print(bresp.content)
            return
        bresp = requests.get(layer['urls'][0], headers=auth_head, stream=True, verify=False)
        if (bresp.status_code != 200):
            print('\rERROR: Cannot download layer {} [HTTP {}]'.format(dir.split('/')[-1], bresp.status_code, bresp.headers['Content-Length']))
            print(bresp.content)
            return
            #exit(1)
    # Stream download and follow the progress
    bresp.raise_for_status()
    unit = int(bresp.headers['Content-Length']) / 50
    acc = 0
    nb_traits = 0
    progress_bar( nb_traits,dir.split('/')[-1],d)
    with open("tmp/" + dir.split("/")[-1], "wb") as file:
        for chunk in bresp.iter_content(chunk_size=8192): 
            if chunk:
                file.write(chunk)
                acc = acc + 8192
                if acc > unit:
                    nb_traits = nb_traits + 1
                    progress_bar( nb_traits,dir.split('/')[-1],d)
                    acc = 0
    sys.stdout.write("\r{}".format(dir.split('/')[-1]) + d + " : Extracting...{}".format(" "*50)) # Ugly but works everywhere
    sys.stdout.flush()
    
    import time
    time.sleep(0.5)

    os.rename("tmp/" + dir.split("/")[-1],dir)

    print("\r{}".format(dir.split('/')[-1]) + d + " : Pull complete [{}]".format(bresp.headers['Content-Length']))

try:
    language = locale.getdefaultlocale()
    language = language[0]
    #language = "zh_CN"
    if os.path.exists("language/Tools/install.py/" + language + ".py") == False:#从git下载
        down(gitrul + "/language/Tools/install.py/" + language + ".py","language/Tools/install.py/" + language + ".py","\t\t\t")
    if os.path.exists("language/Tools/install.py/" + language + ".py") == False:#失败从mirror下载
        down(mirrorrul + "/install/language/install.py/" + language + ".py","language/Tools/install.py/" + language + ".py","\t\t\t")

    run = imp.load_source('run',"language/Tools/install.py/" + language + ".py")
    for textname in text.keys():
        try:
            textval = run.text[textname]
            text[textname] = textval
        except Exception as e:
            print(e.args)
except Exception as e:
    print(e.args)

OS_ = platform.system()
print(sys.executable)

def dl(rul,dir,d):
    if os.path.exists(dir) == False:
        down(gitrul + rul,dir,d)
    if os.path.exists(dir) == False:
        down(mirrorrul + rul,dir,d)

if OS_ == 'Windows':
    rul = ''
    if os.path.exists("jcm_install") == False:
        os.mkdir("jcm_install")
    if sys.executable.split('\\')[-1] == "install.exe":
        os.chdir("jcm_install")
        print("Init ...")
        pwd = os.getcwd()
    if os.path.exists("lib/pkg") == False:
        os.mkdir("lib/pkg")
    if os.path.exists("lib/7z") == False:
        os.mkdir("lib/7z")
    if os.path.exists("lib/7z/7z.dll") == False:
        dl(rul + "/lib/7z/7z.dll","lib/7z/7z.dll","\t\t\t")
    if os.path.exists("lib/7z/7z.exe") == False:
        dl(rul + "/lib/7z/7z.exe","lib/7z/7z.exe","\t\t\t")
    if os.path.exists("lib/bash.zip") == False:
        dl(rul + "/lib/bash.zip","lib/bash.zip","\t\t")
    if os.path.exists("lib/CopyX.exe") == False:
        dl(rul + "/lib/CopyX.exe","lib/CopyX.exe","\t\t")
    if os.path.exists("lib/NET.exe") == False:
        dl(rul + "/lib/NET.exe","lib/NET.exe","\t\t\t")
    if os.path.exists("lib/python-3.6.7.exe") == False:
        dl(rul + "/lib/python-3.6.7.exe","lib/python-3.6.7.exe","\t")
    if os.path.exists("lib/python-3.8.2.exe") == False:
        dl(rul + "/lib/python-3.8.2.exe","lib/python-3.8.2.exe","\t")
    if os.path.exists("lib/python-3.10.5.exe") == False:
        dl(rul + "/lib/python-3.10.5.exe","lib/python-3.10.5.exe","\t")

#    os.system("echo %PATH%")
#    os.system("ls")
#    os.system("pwd")
    install_diri = b"C:\jcm"
else:
    install_diri = b"/usr/jcm"

if os.path.exists("lib/pkg/main_V0.2.pkg") == False:
    dl("/pkg/main_V0.2.pkg","lib/pkg/main_V0.2.pkg","\t\t")

print(text["name"])
install_dir = b''
if len(sys.argv) == 1:
    if os.path.exists("/usr/bin/bashio"):
        fs = open("api.sh","wb")
        fs.write(b"#!/usr/bin/env bashio\r\n")
        fs.write(b"echo $(bashio::$1 $2)")
        fs.close()

        print(text["insdir"] + "[" + install_diri.decode("utf-8") + "] /config/jcm/main")
        install_dir = b"/config/jcm/main"
    else:
        install_dir = input(text["insdir"] + "[" + install_diri.decode("utf-8") + "] ").encode("utf-8")
else:
    if sys.argv[1] != "-y":
        if os.path.exists("/usr/bin/bashio"):
            fs = open("api.sh","wb")
            fs.write(b"#!/usr/bin/env bashio\r\n")
            fs.write(b"echo $(bashio::$1 $2)")
            fs.close()

            print(text["insdir"] + "[" + install_diri.decode("utf-8") + "] /config/jcm/main")
            install_dir = b"/config/jcm/main"
        else:
            install_dir = input(text["insdir"] + "[" + install_diri.decode("utf-8") + "] ").encode("utf-8")
if install_dir == b'':
    install_dir = install_diri
if len(sys.argv) == 1:
    if os.path.exists("/usr/bin/bashio"):
        install_port = os.popen("bashio api.sh config port").read().split("\n")[0]
        print(text["port"] + "[" + str(install_porti) + "] " + install_port)
    else:
        install_port = input(text["port"] + "[" + str(install_porti) + "] ")
else:
    if sys.argv[1] != "-y":
        if os.path.exists("/usr/bin/bashio"):
            install_port = os.popen("bashio api.sh config port").read().split("\n")[0]
            print(text["port"] + "[" + str(install_porti) + "] " + install_port)
        else:
            install_port = input(text["port"] + "[" + str(install_porti) + "] ")
if install_port == '':
    install_port = install_porti
else:
    install_port = int(install_port)
install_boot = b""
install_booti = b"yes"
if len(sys.argv) == 1:
    if os.path.exists("/usr/bin/bashio"):
        print(text["boot"] + "[" + install_booti.decode("utf-8") + "] " + "yes")
    else:
        install_boot = input(text["boot"] + "[" + install_booti.decode("utf-8") + "] ").encode("utf-8")
else:
    if sys.argv[1] != "-y":
        if os.path.exists("/usr/bin/bashio"):
            print(text["boot"] + "[" + install_booti.decode("utf-8") + "] " + "yes")
        else:
            install_boot = input(text["boot"] + "[" + install_booti.decode("utf-8") + "] ").encode("utf-8")
if install_boot == b'y' or install_boot == b'yes' or install_boot == b'':
    install_boot = install_booti
if os.path.exists("/usr/bin/bashio"):
    os.system("bashio api.sh log.info \"" + "#############################\"")
    os.system("bashio api.sh log.info \"" + text["insdir"] + "" + install_dir.decode("utf-8") + "\"")
    os.system("bashio api.sh log.info \"" + text["port"] + "" + str(install_port) + "\"")
    os.system("bashio api.sh log.info \"" + text["boot"] + "" + install_boot.decode("utf-8") + "\"")
    os.system("bashio api.sh log.info \"" + "#############################\"")
else:
    print("#############################")
    print(text["insdir"] + "" + install_dir.decode("utf-8"))
    print(text["port"] + "" + str(install_port))
    print(text["boot"] + "" + install_boot.decode("utf-8"))
    print("#############################")

install_ = b''
if OS_ == 'Windows':
    os.environ['PATH'] = os.environ['PATH'] + ';' + install_dir.decode("utf-8") + "\\Tools\\.bash\\bin"
if os.path.exists("/usr/bin/bashio"):
    print(text["qr"] + "yes")
else:
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
        #osss = OS.split('Windows 1')
        #if len(osss) == 2:
        #    print("install python3")
        #    if os.path.exists(install_dir.decode("utf-8") + "/Tools/.python") == False:
        #        #os.remove(install_dir.decode("utf-8") + "/Tools/.python")
        #        os.system(install_dir.decode("utf-8") + "/Tools/7z/7z.exe x " + pwd + "\\lib\\python-3.10.5.7z -r -o" + install_dir.decode("utf-8") + "\\ -aoa >>log.log")
        #else:
        #    if os.path.exists(install_dir.decode("utf-8") + "\\Tools\\NET") == False:
        #        print("install NET")
        #        os.mkdir(install_dir.decode("utf-8") + "\\Tools\\NET")
        #        os.system(pwd + '\\lib\\NET.exe /norestart /showfinalerror /passive')
        print("install python3")
        #    if os.path.exists(install_dir.decode("utf-8") + "\\Tools\\.python") == False:
        #        os.mkdir(install_dir.decode("utf-8") + "\\Tools\\.python")
        os.system(pwd + "\\lib\\python-3.10.5 /passive  TargetDir=" + install_dir.decode("utf-8") + "\\Tools\\.python InstallAllUsers=1 PrependPath=0")
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
        if os.path.exists(install_dir.decode("utf-8") + "/.out/main_V0.2.pkg") == False:
            os.mkdir(install_dir.decode("utf-8") + "/.out/main_V0.2.pkg")
        if os.path.exists(install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/") == False:
            os.mkdir(install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/")

        sh = "tar xzf lib/pkg/main_V0.2.pkg " + "-C .out/main_V0.2.pkg/"
        #print(sh)
        #os.system("pwd")
        os.system(sh)
        sh = install_dir.decode("utf-8") + "/.out/main_V0.2.pkg/.out/server/main/Package.py "
        sh = imp.load_source(sh,sh)
        sh.install("","","","","",pr)
        '''print("install APP")
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
        fs = open(install_dir.decode("utf-8") + "\\boot.py","wb")
        fs.write(b"\r\n\
import win32serviceutil\r\n\
import win32service\r\n\
import win32event\r\n\
import servicemanager\r\n\
import socket\r\n\
import sys\r\n\
import os\r\n\
import time\r\n\
\r\n\
class MyService(win32serviceutil.ServiceFramework):\r\n\
    _svc_name_ = 'jcm'\r\n\
    _svc_display_name_ = 'JCM'\r\n\
    _svc_description_ = 'Jiang Cluster Management.'\r\n\
\r\n\
    def __init__(self, args):\r\n\
        win32serviceutil.ServiceFramework.__init__(self, args)\r\n\
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)\r\n\
        socket.setdefaulttimeout(60)\r\n\
        self.is_running = True\r\n\
\r\n\
    def SvcStop(self):\r\n\
        os.system(\"stop.bat\")\r\n\
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)\r\n\
        win32event.SetEvent(self.hWaitStop)\r\n\
        self.is_running = False\r\n\
\r\n\
    def SvcDoRun(self):\r\n\
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,\r\n\
                              servicemanager.PYS_SERVICE_STARTED,\r\n\
                              (self._svc_name_, ''))\r\n\
        self.main()\r\n\
\r\n\
    def main(self):\r\n\
        # Your main logic here\r\n\
        os.chdir(\"" + install_dir + b"\")\r\n\
        os.system(\"run.bat\")\r\n\
        #time.sleep(5)\r\n\
        pass\r\n\
\r\n\
if __name__ == '__main__':\r\n\
    if len(sys.argv) == 1:\r\n\
        servicemanager.Initialize()\r\n\
        servicemanager.PrepareToHostSingle(MyService)\r\n\
        servicemanager.StartServiceCtrlDispatcher()\r\n\
    else:\r\n\
        win32serviceutil.HandleCommandLine(MyService)")
        fs.close()
        os.system("Tools\\.python\\python -m pip install pywin32")
        os.system("Tools\\.python\\python -m pip install pyinstaller")
        os.system("Tools\\.python\\Scripts\\pyinstaller.exe -D --hidden-import  win32serviceutil --hidden-import win32service --hidden-import win32event --hidden-import  servicemanager --hidden-import  win32timezone boot.py")
        os.system("del build /Q /S")
        os.system("dist\\boot\\boot.exe install")
        if install_boot == b'yes':
            #os.system(pwd + "/lib/CopyX /Y \"" + install_dir.decode("utf-8") + "\\boot.bat\" \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\"")
            os.system("sc config jcm start=auto")
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
        os.system("cp \"" + pwd + "/api.sh\" " + install_dir.decode("utf-8") + "/")
        os.system("chmod 777 " + install_dir.decode("utf-8") + "/api.sh")
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
        '''print("install APP")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg")
        os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out")
        sh = "tar xzf lib/pkg/APP_V0.2.pkg " + "-C .out/APP_V0.2.pkg/"
        os.system(sh)
        sh = install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out/server/APP/Package.py"
        sh = imp.load_source(sh,sh)
        sh.install("","","","","",pr)
'''
        fs = open(install_dir.decode("utf-8") + "/run.sh","wb")
        fs.write(b"#!/bin/bash\n")
        fs.write(b"cd " + install_dir + b"\n")
        fs.write(b"python3 -m venv venv\n")
        fs.write(b"source ./venv/bin/activate\n")
        fs.write(b"venv/bin/python server/jcm.py")
        fs.close()
        os.system('chmod 777 ' + install_dir.decode("utf-8") + "/run.sh")
        fs = open(install_dir.decode("utf-8") + "/stop.sh","wb")
        fs.write(b"#!/bin/bash\n")
        fs.write(b"cd " + install_dir + b"\n")
        fs.write(b"python3 -m venv venv\n")
        fs.write(b"source ./venv/bin/activate\n")
        fs.write(b"venv/bin/python server/jcm.py stop")
        fs.close()
        os.system('chmod 777 ' + install_dir.decode("utf-8") + "/stop.sh")
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
            fs.write(b"ExecStart=/bin/bash " + install_dir + b"/run.sh\n")
            fs.write(b"ExecStop=/bin/bash " + install_dir + b"/stop.sh\n")
            fs.write(b"\n")
            fs.write(b"[Install]\n")
            fs.write(b"WantedBy=multi-user.target\n")
            fs.close()
            os.system('chmod 777 ' + install_dir.decode("utf-8") + "/jcm.service")
            os.system("cp  \"" + install_dir.decode("utf-8") + "/jcm.service\" \"/usr/lib/systemd/system/\"")
            if install_boot == b'yes':
                os.system("systemctl enable jcm.service")
                #os.system("systemctl status jcm.service")
            else:
                os.system("systemctl disable jcm.service")
                #os.system("systemctl status jcm.service")
        elif os.path.exists("/etc/rc.d"):
            if install_boot == b'yes':
                os.system("cp run.sh /etc/rc.d/S99jcm")

        
    if OS_ == 'Windows':
        os.system("run.bat")
    else:
        if os.path.exists("/usr/bin/bashio"):
            os.system("/usr/bin/bashio run.sh")
        else:
            os.system("sh run.sh")
