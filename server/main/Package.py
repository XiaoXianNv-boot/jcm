# coding=utf-8
#!/bin/python
#cding=utf-8
# encoding=utf8

import os
import sys

name = "main"
Version = "V0.2"

def install(new_client_socket,post,Versino,Headers,info,prin):
    import imp
    pkg=""
    try:
        fs = open("server/server.ini", "rb")
        pkg = fs.read().decode("utf-8").split('\n')
    except Exception as e:
        prin(new_client_socket,(e.args[-1]).encode("utf-8"))
    inpkg = "install"
    for i in pkg:
        if i.split('\r')[0] == name:
            inpkg = ""
    prin(new_client_socket,("install " + name + " V0.2\n\r").encode("utf-8"))      
    os.system("cp -rf .out/" + name + "_V0.2.pkg/.out/* ./")
    
    if inpkg == "install":
        os.system("echo " + name + ">>server/server.ini")
    inpkg = "install"
    for i in pkg:
        if i.split('\r')[0] == 'info':
            inpkg = ""
    if inpkg == "install":
        os.system("echo " + 'info' + ">>server/server.ini")
    inpkg = "install"
    for i in pkg:
        if i.split('\r')[0] == 'setup':
            inpkg = ""
    if inpkg == "install":
        os.system("echo " + 'setup' + ">>server/server.ini")
    prin(new_client_socket,("重启服务\n\r").encode("utf-8"))   
    if new_client_socket != "":
        #os.system("sh run.sh &")
        run = imp.load_source('run',"server/run.py")
        #run.reset()
        run.shutdown("reset")
        #sys.exit()
    #prin(new_client_socket,("END\n\r").encode("utf-8"))   
    os.system("rm -rf .out/" + name + "_V0.2.pkg")
def remove():
    os.system("rm -rf server/" + name)
    os.system("rm -rf web/" + name)
def out():
    os.system("cp -rf web/Ace_Admin/" + name + " .out/web/Ace_Admin/")
    os.system("cp -rf server/" + name + " .out/server/")
    os.system("cp -rf web/Ace_Admin/" + 'info' + " .out/web/Ace_Admin/")
    os.system("cp -rf server/" + 'info' + " .out/server/")
    os.system("cp -rf web/Ace_Admin/" + 'setup' + " .out/web/Ace_Admin/")
    os.system("cp -rf server/" + 'setup' + " .out/server/")
    #os.system("cp -rf web/" + "info" + " .out/web/")
    os.system("cp -rf web/Ace_Admin/" + "assets" + " .out/web/Ace_Admin/")
    os.system("cp -rf web/Ace_Admin/" + "*.php" + " .out/web/Ace_Admin/")
    os.system("cp -rf web/" + "*.ico" + " .out/web/")
    os.system("cp -rf web/Ace_Admin/" + "*.js" + " .out/web/Ace_Admin/")
    os.system("cp -rf web/Ace_Admin/" + "*.html" + " .out/web/Ace_Admin/")
    os.system("cp -rf server/" + "info" + " .out/server/")
    os.system("cp -rf server/" + "jcm.py" + " .out/server/")
    #os.system("cp -rf server/" + "php.py" + " .out/server/")
    os.system("cp -rf server/" + "run.py" + " .out/server/")
    os.mkdir(".out/Tools")
    os.system("cp -rf Tools/Tools.bat .out/Tools/")
    os.system("cp -rf Tools/Tools.sh .out/Tools/")
    os.system("cp -rf Tools/Tools.py .out/Tools/")
    os.system("cp -rf Tools/install.bat .out/Tools/")
    os.system("cp -rf Tools/install.sh .out/Tools/")
    os.system("cp -rf Tools/install.py .out/Tools/")
    
    rm('.out/server/','__pycache__')
    
#    os.system("find .out/  -name __pycache__")
def rm(dir,name):
    path = os.listdir(dir)
    for p in path:
        if os.path.isdir(dir + p):
            if p == name:
                os.system("rm -rf " + dir + name)
            else:
                rm(dir + p + '/',name)
def info():
    data = {}
    #文件夹名称
    data["Package"] = name
    #首选名称
    data["names"] = "首页"
    #多国语言翻译
    data["namei"] = {}
    data["namei"]["zh-CN"] = "首页".encode("utf-8")
    #版本
    data["Version"] = Version
    #依赖
    data["Depends"] = "main"
    #License
    data["License"] = "GPL-2.0"
    #首选解释
    data["Description"] = "此软件包包含基本文件系统和系统脚本"
    #多国语言翻译
    data["Descriptions"] = {}
    data["Descriptions"]["zh-CN"] = "此软件包包含基本文件系统和系统脚本".encode("utf-8")
    #库名称
    data["issued"] = "pkg"

    return data

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv = sys.argv[0],"install"

    if sys.argv[1] == "install":
        install('','','','','')
    elif sys.argv[1] == "remove": 
        remove()
    elif sys.argv[1] == "out":
        out()
    else:
        info()