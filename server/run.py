# coding=utf-8
#!/bin/python

import imp
import os
import time
import sys
import socket

import random
import psutil
import traceback
import threading

def rom(info):
    i=0
    retlist1=[]
    rom=0
    disks=1
    if info['OS'] == "Linux":
        romsh = os.popen("LANG=en_US df -h")
        list = romsh.read().split("\n")
        ilen = len(list)
        while i < ilen:
            if list[i] == "":
                i += 1
            elif list[i].split(" ")[0] == "Filesystem":
                i += 1
            elif list[i].split(" ")[0] == "udev":
                i += 1
            elif list[i].split(" ")[0] == "tmpfs":
                i += 1
            elif list[i].split(" ")[0] == "devtmpfs":
                i += 1
            elif list[i].split(" ")[0] == "overlay":
                i += 1
            elif list[i].split(" ")[0][:-1] == "/dev/zram":
                i += 1
            elif list[i].split(" ")[0][:-1] == "/dev/loop":
                i += 1
            else:

                diskinfo = int(list[i].split("%")[0].split(" ")[-1])

                if rom < diskinfo:
                    rom = diskinfo
                i=i+1
                disks += 1
    else:
        list = psutil.disk_partitions()
        ilen = len(list)
        while i < ilen:
            if list[i].mountpoint == "/boot":
                i += 1
            else:
                try:
                    diskinfo = psutil.disk_usage(list[i].mountpoint)
                    if rom < diskinfo.percent:
                        rom = diskinfo.percent
                except Exception as e:
                    if(len(e.args) == 2):
                        if e.args[1] != '设备未就绪。':
                            print(e.args)   
                    else:
                        print(e.args)   
                i=i+1
                disks += 1
    return str(rom)



def httpserver_void(new_client_socket,RUL,RUL_CS,post_data,Headers,logs,info):
    global session_
    global sent_before
    global recv_before
    global ttime
    global exre

    strr = {}
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    try:
        data = httpserver.catHeaders("Cookie",Headers)
        #print(data)
        data = httpserver.catCookie("Cluster_management_Jiang",Headers,session_.split('\n'))
        #print(data)
        user = ""
        tmp4 = session_.split('\n')
        for y in range(len(tmp4)):
            tmp5 = tmp4[y].split(',')
            if len(tmp5) >1:
                if data == tmp5[0]:
                    user = tmp5[1]
        if RUL == "/favicon.ico":
            if post_data == b'':
                post = RUL_CS.split('&')
            else:
                post = post_data.decode("utf-8").split('&')
            httpserver.httppostfile(new_client_socket,"200","./web" + RUL,True,Headers,info)
        else:
            if user == "":
                ma = "200"
                if RUL == "/login":
                    if Headers[0][:4] == "POST":
                        post = post_data.decode("utf-8").split('&')
                        name = ""
                        password = ""
                        checkbox = ""
                        for p in post:
                            pp = p.split("=")
                            if pp[0] == "name":
                                name = pp[1]
                            if pp[0] == "password":
                                password = pp[1]
                            if pp[0] == "checkbox":
                                checkbox = pp[1]
                        tools = imp.load_source("Tools/Tools.py","Tools/Tools.py")
                        tools = tools.ifuser(name,password)
                        res = ""
                        if tools == "yes":
                            cok = ''
                            for x in range(32):
                                cok = cok + random.choice("0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLLZXCVBNM")
                            fs_rr = session_
                            fs_session = fs_rr.split('\n')
                            for fs_ in fs_session:
                                if fs_ == "sessinon":
                                    session_ = (fs_)
                                    session_ = session_ + ("\n") 
                                else:
                                    if fs_ == "":
                                        fs_ = fs_
                                    else:
                                        session_ = session_ + fs_ + ("\n") 
                                        fs__ = fs_.split(',')
                            import datetime
                            cookie_date = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%a, %d %b %Y %H:%M:%S GMT")
                            #time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime(time.strptime("1","%d"))) 
                            
                            session_ = session_ + cok + "," + name + "," + cookie_date + "\n"
                            if checkbox == "true":
                                fs_user = open(".config/sessino","r")#sessino
                                fs_r = fs_user.read()
                                fs_rr = fs_r#.decode("utf-8")
                                fs_session = fs_rr.split('\n')
                                fs_user.close()
                                user_write = ''
                                for fs_ in fs_session:
                                    if fs_ == "sessinon":
                                        fs_ = fs_
                                    else:
                                        if fs_ == "":
                                            fs_ = fs_
                                        else:
                                            fs__ = fs_.split(",")
                                res = res + "set-Cookie: Cluster_management_Jiang=" + cok + "; SameSite=Lax; Expires=" + cookie_date
                                fs_user = open(".config/sessino","a")
                                fs_user.write(cok + "," + name + "," + cookie_date + "\n")
                                fs_user.close()
                            else:
                                res = res + "set-Cookie: Cluster_management_Jiang=" + cok + "; SameSite=Lax;"# Expires=" + cookie_date + "\r\n"
                            res = "application/json\r\n" + res
                            httpserver.httppostchar(new_client_socket,"200",b"{\"data\":\"login\"}",res,Headers,info)
                        else:
                            res = "application/json" + res
                            httpserver.httppostchar(new_client_socket,"200","{\"data\":\"用户名或密码错误\"}".encode("utf-8"),res,Headers,info)
                        
                if RUL[:len("/assets")] != "/assets":
                    RUL = "/login.html"
                    for h in Headers:
                        if h == 'Connection: Upgrade':
                            httpserver.websockinit(new_client_socket,Headers,info)
                            httpserver.websockend(new_client_socket,b"No Login\r\n")
                    ma = "401"
                RUL = "./web/" + info["theme"] + RUL
                httpserver.httppostfile(new_client_socket,ma,RUL,True,Headers,info)
            else:
                my_file = "./web/" + info["theme"] + RUL
                link = ''
                for i in RUL_CS.split('&'):
                    tmp = i.split('=')
                if tmp[0] == 'link':
                    link = tmp[1]
                if os.path.isdir(my_file):
                    if os.path.isfile("./web/" + info["theme"] + RUL + "/index.php"):
                        RUL = RUL + "/index.php"
                    else:
                        my_file = "./web/" + info["theme"] + RUL + "/index.html"
                        if os.path.isfile(my_file):
                            RUL = RUL + "/index.html" 
                if os.path.isfile("./web/" + info["theme"] + RUL):
                    tmp2 = RUL.split('.')
                    if tmp2[-1] == 'php':
                        php = imp.load_source("server/main/php.py","server/main/php.py")
                        if post_data == b'':
                            post = RUL_CS.split('&')
                        else:
                            post = post_data.decode("utf-8").split('&')
                        data = php.php(new_client_socket,post,RUL,user,Headers,info,strr)
                        httpserver.httppostchar(new_client_socket,"200",data.encode("utf-8"),"text/html;charset=UTF-8",Headers,info)
                    else:
                        RUL = "./web/" + info["theme"] + RUL
                        httpserver.httppostfile(new_client_socket,"200",RUL,True,Headers,info)
                else:
                    if RUL == "/login":
                        httpserver.httppostchar(new_client_socket,"200",b"{\"data\":\"login\"}","application/json",Headers,info)
                    elif RUL == "/token":
                        httpserver.httppostchar(new_client_socket,"200",b"{\"token\":\"\"}","application/json",Headers,info)
                    elif RUL == "/main/info":
                        res = ''
                        if os.path.isfile(".config/main/lits.json"):
                            fs = open(".config/main/lits.json", "rb")
                            hosts = fs.read().decode("utf-8").split('\n')
                            res += '{"for": "'+str(len(hosts)-1)+'","server": ['
                            for i in range(len(hosts)-1):
                                ii = hosts[i].split('"')
                                if i == 0 :
                                    res += '{"name": "'+ ii[3] +'",'
                                else:
                                    res += ',{"name": "'+ ii[3] +'",'
                                if ii[7] == "127.0.0.1":
                                    sent_now = psutil.net_io_counters().bytes_sent
                                    recv_now = psutil.net_io_counters().bytes_recv 
                                    sent = (sent_now - sent_before)/1024/(time.time()-ttime)  # 算出1秒后的差值 
                                    recv = (recv_now - recv_before)/1024/(time.time()-ttime)
                                    ttime=time.time()
                                    sent_before=sent_now
                                    recv_before=recv_now
                                    res += '"api": "1",'
                                    if info['OS'] == "Linux":
                                        res += '"safe": "--",'
                                    else:
                                        res += '"safe": "--",'
                                    res += '"cpu": "'+str(psutil.cpu_percent(None))+'",'
                                    res += '"ram": "'+str(psutil.virtual_memory().percent)+'",'
                                    res += '"rom": "'+rom(info)+'",'
                                    tx = ""
                                    rx = ""
                                    if sent < 1000:
                                        tx = '{0}KB/s'.format("%.2f"%sent)
                                    else:
                                        sent = sent / 1024
                                        tx = '{0}MB/s'.format("%.2f"%sent)
                                    if recv < 1000:
                                        rx = '{0}KB/s'.format("%.2f"%recv)
                                    else:
                                        recv = recv / 1024
                                        rx = '{0}MB/s'.format("%.2f"%recv)
                                    res += '"tx": "'+tx+'",'
                                    res += '"rx": "'+rx+'"'
                                    res += '}'
                                else:
                                    url = "http://" + ii[7] + ":8889/assets/info"
                                    sh = imp.load_source("server/main/httpclient","server/main/httpclient.py")
                                    #cat,cdata = sh.Client(ii[7],int(ii[19]),"/assets/info")
                                    cat,cdata = sh.Client(ii[7],int(ii[19]),'/login/dev','')
                                    if cat == "200":
                                        try:
                                            #response = urllib.request.urlopen(url, timeout=1)
                                            #html = response.read().decode('utf-8')         # 获取到页面的源代码
                                            #html = sh.Client("pi.lan",8889,"/assets/info")
                                            res += '"api": "1",'
                                            data = cdata.decode("utf-8").split('"')
                                            res += '"safe": "'+data[3]+'",'
                                            res += '"cpu": "'+data[7]+'",'
                                            res += '"ram": "'+data[11]+'",'
                                            res += '"rom": "'+data[15]+'",'
                                            res += '"tx": "'+data[19]+'",'
                                            res += '"rx": "'+data[23]+'"'
                                            res += '}'
                                        except:
                                            res += '"api": "0",'
                                            res += '"safe": "--",'
                                            res += '"cpu": "--",'
                                            res += '"ram": "--",'
                                            res += '"rom": "--",'
                                            res += '"tx": "--KB/s",'
                                            res += '"rx": "--KB/s"'
                                            res += '}'
                                    elif cat =="401":
                                        res += '"api": "3",'
                                        res += '"safe": "--",'
                                        res += '"cpu": "--",'
                                        res += '"ram": "--",'
                                        res += '"rom": "--",'
                                        res += '"tx": "--KB/s",'
                                        res += '"rx": "--KB/s"'
                                        res += '}'
                                    else:
                                        data = os.popen('ping ' + ii[7] + ' -c 1 | grep icmp_seq').read()
                                        if len(data.split('icmp_seq=1 ttl=64')) == 2:
                                            res += '"api": "2",'
                                            res += '"safe": "--",'
                                            res += '"cpu": "--",'
                                            res += '"ram": "--",'
                                            res += '"rom": "--",'
                                            res += '"tx": "--KB/s",'
                                            res += '"rx": "--KB/s"'
                                            res += '}'
                                        else:
                                            res += '"api": "0",'
                                            res += '"safe": "--",'
                                            res += '"cpu": "--",'
                                            res += '"ram": "--",'
                                            res += '"rom": "--",'
                                            res += '"tx": "--KB/s",'
                                            res += '"rx": "--KB/s"'
                                            res += '}'
                            res += ']'
                            res += '}'
                            httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)
                        else:
                            if os.path.isdir('.config') == False:
                                os.mkdir('.config')
                            if os.path.isdir('.config/main') == False:
                                os.mkdir('.config/main')
                            fs = open(".config/main/lits.json", "a")
                            data = '{"name":"'+"127.0.0.1"+'","host":"'+"127.0.0.1"+'"}' + '\n'
                            fs.write(data)
                            fs.close()
                    else:
                        my_file = "./server" + RUL + "/api.py"
                        if os.path.isfile(my_file):
                            if post_data == b'':
                                post = RUL_CS.split('&')
                            else:
                                rul_ = post_data.decode("utf-8").split('%')
                                post_data = b''
                                for y in range(len(rul_)):
                                    if y == 0:
                                        post_data = rul_[y].encode("utf-8")
                                    elif y == (len(rul_)+1):
                                        y=y 
                                    else:
                                        hex = rul_[y][:2]
                                        charb = bytes.fromhex(hex)
                                        post_data = post_data + charb
                                        if len(rul_[y]) > 2:
                                            post_data = post_data + rul_[y][2:].encode("utf-8")
                                #RUL_CS = RUL_CS.decode("utf-8")
                                post = post_data.decode("utf-8").split('&')
                                
                            sh = imp.load_source(RUL + "/api.py",my_file)
                            sh.main(new_client_socket,post,Headers,info,user)
                        else:
                            strr = {}
                            strr["err"] = '404'
                            sh = imp.load_source("server/main/php.py","server/main/php.py")
                            data = sh.php(new_client_socket,"post","/404.php",user,Headers,info,strr)
                            httpserver.httppostchar(new_client_socket,"404",data.encode("utf-8"),"text/html;charset=UTF-8",Headers,info)
                            #res = "HTTP/1.1 404 OK \r\n"
    except Exception as e:
        strr = {}
        strr["err"] = traceback.format_exc()  
        logsprnt("ERROR",info,traceback.format_exc())
        sh = imp.load_source("server/main/php.py","server/main/php.py")
        data = sh.php(new_client_socket,"post","/500.php",user,Headers,info,strr)
        httpserver.httppostchar(new_client_socket,"500",data.encode("utf-8"),"text/html;charset=UTF-8",Headers,info)
        
    if exre == 'reset':
        return -9
    if exre == 'exit':
        return -2
    return 0

def shutdown(data):
    global exre
    exre = data
    logsprnt("info","info",data)

def logsprnts(live,info,data):
    import threading
    lock = threading.Lock()
    lock.acquire()
    #if len(sys.argv) == 5:
    #    if sys.argv[1] == "hass":
    #        os.system("bashio::log." + live + " " + data.decode("utf-8"))
    #    else:
    #        print(live,end=' ')
    #        print(data,end='\r')
    #else:
    try:
        if data[-2:] == b'\r\n':
            data = data[:-2]
    except Exception as e:
        print()
    if live == "info":
        if os.path.exists("info.sh"):
            try:
                os.system("./info.sh '" + data.decode("utf-8") + "'")
            except Exception as e:
                print()

        print("\033[32m " + live,end=' ')
        print(data,end='')
        print('\033[0m')
    else:
        if os.path.exists("error.sh"):
            try:
                os.system("./error.sh '" + data.decode("utf-8") + "'")
            except Exception as e:
                print()
        print(live,end=' ')
        print(data,end='')
        print('')
    lock.release()
def logsprnt(live,info,data):
    t = threading.Thread(target=logsprnts, args=(live,info,data))
    t.start()

def main(info):
    global sent_before
    global recv_before
    global ttime
    global session_
    global exre
    global res

    exre = ''

    print("boot")
    fs = open("./server/server.ini", "rb")
    pat = fs.read().decode("utf-8")
    path = pat.split('\n')
    for p in path:
        p = "server/" + p.split("\r")[0]
        if os.path.isdir(p):
            if os.path.isfile(p + "/boot.py"):
                print(p)
                sh = imp.load_source(p + "/boot.py",p + "/boot.py")
                sh.boot(info)
    sent_before = psutil.net_io_counters().bytes_sent # 已发送的流量 
    recv_before = psutil.net_io_counters().bytes_recv # 已接收的流量 
    ttime = time.time()

    port = info["port"]
    python = info["python"]
    OS = info["OS"]
    dir = info["dir"]
    Versino = info["Versino"]

    fs = open(".config/sessino","rb")
    session__ = fs.read().decode("utf-8").split('\r\n')
    session_ = ''
    for p in session__:
        session_ += p + '\n'
    fs.close()

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a = 1
    while a < 10:
        try:
            tcp_server_socket.bind(("", port))
            a = 16
        except Exception as e:
            print(e.args)
            time.sleep(1)
    tcp_server_socket.listen(100)
    tcp_server_socket_run = tcp_server_socket
    if os.path.exists(".config/ssl/site.key"):
        try:
            import ssl
            tcp_server_socket_ssl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_server_socket_ssl = ssl.wrap_socket(tcp_server_socket_ssl,keyfile='.config/ssl/site.key',certfile='.config/ssl/site.crt')
            tcp_server_socket_ssl.bind(("localhost",0))
            ssl_port = tcp_server_socket_ssl.getsockname()
            tcp_server_socket_ssl.listen(100)
            tcp_server_socket_run = tcp_server_socket_ssl
            #t = threading.Thread(target=tcptossl, args=(tcp_server_socket,ssl_port))
            #t.start()
            #tcptossl(tcp_server_socket,ssl_port)
        except Exception as e:
            print(e.args)
            time.sleep(1)
            tcp_server_socket_run = tcp_server_socket
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    res = httpserver.server(tcp_server_socket_run,info,logsprnt,httpserver_void)
    if res == -9:
        tcp_server_socket.close()
        run = imp.load_source('run',"server/run.py")
        run.main(info)