# coding=utf-8
#!/bin/python

import os
import sys
#import imp
import importlib
import platform
import shutil
import binascii
import hashlib
import locale
import socket
import ssl
from ssl import SSLContext

#cmd = sys.executable
#cmd = cmd + " -m pip install requests"
#os.system(cmd)
#import requests
#import urllib3
#urllib3.disable_warnings()

#os.chdir("install/jcm_install")

#gitrul = "https://github.com/XiaoXianNv-boot/jcm/raw/master"
gitrul = "https://github.com/XiaoXianNv-boot/jcm/releases/download"
mirrorrul = "http://jiang144.i234.me/data/jcm"
mirrorrul = "http://openwrt.lan/data/jcm"

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
text["init"] = "init"
text["user"] = "User:"
text["passwor"] = "Password:"

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


def bitto(size):
    if size < 1024:
        ramall = str(size)
        ramall = ramall + "B"
    elif size < (1024 * 1024):
        ramall = str(size / 1024)
        if len(ramall.split('.')) == 2:
            if len(ramall.split('.')[1]) > 2:
                ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "KB"
            else:
                ramall = ramall + "KB"
        else:
            ramall = ramall + "KB"
    elif size < (1024 * 1024 * 1024):
        ramall = str(size / 1024 / 1024)
        if len(ramall.split('.')) == 2:
            if len(ramall.split('.')[1]) > 2:
                ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "MB"
            else:
                ramall = ramall + "MB"
        else:
            ramall = ramall + "MB"
    elif size < (1024 * 1024 * 1024 * 1024):
        ramall = str(size / 1024 / 1024 / 1024)
        if len(ramall.split('.')) == 2:
            if len(ramall.split('.')[1]) > 2:
                ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "GB"
            else:
                ramall = ramall + "GB"
        else:
            ramall = ramall + "GB"
    return ramall
    

def start(data,lens,lenmax,new_client_socket,datas,hasattr):
    cat = hasattr[0].split(b" ")[1].decode('utf-8')
    prin = datas["prin"]
    dir  = datas["dir"]
    d    = datas["d"]
    if cat == "200":
        unit = lenmax / 50
        nb_traits = lens / unit
        nb_traits = int(str(nb_traits).split('.')[0])
        progress_bar( nb_traits,dir.split('/')[-1],d)
    
    return datas
def loop(data,lens,lenmax,new_client_socket,datas,hasattr):
    cat = hasattr[0].split(b" ")[1].decode('utf-8')
    prin = datas["prin"]
    dir  = datas["dir"]
    d    = datas["d"]
    if cat == "200":
        unit = lenmax / 50
        nb_traits = lens / unit
        nb_traits = int(str(nb_traits).split('.')[0])
        progress_bar( nb_traits,dir.split('/')[-1],d)
    #print("[" + str(lens) + " / " + str(lenmax) + "]\r",end="")

    return datas
def end(data,lens,lenmax,new_client_socket,datas,hasattr):
    #print("[" + str(lens) + " / " + str(lenmax) + "]\r",end="")
    prin = datas["prin"]
    dir  = datas["dir"]
    d    = datas["d"]
    sys.stdout.write("\r{}".format(dir.split('/')[-1]) + d + " : Extracting...{}".format(" "*51)) # Ugly but works everywhere
    sys.stdout.flush()

    print("\r{}".format(dir.split('/')[-1]) + d + " : Pull complete [{}]".format(lenmax))
    
    return datas

def curl(rul,new_client_socket,file,datas,start,loop,stop):
    tmp = rul.split('/')
    tmpp = ''
    if tmp[0] == 'http:':
       tmpp = (tmp[2] + ':80').split(':')
    else:
        tmpp = (tmp[2] + ':443').split(':')
    ruldir = "/".split('/')
    ruldir[0] = tmp[0] + '//'
    if len(tmpp) == 2:
        ruldir[1] = rul[(len(ruldir[0] + tmpp[0])):]
    else:
        ruldir[1] = rul[(len(ruldir[0] + tmpp[0] + ':' + tmpp[1])):]
    host = tmpp[0]
    port = int(tmpp[1])
    dir  = ruldir[1]

    socket.setdefaulttimeout(1)
    client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象

    if ruldir[0] == "https://":
        '''fs = open("ca.crt","wb")
        fs.write(b"-----BEGIN CERTIFICATE-----\n")
        fs.write(b"MIIDrzCCApegAwIBAgIQCDvgVpBCRrGhdWrJWZHHSjANBgkqhkiG9w0BAQUFADBh\n")
        fs.write(b"MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n")
        fs.write(b"d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD\n")
        fs.write(b"QTAeFw0wNjExMTAwMDAwMDBaFw0zMTExMTAwMDAwMDBaMGExCzAJBgNVBAYTAlVT\n")
        fs.write(b"MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5j\n")
        fs.write(b"b20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IENBMIIBIjANBgkqhkiG\n")
        fs.write(b"9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4jvhEXLeqKTTo1eqUKKPC3eQyaKl7hLOllsB\n")
        fs.write(b"CSDMAZOnTjC3U/dDxGkAV53ijSLdhwZAAIEJzs4bg7/fzTtxRuLWZscFs3YnFo97\n")
        fs.write(b"nh6Vfe63SKMI2tavegw5BmV/Sl0fvBf4q77uKNd0f3p4mVmFaG5cIzJLv07A6Fpt\n")
        fs.write(b"43C/dxC//AH2hdmoRBBYMql1GNXRor5H4idq9Joz+EkIYIvUX7Q6hL+hqkpMfT7P\n")
        fs.write(b"T19sdl6gSzeRntwi5m3OFBqOasv+zbMUZBfHWymeMr/y7vrTC0LUq7dBMtoM1O/4\n")
        fs.write(b"gdW7jVg/tRvoSSiicNoxBN33shbyTApOB6jtSj1etX+jkMOvJwIDAQABo2MwYTAO\n")
        fs.write(b"BgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUA95QNVbR\n")
        fs.write(b"TLtm8KPiGxvDl7I90VUwHwYDVR0jBBgwFoAUA95QNVbRTLtm8KPiGxvDl7I90VUw\n")
        fs.write(b"DQYJKoZIhvcNAQEFBQADggEBAMucN6pIExIK+t1EnE9SsPTfrgT1eXkIoyQY/Esr\n")
        fs.write(b"hMAtudXH/vTBH1jLuG2cenTnmCmrEbXjcKChzUyImZOMkXDiqw8cvpOp/2PV5Adg\n")
        fs.write(b"06O/nVsJ8dWO41P0jmP6P6fbtGbfYmbW0W5BjfIttep3Sp+dWOIrWcBAI+0tKIJF\n")
        fs.write(b"PnlUkiaY4IBIqDfv8NZ5YBberOgOzW6sRBc4L0na4UU+Krk2U886UAb3LujEV0ls\n")
        fs.write(b"YSEY1QSteDwsOoBrp+uvFRTp2InBuThs4pFsiv9kuXclVzDAGySj4dzp30d8tbQk\n")
        fs.write(b"CAUw7C29C79Fv1C5qfPrmAESrciIxpg0X40KPMbp1ZWVbd4=\n")
        fs.write(b"-----END CERTIFICATE-----\n")
        fs.close()'''
        ssl._create_stdlib_context = ssl._create_unverified_context()
        ssl._create_default_https_context = ssl._create_unverified_context()
        context = ssl.create_default_context()
        ssl._create_stdlib_context = ssl._create_unverified_context()
        ssl._create_default_https_context = ssl._create_unverified_context()
        #client = ssl.wrap_socket(client,cert_reqs=ssl.CERT_REQUIRED,ca_certs='./ca.crt')
        #client = ssl.SSLContext.wrap_socket(client,cert_reqs=ssl.CERT_REQUIRED,ca_certs='./ca.crt')
        client = context.wrap_socket(client, server_hostname=host)
    fsdata = 'GET ' + dir + ' HTTP/1.1\r\n'
    if ruldir[0] == "https://":
        if port == 443:
            fsdata = fsdata + 'Host: ' + host + '\r\n'
        else:
            fsdata = fsdata + 'Host: ' + host + ':' + str(port) + '\r\n'
    else: 
        if port == 80:
            fsdata = fsdata + 'Host: ' + host + '\r\n'
        else:
            fsdata = fsdata + 'Host: ' + host + ':' + str(port) + '\r\n'
    fsdata = fsdata + 'Referer: ' + ruldir[0] + host + dir + '\r\n'
    
    client.connect((host,port))
    client.send((fsdata + '\r\n').encode("utf-8"))
    data = b''

    lens = 0     #已经下载长度
    lenmax = -1  #总长度
    run = 0
    hasattr = ""
    fs = ''
    try:
        while run == 0:
            d = client.recv(10240000)
            if d:
                if hasattr == "":
                    data += d
                    hasattr = data.split(b'\r\n\r\n')
                    if len(hasattr) == 1:
                        hasattr = ""
                    else:
                        hasattr = hasattr[0]
                        hasattr = hasattr.split(b'\r\n')
                        for ddd in hasattr:
                            dddd = ddd.split(b': ')
                            if dddd[0] == b'Content-Length':
                                lenmax = int(dddd[1])
                        lens = len(data[len(data.split(b'\r\n\r\n')[0])+4:])
                        data = data[len(data.split(b'\r\n\r\n')[0])+4:]
                        datas = start(data,lens,lenmax,new_client_socket,datas,hasattr)
                        if hasattr[0].split(b" ")[1] == b"200":
                            if file != '':
                                fs = open(file,'wb')
                                fs.write(data)
                        if lenmax == 0:
                            run = 1
                else:
                    lens += len(d) 
                    if hasattr[0].split(b" ")[1] == b"200":
                        if fs == '':
                            data += d
                        else:
                            fs.write(d)
                            data = b""
                    else:
                        data += d
                    datas = loop(data,lens,lenmax,new_client_socket,datas,hasattr)
                    if lens == lenmax:
                        run = 1
                        fs.close()
                        datas = stop(data,lens,lenmax,new_client_socket,datas,hasattr)
            else:
                run = 1
    except Exception as e:
        #print(e.args)
        if hasattr[0].split(b" ")[1] == b"200":
            os.remove(file)
        
    return hasattr,data

def wget(rul,new_client_socket,file,datas,start,loop,stop):
    hasattr,data = curl(rul,new_client_socket,file,datas,start,loop,stop)
    cat = hasattr[0].split(b" ")[1].decode('utf-8')
    prin = datas["prin"]
    if cat == '301':
        for d in hasattr:
            dd = d.split(b': ')
            if dd[0] == b'Location':
                rul = d[len(dd[0] + b": "):].decode("utf-8")
        #prin(new_client_socket,(' 301\r\n').encode("utf-8"))
        #prin(new_client_socket,rul.encode("utf-8"))
        hasattr,data = wget(rul,new_client_socket,file,datas,start,loop,stop)
    elif cat == '302':
        for d in hasattr:
            dd = d.split(b': ')
            if dd[0] == b'Location':
                rul = d[len(dd[0] + b": "):].decode("utf-8")
        #prin(new_client_socket,(' 302\r\n        ').encode("utf-8"))
        #prin(new_client_socket,rul.encode("utf-8"))
        hasattr,data = wget(rul,new_client_socket,file,datas,start,loop,stop)
    elif cat != '200':
        print("(" + cat + ")")
    #prin(new_client_socket,('\r\n').encode("utf-8"))
    return hasattr,data

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
    datas = {}
    datas["prin"] = pr
    datas["dir"]  = dir
    datas["d"]    = d
    wget(rul,"",dir,datas,start,loop,end)
    return
    #bresp = requests.get(rul, stream=True, verify=False, timeout=60)
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
        down(gitrul + "/language/" + language + ".py","language/Tools/install.py/" + language + ".py","\t\t\t")
    if os.path.exists("language/Tools/install.py/" + language + ".py") == False:#失败从mirror下载
        down(mirrorrul + "/install/language/install.py/" + language + ".py","language/Tools/install.py/" + language + ".py","\t\t\t")

    moduleName = 'run'
    fileName   = "language/Tools/install.py/" + language + ".py"
    #run = imp.load_source('run',"language/Tools/install.py/" + language + ".py")
    run = importlib.machinery.SourceFileLoader(moduleName, fileName).load_module()
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
    i = 10
    while i > 0:
        if os.path.exists(dir) == False:
            try:
                down(gitrul + rul,dir,d)
            except Exception as e:
                print(e.args)
        if os.path.exists(dir) == False:
            try:
                down(mirrorrul + rul,dir,d)
            except Exception as e:
                print(e.args)
        if os.path.exists(dir) == False:
            i= i - 1
            print("[ 10 / " + str(i) + " ]")
            if i == 0:
                print("Down ERR")
                exit()
        else:
            i = 0


#print(os.args)
if os.path.exists("tmp") == False:
    os.mkdir("tmp")
if os.path.exists("lib") == False:
    os.mkdir("lib")
def install():
    OS_ = platform.system()
    pwd = os.getcwd()
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
        #if os.path.exists("lib/instsrv.exe") == False:
        #    down(rul + "/lib/instsrv.exe","lib/instsrv.exe","\t\t\t")
        #if os.path.exists("lib/srvany.exe") == False:
        #    down(rul + "/lib/srvany.exe","lib/srvany.exe","\t\t\t")
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

    if os.path.exists("lib/pkg/main_V0.3.pkg") == False:
        dl("/pkg/main_V0.3.pkg","lib/pkg/main_V0.3.pkg","\t\t")

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
            if os.path.exists(install_dir.decode("utf-8") + "/.out/main_V0.3.pkg") == False:
                os.mkdir(install_dir.decode("utf-8") + "/.out/main_V0.3.pkg")
            if os.path.exists(install_dir.decode("utf-8") + "/.out/main_V0.3.pkg/") == False:
                os.mkdir(install_dir.decode("utf-8") + "/.out/main_V0.3.pkg/")

            sh = "tar xzf lib/pkg/main_V0.3.pkg " + "-C .out/main_V0.3.pkg/"
            #print(sh)
            #os.system("pwd")
            os.system(sh)
            sh = install_dir.decode("utf-8") + "/.out/main_V0.3.pkg/.out/server/main/Package.py "
            #sh = imp.load_source(sh,sh)
            sh = importlib.machinery.SourceFileLoader(sh, sh).load_module()
            sh.install("","","","","",pr)
            sh = install_dir.decode("utf-8") + "/Tools/install.py"
            sh = importlib.machinery.SourceFileLoader(sh, sh).load_module()
            sh.initaddr()

            '''print("install APP")
            sh = "tar xzf lib/pkg/APP_V0.2.pkg " + "-C .out/APP_V0.2.pkg/.out"
            os.system(sh)
            sh = install_dir.decode("utf-8") + "/.out/APP_V0.2.pkg/.out/server/APP/Package.py "
            sh = imp.load_source(sh,sh)
            sh.install("","","","","",pr)
            '''
            fs = open(install_dir.decode("utf-8") + "\\run.bat","wb")
            fs.write(b"@cd " + install_dir + b"\n")
            fs.write(b"@Tools\\.python\\python server\\jcm.py")
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
            #os.system("cp \"" + pwd + "/api.sh\" " + install_dir.decode("utf-8") + "/")
            #os.system("chmod 777 " + install_dir.decode("utf-8") + "/api.sh")
            os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out")
            os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/main_V0.3.pkg")
            os.system("mkdir -p " + install_dir.decode("utf-8") + "/.out/main_V0.3.pkg/.out")
            sh = "tar xzf lib/pkg/main_V0.3.pkg " + "-C .out/main_V0.3.pkg/"

            #print(sh)
            #os.system("pwd")
            os.system(sh)
            sh = install_dir.decode("utf-8") + "/.out/main_V0.3.pkg/.out/server/main/Package.py"
            #sh = imp.load_source(sh,sh)
            sh = importlib.machinery.SourceFileLoader(sh, sh).load_module()
            sh.install("","","","","",pr)
            sh = install_dir.decode("utf-8") + "/Tools/install.py"
            sh = importlib.machinery.SourceFileLoader(sh, sh).load_module()
            sh.initaddr()
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
            elif OS.split(" ")[0] == "OpenWrt":
                fs = open(install_dir.decode("utf-8") + "/run.sh","wb")
                fs.write(b"#!/bin/sh\n")
                fs.write(b"cd " + install_dir + b"\n")
                fs.write(b"python3 -m venv venv\n")
                fs.write(b"source ./venv/bin/activate\n")
                fs.write(b"venv/bin/python server/jcm.py")
                fs.close()
                fs = open("/etc/init.d/jcm","wb")
                fs.write(b"\
#!/bin/sh /etc/rc.common\n\
\n\
START=99\n\
STOP=1\n\
\n\
start() {\n\
    /bin/sh " + install_dir + b"/run.sh\n\
}     \n\
stop() {\n\
    /bin/sh " + install_dir + b"/stop.sh\n\
}    \n\
")
                fs.close()
                os.system('chmod 777 /etc/init.d/jcm')
                if install_boot == b'yes':
                    os.system("/etc/init.d/jcm enable")

            elif os.path.exists("/etc/rc.d"):
                if install_boot == b'yes':
                    os.system("cp run.sh /etc/rc.d/S99jcm")
        

        if OS_ == 'Windows':
            os.system("Tools\\.python\\python Tools/install.py init")
            os.system("run.bat")
        else:
            os.system("python3 -m venv venv")
            os.system("venv/bin/python3 Tools/install.py init")
            if os.path.exists("/usr/bin/bashio"):
                os.system("/usr/bin/bashio run.sh")
            else:
                os.system("sh run.sh")

def pip(name):
    run = 1
    print('pip ' + name)
    while run == 1:
        run = pipinstall(name,"  ")
        if run == 1:
            run = pipinstall(name,"  --break-system-packages ")
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
    python = sys.executable
    bash = ""
    bin = ""
    if platform.system() == "Windows":
        bash = "Tools\\.bash\\bin\\"
    sh = os.popen("" + python + " -m pip list | " + bash + "grep '" + name + "'")
    shell = sh.read().split("\n")[0].split(' ')
    if shell[0] != name:
        if link[0] == 'h':
            link = ' -i ' + link
        os.system(bin + "" + python + " -m pip install " + name + link)
        sh = os.popen("" + python + " -m pip list | " + bash + "grep '" + name + "'")
        shell = sh.read().split("\n")[0].split(' ')
        if shell[0] == name:
            pr = ''
            for p in shell:
                pr = pr + p
                if pr == name:
                    pr = pr + ' '
            if os.path.exists("info.sh"):
                os.system("./info.sh '" + pr + "'")
            print(pr)
            return 0
    else:
        pr = ''
        for p in shell:
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

def initaddr():
    text = {}
    text["init"] = "init"
    text["user"] = "User:"
    text["passwor"] = "Password:"
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
        else:
            user = input(text["user"]).encode("utf-8")
        password = ''
        if os.path.exists("/usr/bin/bashio"):
            password = os.popen("bashio api.sh config pass").read().split("\n")[0]
            print(text["passwor"] + password)
        else:
            password = input(text["passwor"]).encode("utf-8")
        #tools = imp.load_source('tools',"Tools/Tools.py")
        tools = importlib.machinery.SourceFileLoader('tools', "Tools/Tools.py").load_module()
        tools.newuser(user,password,b"0")
        #if OS_ == "Linux":
    file(".config/main/cookie","\n")
    file(".config/sessino","sessinon\n")
    file(".config/main/lits.json",'{"name":"'+"127.0.0.1"+'","host":"'+"127.0.0.1"+'"},' + '\n')


def init():
    OS = platform.system()
    python = sys.executable
    dir = os.getcwd()
    if OS != "Windows":
        try:
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
    if OS == "Windows":
        pip("psutil")
        pip("pywin32")
        pip("requests")
        pip("pythonnet")
    elif OS_ == "Linux":
        if os.path.exists("/bin/apt"):
            os.system("apt-get update")
            os.system("apt-get install -y python3-pip")
            os.system("apt-get install -y python3-dev")
            os.system("apt-get install -y gcc")
            os.system("apt-get install -y curl")
        elif os.path.exists("/bin/yum"):
            os.system("yum install -y python3-pip")
            os.system("yum install -y python3-devel")
            os.system("yum install -y gcc")
            os.system("yum install -y curl")
        elif os.path.exists("/bin/opkg"):
            os.system("opkg update")
            os.system("opkg install python3-pip")
            os.system("opkg install python3-dev")
            os.system("opkg install gcc")
            os.system("opkg install curl")
        pip("psutil")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv = (sys.argv[0] + " init").split(" ")

    if sys.argv[1] == "install":
        install()
    elif sys.argv[1] == "init": 
        initaddr()
        init()
