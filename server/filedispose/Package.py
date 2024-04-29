# coding=utf-8
#!/bin/python
#cding=utf-8
# encoding=utf8

import os
import sys

name = "filedispose"
Version = "V0.2"

def install(new_client_socket,post,Versino,Headers,info,prin):
    pkg=""
    try:
        fs = open("server/server.ini", "rb")
        pkg = fs.read().decode("utf-8").split('\n')
    except Exception as e:
        prin(new_client_socket,(e.args).encode("utf-8"))
    inpkg = "install"
    for i in pkg:
        if i.split('\r')[0] == name:
            inpkg = ""
    prin(new_client_socket,("install " + name + " " + Version + "\n\r").encode("utf-8"))       
    os.system("cp -rf .out/" + name + "_" + Version + ".pkg/.out/* ./")
    
    if inpkg == "install":
        os.system("echo " + name + ">>server/server.ini")
#    prin(new_client_socket,("END\n\r").encode("utf-8"))  
    os.system("rm -rf .out/" + name + "_" + Version + ".pkg")
def remove():
    os.system("rm -rf server/" + name)
    os.system("rm -rf web/" + name)
def out():
    #os.system("cp -rf web/" + name + " .out/web/")
    os.system("cp -rf web/Ace_Admin/" + name + " .out/web/Ace_Admin/")
    os.system("cp -rf server/" + name + " .out/server/")
    
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
    data["names"] = "文件处理"
    #多国语言翻译
    data["namei"] = {}
    data["namei"]["zh-CN"] = "文件处理".encode("utf-8")
    #版本
    data["Version"] = Version
    #依赖
    data["Depends"] = "main"
    #License
    data["License"] = "GPL-2.0"
    #首选解释
    data["Description"] = "文件处理"
    #多国语言翻译
    data["Descriptions"] = {}
    data["Descriptions"]["zh-CN"] = "文件处理".encode("utf-8")
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