# coding=utf-8
#!/bin/python

import os
import sys
import imp
import locale

OS=''
Versino = "0.0.2"
port = 8888
python = sys.executable
dir = os.getcwd()
OS = "Windows"
OS_ = ''
dev_name = ''
bin = ''
bash = ''
gui = ''

iftext = {}
iftext["osname"] = "OS Name:"
iftext["devname"] = "Host Name:"
text = {}
text["init"] = "init"
text["user"] = "User:"
text["passwor"] = "Password:"
try:
    language = locale.getdefaultlocale()
    language = language[0]
    #language = "zh_CN"
    run = imp.load_source('run',"language/server/init.py/" + language + ".py")
    for textname in iftext.keys():
        try:
            textval = run.text[textname]
            iftext[textname] = textval
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
    pkginstallname = ""

def pip(name):
    run = 1
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
        os.system(bin + "" + python + " -m pip install " + name + link)
        sh = os.popen("" + python + " -m pip list | " + bash + "grep '" + name + "'")
        shell = sh.read().split(' ')
        if shell[0] == name:
            pr = ''
            for p in shell[:-1]:
                pr = pr + p
                if pr == name:
                    pr = pr + ' '
            print(pr)
            return 0
    else:
        pr = ''
        for p in shell[:-1]:
            pr = pr + p
            if pr == name:
                pr = pr + ' '
        print(pr)
        return 0
    return 1

    

def file(dir,new):
    if not os.path.exists(dir):
        fs = open(dir,"w")
        fs.write(new)
        fs.close()

def file(dir,new):
    if not os.path.exists(dir):
        fs = open(dir,"w")
        fs.write(new)
        fs.close()

if OS == 'Windows':
    sh = os.popen("systeminfo")
    shell = sh.read().split('\n')
    for sh in range(len(shell)):
        #print('[' + str(sh) + '] ' + shell[sh])
        sh = shell[sh].split('  ')
        if sh[0] == iftext["osname"]:
            OS = sh[-1]
        if sh[0] == iftext["devname"]:
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
    user = input(text["user"]).encode("utf-8")
    password = input(text["passwor"]).encode("utf-8")
    tools = imp.load_source('tools',"Tools/Tools.py")
    tools.newuser(user,password,b"0")
if os.path.exists(".config/main/port"):
    fs = open(".config/main/port", "rb")
    ini = fs.read().decode("utf-8")
    port = int(ini)
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
    pkginstall("update")
    pkginstall(python.split('/')[-1] + "-pip ")
    pkginstall(python.split('/')[-1] + "-dev")
    pkginstall("gcc")
    pkginstall("curl")
    pip("psutil")

    OS_ = os.popen('if [ "$(stat -c %d:%i /)" != "$(stat -c %d:%i /proc/1/root/.)" ]; then   echo "chroot"; else   echo "Linux"; fi').read().split('\r')[0].split('\n')[0]

sh = os.popen(python + " -V")
shell = sh.read().split('\n')

theme = "Ace_Admin"

print(shell[0])
print("JCM " + Versino)
print("name: " + dev_name)
print("python: " + python)
print("dir: " + dir)
print("OS: " + OS)
print("OS: " + OS_)
print("port: " + str(port))
print("theme: " + theme)

info = {}
info["Versino"] = Versino
info["python"] = python
info["dir"] = dir
info["OS"] = OS_
info["OS_name"] = OS
info["port"] = port
info["dev_name"] = dev_name
info["theme"] = theme
info['debug'] = False
info['debug'] = True

if dev_name == ' JIANG-G5-5500-P': #调试设备
    info['debug'] = True 
if info['debug']:
    print('Debug')


run = imp.load_source('run',"server/run.py")

run.main(info)
print("end")