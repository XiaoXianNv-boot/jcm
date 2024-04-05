# coding=utf-8
#!/bin/python

import os
import sys
#import imp
import importlib
import locale
import platform

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

info = {}
info["Versino"] = ""
info["python"] = "python"
info["dir"] = "dir"
info["OS"] = "OS_"
info["OS_name"] = "OS"
info["port"] = "port"
info["dev_name"] = "dev_name"
info["theme"] = "Ace_Admin"
info["Headers"] = "Server: JCM/1.0\r\n"
info['debug'] = False
info['tmp'] = '/tmp/jcm'

#获取版本
def catVersino():
    sh = "server/main/Package.py"
    sh = importlib.machinery.SourceFileLoader(sh, sh).load_module()
    info["Versino"] = sh.Version
    info["Headers"] = "Server: JCM/" + sh.Version + "\r\n"
#获取端口
def catport():
    info["port"] = 8888
    if os.path.exists(".config/main/port"):
        fs = open(".config/main/port", "rb")
        ini = fs.read().decode("utf-8")
        info["port"] = int(ini)
#获取Python地址
info["python"] = sys.executable
#获取目录
info["dir"] = os.getcwd()
#获取OS类型
info["OS"] = platform.system()
#获取OS名称
def catosname():
    if info["OS"] == "Windows":
        sh = os.popen("systeminfo")
        shell = sh.read().split('\n')
        for sh in range(len(shell)):
            #print('[' + str(sh) + '] ' + shell[sh])
            sh = shell[sh].split('  ')
            if sh[0] == iftext["osname"]:
                info["OS_name"] = sh[-1]
            if sh[0] == iftext["devname"]:
                info["dev_name"] = sh[-1]
    else:
        if os.path.exists('/etc/os-release'):
            sh = os.popen("cat /etc/os-release | grep PRETTY_NAME")
            shell = sh.read().split('"')
            info["OS_name"] = shell[1]
        else:
            sh = os.popen("uname -n")
            shell = sh.read()
            info["OS_name"] = shell[:-1]
    sh = os.popen('cat /etc/hostname')
    info["dev_name"] = sh.read().split('\r')[0].split('\n')[0]

catVersino()
catport()
catosname()

if os.path.exists(".config/main/debug"):
    info['debug'] = True

sh = os.popen(info["python"] + " -V")
shell = sh.read().split('\n')

if os.path.exists("info.sh"):
    os.system("./info.sh '" + shell[0] + "'")
    os.system("./info.sh '" + "JCM " + info["Versino"] + "'")
    os.system("./info.sh '" + "name: " + info["dev_name"] + "'")
    os.system("./info.sh '" + "python: " + info["python"] + "'")
    os.system("./info.sh '" + "dir: " + info["dir"] + "'")
    os.system("./info.sh '" + "OS: " + info["OS"] + "'")
    os.system("./info.sh '" + "OS: " + info["OS_name"] + "'")
    os.system("./info.sh '" + "port: " + str(info["port"]) + "'")
    os.system("./info.sh '" + "theme: " + info["theme"] + "'")
else:
    print(shell[0])
    print("JCM " + info["Versino"])
    print("name: " + info["dev_name"])
    print("python: " + info["python"])
    print("dir: " + info["dir"])
    print("OS: " + info["OS"])
    print("OS: " + info["OS_name"])
    print("port: " + str(info["port"]))
    print("theme: " + info["theme"])
try:
    import psutil
    print("Net: ")
    net = psutil.net_if_addrs()
    for i in net:
        addrees = net[i]
        addrees = addrees[0]
        addrees = addrees.address
        print('\t' + i + '\t' + addrees)
except Exception as e:
    print(e.args)

if info['debug']:
    if os.path.exists("info.sh"):
        os.system("./info.sh '" + "DEBUG" + "'")
        os.system("error.sh '" + "DEBUG" + "'")
    print('Debug')

#run = imp.load_source('run',"server/run.py")
run = importlib.machinery.SourceFileLoader('run', "server/run.py").load_module()
#if install == "L":
#    if OS_ == "Linux":
#        os.system("systemctl start jcm.service")
#    else:
#        os.system("dist/boot/boot.exe start")
run.main(info)
print("end")