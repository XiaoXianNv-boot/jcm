# coding=utf-8
#!/bin/python

import os
import sys
import imp
import locale
import platform

OS=''
Versino = "0.0.2"
port = 8888
python = sys.executable
dir = os.getcwd()
OS = platform.system()
OS_ = ''
dev_name = ''
bin = ''
bash = ''
ipaddr = ''
install = ''

iftext = {}
iftext["osname"] = "OS Name:"
iftext["devname"] = "Host Name:"
iftext["netdir"] = "Network Card(s):"
iftext["netname"] = "Connection Name:"
iftext["ip"] = "IP addrees(es)"
text = {}
text["init"] = "init"
text["user"] = "User:"
text["passwor"] = "Password:"
#加载语言文件
try:
    language = locale.getdefaultlocale()
    language = language[0]
    #language = "zh_CN"
    if os.path.exists("language/server/init.py/" + language + ".py"):
        run = imp.load_source('run',"language/server/init.py/" + language + ".py")
        for textname in iftext.keys():
            try:
                textval = run.text[textname]
                iftext[textname] = textval
            except Exception as e:
                print(e.args)
except Exception as e:
    print(e.args)

try:
    language = locale.getdefaultlocale()
    language = language[0]
    #language = "zh_CN"
    if os.path.exists("language/server/init.py/" + language + ".py"):
        run = imp.load_source('run',"language/server/init.py/" + language + ".py")
        for textname in text.keys():
            try:
                textval = run.text[textname]
                text[textname] = textval
            except Exception as e:
                print(e.args)
except Exception as e:
    print(e.args)

if OS != "Windows":
    try:
        sh = os.popen('uname')
        OS = sh.read().split('\n')[0]
        #if OS == ''or OS[:7] == 'MINGW32':
        osuser = os.popen("id -un").read().split('\n')[0].split('\r')[0]
        if osuser != "root":
            print("No root user,exit!")
            exit()
    except Exception as e:
        print(e.args)
else:
    os.environ['path']= dir + "\\Tools\\.bash\\bin\\;" +  os.getenv('path')
    python = '"' + python + '"'
    bash = dir + "\\Tools\\.bash\\bin\\"
    if os.path.exists(dir + "\\Tools\\7z") == False:
        os.system("mkdir Tools\\7z")
        cmd = "" + "xcopy " + dir + "\\lib\\7z\\* " + dir + "\\Tools\\7z"
        os.system(cmd)
    if os.path.exists(dir + "\\Tools\\.bash\\bin") == False:
        cmd = dir + "\\Tools\\7z\\7z.exe x " + dir + "\\lib\\bash.zip -r -o" + dir + "\\Tools\\"
        os.system(cmd)
OS_ = OS

def dpkginstall(name):
    pkg = ''
    if os.path.exists("/bin/apt"):
        if name == "update":
            os.system("apt update")
        pkg = "apt install -y "
    elif os.path.exists("/bin/yum"):
        pkg = "yum install -y "
    elif os.path.exists("/bin/opkg"):
        if name == "update":
            os.system("opkg update")
        pkg = "opkg install "
    if name == (python.split('/')[-1] + "-pip "):
        if os.path.exists("/bin/pip3") == False:
            os.system(pkg + " " + name)
    elif name == "update":
        print()
    elif name == (python.split('/')[-1] + "-dev"):
        if pkg == "yum":
            os.system(pkg + "  " + python.split('/')[-1] + "-devel")
        else:
            os.system(pkg + "  " + name)
    elif name == ("gcc"):
        if os.path.exists("/bin/gcc") == False:
            os.system(pkg + "  " + name)
    elif name == ("curl"):
        if os.path.exists("/bin/curl") == False:
            os.system(pkg + "  " + name)
    
def pip(name):
    run = 1
    if os.path.exists("info.sh"):
        os.system("./info.sh '" + name + "'")
    print('pip ' + name)
    while run == 1:
        run = pipinstall(name,"  ")
        if run == 1:
            run = pipinstall(name,"https://pypi.tuna.tsinghua.edu.cn/simple")
            if run == 1:
                link = ''
                if name == 'psutil':
                    link = '==4.4.2'
                run = pipinstall(name,link)
                if run == 1:
                    run = pipinstall(name,link + " -i https://pypi.tuna.tsinghua.edu.cn/simple")

def pipinstall(name,link):
    sh = os.popen("" + python + " -m pip list | " + bash + "grep '" + name + "'")
    shell = sh.read().split(' ')
    if shell[0] != name:
        if link[0] == 'h':
            link = ' -i ' + link
        os.system(bin + "" + python + " -m pip install --break-system-packages " + name + link)
        sh = os.popen("" + python + " -m pip list | " + bash + "grep '" + name + "'")
        shell = sh.read().split(' ')
        if shell[0] == name:
            pr = ''
            for p in shell[:-1]:
                pr = pr + p
                if pr == name:
                    pr = pr + ' '
            if os.path.exists("info.sh"):
                os.system("./info.sh '" + pr + "'")
            print(pr)
            return 0
    else:
        pr = ''
        for p in shell[:-1]:
            pr = pr + p
            if pr == name:
                pr = pr + ' '
        if os.path.exists("info.sh"):
            os.system("./info.sh '" + pr + "'")
        print(pr)
        return 0
    return 1
def file(dir,new):
    if not os.path.exists(dir):
        fs = open(dir,"w")
        fs.write(new)
        fs.close()

if OS == 'Windows':
    ifnet = False
    ifip = False
    ifkg = False
    sh = os.popen("systeminfo")
    shell = sh.read().split('\n')
    for sh in range(len(shell)):
        #print('[' + str(sh) + '] ' + shell[sh])
        sh = shell[sh].split('  ')
        if sh[0] == iftext["osname"]:
            OS = sh[-1]
        if sh[0] == iftext["devname"]:
            dev_name = sh[-1]
        if ifnet:
            data = ''
            kg = 0
            if sh[0] != '':
                ifnet = False
            else:
                for ss in sh:
                    data = data + ss
                    if ss != '':
                        data = data + '\t'
                    else:
                        kg = kg + 1
                sh = data.split('\t')
                if ifip:
                    if ifkg == False or ifkg == kg:
                        if sh[0][0] == '[':
                            sh = sh[0].split(' ')
                            ipaddr = ipaddr + sh[1] + ' '
                            if ifkg == 0:
                                ifkg = kg
                    else:
                        ifip = False
                        ipaddr = ipaddr + '\r'
                if sh[0] == iftext["ip"]:
                    ifip = True
            if sh[0] == iftext["netname"]:
                ipaddr = ipaddr + sh[1] + '\t'
        if sh[0] == iftext["netdir"]:
            ifnet = True
    if OS == '':
        if os.path.exists("info.sh"):
            os.system("./info.sh '" + text["oserr"] + "'")
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
    dev_name = sh.read().split('\r')[0].split('\n')[0]


if os.path.exists(".logs") == False:
    os.mkdir(".logs")
if os.path.exists(".logs/run.py") == False:
    os.mkdir(".logs/run.py")
if os.path.exists(".config/main/user") == False:
    if os.path.exists(".config") == False:
        os.mkdir(".config")
    if os.path.exists(".config/main") == False:
        os.mkdir(".config/main")
    print(text["init"])
    user = ''
    if os.path.exists("/usr/bin/bashio"):
        user = os.popen("bashio api.sh config user").read().split("\n")[0]
        print(text["user"] + user)
        user = user.encode("utf-8")
    else:
        user = input(text["user"]).encode("utf-8")
    password = ''
    if os.path.exists("/usr/bin/bashio"):
        password = os.popen("bashio api.sh config password").read().split("\n")[0]
        print(text["passwor"] + password)
        password = password.encode("utf-8")
    else:
        password = input(text["passwor"]).encode("utf-8")
    tools = imp.load_source('tools',"Tools/Tools.py")
    tools.newuser(user,password,b"0")
    if OS_ == "Linux":
        install = "L"

if os.path.exists(".config/main/port"):
    fs = open(".config/main/port", "rb")
    ini = fs.read().decode("utf-8")
    port = int(ini)
if len(sys.argv) == 5:
    if sys.argv[1] == "hass":
        print(sys.argv)
        port = int(sys.argv[2])
file(".config/main/cookie","\n")
file(".config/sessino","sessinon\n")
file(".config/main/lits.json",'{"name":"'+"127.0.0.1"+'","host":"'+"127.0.0.1"+'"},' + '\n')

OSS = OS.split(' ')
if OS_ == "Windows":
    pip("psutil")
    pip("pywin32")
elif OS == "DSM":
    if os.path.exists("server/psutil.py") == False:
        os.system('cp lib/psutil.py ./server/')
    if os.path.exists("server/_common.py") == False:
        os.system('cp lib/_common.py ./server/')
elif OS_ == "Linux":
    t = 0
    if len(sys.argv) == 5:
        if sys.argv[1] == "hass":
            t = 1
    if t == 0:
        dpkginstall("update")
        dpkginstall(python.split('/')[-1] + "-pip ")
        dpkginstall(python.split('/')[-1] + "-dev")
        dpkginstall("gcc")
        dpkginstall("curl")
    pip("psutil")

    OS_ = os.popen('if [ "$(stat -c %d:%i /)" != "$(stat -c %d:%i /proc/1/root/.)" ]; then   echo "chroot"; else   echo "Linux"; fi').read().split('\r')[0].split('\n')[0]

sh = os.popen(python + " -V")
shell = sh.read().split('\n')

theme = "Ace_Admin"

if os.path.exists("info.sh"):
    os.system("./info.sh '" + shell[0] + "'")
    os.system("./info.sh '" + "JCM " + Versino + "'")
    os.system("./info.sh '" + "name: " + dev_name + "'")
    os.system("./info.sh '" + "python: " + python + "'")
    os.system("./info.sh '" + "dir: " + dir + "'")
    os.system("./info.sh '" + "OS: " + OS + "'")
    os.system("./info.sh '" + "OS: " + OS_ + "'")
    os.system("./info.sh '" + "port: " + str(port) + "'")
    os.system("./info.sh '" + "theme: " + theme + "'")
print(shell[0])
print("JCM " + Versino)
print("name: " + dev_name)
print("python: " + python)
print("dir: " + dir)
print("OS: " + OS)
print("OS: " + OS_)
print("port: " + str(port))
print("theme: " + theme)
for iipp in ipaddr.split('\r'):
    print(iipp)

info = {}
info["Versino"] = Versino
info["python"] = python
info["dir"] = dir
info["OS"] = OS_
info["OS_name"] = OS
info["port"] = port
info["dev_name"] = dev_name
info["theme"] = theme
info["Headers"] = "Server: JCM/1.0\r\n"
info["ip"] = iipp
info['debug'] = False
info['tmp'] = '/tmp/jcm'

if os.path.exists(".config/main/debug"):
    info['debug'] = True

if dev_name == ' JIANG-G5-5500-P':
    info['debug'] = True
if info['debug']:
    if os.path.exists("info.sh"):
        os.system("./info.sh '" + "DEBUG" + "'")
        os.system("error.sh '" + "DEBUG" + "'")
    print('Debug')


run = imp.load_source('run',"server/run.py")
if install == "L":
        os.system("systemctl start jcm.service")
run.main(info)
print("end")