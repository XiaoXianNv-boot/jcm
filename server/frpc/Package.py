# coding=utf-8
#!/bin/python
#cding=utf-8
# encoding=utf8

import os
import sys
import platform

name = "frpc"
Version = "V0.2"

def catcw(datas,m):
    try:
        datas = datas + os.read(m,1)
        datas.decode("utf-8")
    except Exception as e:
        datas = catcw(datas,m)
    return datas

def installs(new_client_socket,post,Versino,Headers,info,prin,file):
    os.system("tar xf " + file + " -C .tmp")
    sh = file.split('/')[-1][:-7]
    sh = os.popen(".tmp/" + sh + "/frpc -v").read()[:-1]
    if sh == '':
        sh = os.popen("cd Tools/.frp/ && pwd").read()[:-1]
        prin(new_client_socket,("出现错误,请手动将frpc可执行文件复制到\r\n").encode("utf-8")) 
        prin(new_client_socket,(sh + "/\r\n").encode("utf-8")) 
        prin(new_client_socket,("ERROR " + sh + "/frpc -v\r\n").encode("utf-8")) 
        prin(new_client_socket,("      no data\r\n").encode("utf-8")) 
    else:
        prin(new_client_socket,("安装 frp " + sh + " ...\r\n").encode("utf-8"))  
    os.system("mkdir -p Tools/.frp")
    sh = file.split('/')[-1][:-7]
    os.system("mv .tmp/" + sh + "/frpc* Tools/.frp/")
    os.system("mv .tmp/" + sh + "/LICENSE Tools/.frp/")
    os.system("rm -rf .tmp/" + sh + " server/frpc/lib")

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
    prin(new_client_socket,("系统类型 " + platform.system() + " \n\r").encode("utf-8"))
    prin(new_client_socket,("系统架构 " + platform.machine() + " \n\r").encode("utf-8")) 
    gz = platform.machine()  
    os.system("cp -rf .out/" + name + "_" + Version + ".pkg/.out/* ./")
    if platform.system() == "Windows":
        pkg = ''
    else:
        if gz == "armv7l":
            gz = "arm"
            os.system('mkdir -p .tmp')
            installs(new_client_socket,post,Versino,Headers,info,prin,"server/frpc/lib/frp_0.51.3_linux_" + gz + ".tar.gz")
            
        elif gz == "x86_64":
            gz = "amd64"
            os.system('mkdir -p .tmp')
            installs(new_client_socket,post,Versino,Headers,info,prin,"server/frpc/lib/frp_0.51.3_linux_" + gz + ".tar.gz")

        elif gz == "aarch64":
            gz = "arm64"
            os.system('mkdir -p .tmp')
            installs(new_client_socket,post,Versino,Headers,info,prin,"server/frpc/lib/frp_0.51.3_linux_" + gz + ".tar.gz")

        else:
            prin(new_client_socket,("安装脚本不支持此架构 " + platform.machine() + " \n\r").encode("utf-8"))  
            return
    
    if inpkg == "install":
        os.system("echo " + name + ">>server/server.ini")
    #prin(new_client_socket,("END\n\r").encode("utf-8"))     
    os.system("rm -rf .out/" + name + "_" + Version + ".pkg")
def remove():
    os.system("rm -rf server/" + name)
    os.system("rm -rf web/" + name)
def out():
    os.system("cp -rf web/Ace_Admin/" + name + " .out/web/Ace_Admin/")
    os.system("cp -rf server/" + name + " .out/server/")
    os.system("#cp -rf lib/frp .out/server/frpc/lib")
    
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
    print("name:frpc")
    print("Version:" + Version)
    print("Depends:main")
    print("License:GPL-2.0")
    print("Description:frp内网穿透客户端")
    print("issued:pkg") 

def ybsh(sh,file):
    os.system(sh)

def pri(new_client_socket,p):
    print(p.decode("utf-8"),end='')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv = sys.argv[0],"install"

    if sys.argv[1] == "install":
        install('','','','','',pri)
    elif sys.argv[1] == "remove": 
        remove()
    elif sys.argv[1] == "out":
        out()
    else:
        info()