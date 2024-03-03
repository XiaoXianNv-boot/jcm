# coding=utf-8
#!/bin/python
#cding=utf-8
# encoding=utf8

import os
import sys

name = "APP"
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
    os.system("rm -rf .out/web/APP/info.json")
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
    print("Package:" + name)
    print("name:应用商店")
    print("Version:" + Version)
    print("Depends:main")
    print("License:GPL-2.0")
    print("Description:软件的应用商店")
    print("issued:pkg")

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