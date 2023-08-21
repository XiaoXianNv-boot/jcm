
# coding=utf-8
#!/bin/python

import imp
import threading
import socket
import os
import time
import sys
import traceback

import psutil
import random

run_ = 0
exit = ''

def httplink(new_client_socket,RUL,RUL_CS,post_data,user,Headers,info):
    global session_
    global a
    global Versino
    global run_
    global update
    global OS
    global ttime
    global sent_before
    global recv_before
    global exit

    if RUL == "/favicon.ico":
        sh = imp.load_source("server/main/http.py","server/main/http.py")
        if post_data == b'':
            post = RUL_CS.split('&')
        else:
                post = post_data.decode("utf-8").split('&')
        sh.file(new_client_socket,post,Versino,RUL,user,Headers,info)
    my_file = "./web/" + info["theme"] + RUL
    link = ''
    for i in RUL_CS.split('&'):
        tmp = i.split('=')
        if tmp[0] == 'link':
            link = tmp[1]
    if user != "no_login":
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
                sh = imp.load_source("server/main/http.py","server/main/http.py")
                if post_data == b'':
                    post = RUL_CS.split('&')
                else:
                       post = post_data.decode("utf-8").split('&')
                sh.php(new_client_socket,post,Versino,RUL,user,Headers,info)
            else:
                sh = imp.load_source("server/main/http.py","server/main/http.py")
                if post_data == b'':
                    post = RUL_CS.split('&')
                else:
                       post = post_data.decode("utf-8").split('&')
                sh.file(new_client_socket,post,Versino,RUL,user,Headers,info)
        else:
            if RUL == "/login":
                post = post_data.decode("utf-8").split('&')
    else:
        if RUL == "/login":
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
            ifuser = ""
            ifpass = ""
            tools = imp.load_source('tools',"Tools/Tools.py")
            text = ''
            type = "Content-Type: text/html;charset=UTF-8"
            if tools.ifuser(name,password) == "yes":
                text = '{"data":"login"}'
                cok = ""
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
                            fs__ = fs_.split(',')
                            session_ = session_ + fs_ + ("\n") 
                import datetime
                cookie_date = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%a, %d %b %Y %H:%M:%S GMT")
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
                    type = type + "\r\nset-Cookie: Cluster_management_Jiang=" + cok + "; SameSite=Lax; Expires=" + cookie_date + ""
                    fs_user = open(".config/sessino","a")
                    fs_user.write(cok + "," + name + "," + cookie_date + "\n")
                    fs_user.close()
                else:
                    type = type + "\r\nset-Cookie: Cluster_management_Jiang=" + cok + "; SameSite=Lax;"# Expires=" + cookie_date + "\r\n"
            else:
                text = '{"data":"用户名或密码错误"}'
            sh = imp.load_source("server/main/http.py","server/main/http.py")
            sh.textpost(new_client_socket,Versino,text,"200",type)
        else:
            RUL_ = "/login.html"
            if RUL[:len("/assets")] == "/assets":
                RUL_ = RUL
            sh = imp.load_source("server/main/http.py","server/main/http.py")
            if post_data == b'':
                post = RUL_CS.split('&')
            else:
                    post = post_data.decode("utf-8").split('&')
            sh.file(new_client_socket,post,Versino,RUL_,user,Headers,info)
def http_to_char(data):
    rul_ = data.split('%')
    for y in range(len(rul_)):
        if y == 0:
            data = rul_[y].encode("utf-8")
        elif y == (len(rul_)+1):
            y=y
        else:
            hex = rul_[y][:2]
            charb = bytes.fromhex(hex)
            data = data + charb
            if len(rul_[y]) > 2:
                data = data + rul_[y][2:].encode("utf-8")
    data = data.decode("utf-8")    
    return data

def tcplink(sock, addr, info):
    try:
        new_client_socket = sock
        client_addr = addr
        global session_
        global a
        global run_
        global update

        RUL = ''
        RUL_t = '' 
        HTTPMethod = ''

        user = "no_login"
        # 接收客户端发送过来的请求
        recv_tcp = new_client_socket.recv(8192)
        if recv_tcp:
            if recv_tcp == b'':
                #print(str(client_addr) + " ???")
                recv_tcp = new_client_socket.recv(8192)
                if recv_tcp == b'':
                    #print(str(client_addr) + " ???")
                    return
        else:
            return
        recv_data=""
        post_data=b''
        Headers = ''
        recv_data = recv_tcp.split(b'\r\n\r\n')
        haslen = len(recv_data[0]) + 4
        post_data = recv_tcp[haslen:]
        recv_data = recv_data[0].decode("utf-8")
        Headers = recv_data.split('\r\n')
        RUL = ''
        RUL_CS = ''
        RUL = Headers[0].split(' ')[1].split('?')[0].split('#')[0]
        RUL_CS = Headers[0].split(' ')
        RUL_CS = RUL_CS[1].split('?')
        if len(RUL_CS) == 1:
            RUL_CS = ''
        else:
            RUL_CS = http_to_char(RUL_CS[1])

        for h in Headers:
            tmp2 = h.split(' ')
            if tmp2[0] == "Cookie:":
                for x in range(0,len(tmp2)):
                    tmp3 = tmp2[x].split('=')
                    if(tmp3[0] == "Cluster_management_Jiang"):
                        tmp4 = session_.split('\n')
                        for y in range(len(tmp4)):
                            tmp5 = tmp4[y].split(',')
                            tmp3t = tmp3[1].split(';')
                            if tmp3t[0] == tmp5[0]:
                                user = tmp5[1]
        '''if "login" == "login":
            if user == "no_login":
                RUL_t = RUL
                tmp6 = RUL_t.split('/')   
                if tmp6[1] != "assets":
                    if len(tmp6) == 2:
                        RUL = '/login'
                    else:
                        RUL = '/login'
                if RUL_t == "/login/dev":
                    RUL = RUL_t'''
        pr = (time.strftime("I %Y-%m-%d %H:%M:%S ", time.localtime()).encode("utf-8"))
        pr += ((str(client_addr) + ' ' + user + ' ' + Headers[0].split(' ')[1]).encode("utf-8"))
        print(pr.decode("utf-8"))
        logs = open(".logs/run.py/" + time.strftime("%Y-%m-%d.log", time.localtime()),"ab")
        logs.write(time.strftime("I %Y-%m-%d %H:%M:%S ", time.localtime()).encode("utf-8"))
        logs.write((str(client_addr) + ' ' + user + ' ' + Headers[0].split(' ')[1]).encode("utf-8"))
        logs.write(b'\r\n')
        logs.close()
        if info['debug']:
            httplink(new_client_socket,RUL,RUL_CS,post_data,user,Headers,info)
        else:
            t = threading.Thread(target=httplink, args=(new_client_socket,RUL,RUL_CS,post_data,user,Headers,info))
            t.start()
    except Exception as e:
        pr = (time.strftime("E %Y-%m-%d %H:%M:%S ", time.localtime()).encode("utf-8"))
        pr += ((traceback.format_exc()).encode("utf-8"))
        print(pr.decode("utf-8"))
        logs = open(".logs/run.py/" + time.strftime("%Y-%m-%d.log", time.localtime()),"ab")
        logs.write(time.strftime("E %Y-%m-%d %H:%M:%S ", time.localtime()).encode("utf-8"))
        logs.write((traceback.format_exc()).encode("utf-8"))
        logs.write(b'\r\n')
        logs.close()
        #e500(new_client_socket,Versino,user,Headers,traceback.format_exc())
        time.sleep(1)

def tcptossltx(sock,tcp_server_socket):
    rin = 1
    while rin == 1:
        try:
            recv_tcp = sock.recv(8192)
            if recv_tcp:
                tcp_server_socket.send(recv_tcp)
            else:
                rin = 0
                print("txend")
                tcp_server_socket.close()
                sock.close()
            
        except Exception as e:
            rin = 0
            tcp_server_socket.close()
            sock.close()
            if len(e.args) > 1:
                if e.args[1] != "你的主机中的软件中止了一个已建立的连接。":
                    print(e.args)
            else:
                print(e.args)
def tcptosslrx(tcp_server_sockets,socks):
    rin = 1
    while rin == 1:
        try:
            recv_tcp = socks.recv(8192)
            if recv_tcp:
                tcp_server_sockets.send(recv_tcp)
            else:
                rin = 0
                print("rxend")
                socks.close()
                tcp_server_sockets.close()
            
        except Exception as e:
            rin = 0
            socks.close()
            tcp_server_sockets.close()
            if len(e.args) > 1:
                if e.args[1] != "远程主机强迫关闭了一个现有的连接。":
                    print(e.args)
            else:
                print(e.args)
def tcptossllink(tcp_server_socket,ssl_port,recv_tcp):
    rin = 1
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(ssl_port)
    sock.send(recv_tcp)
    tx = threading.Thread(target=tcptossltx, args=(sock,tcp_server_socket))
    tx.start()
    rx = threading.Thread(target=tcptosslrx, args=(sock,tcp_server_socket))
    rx.start()
    if tx.is_alive():
        tx.join()
    if rx.is_alive():
        rx.join()


def tcptossl(tcp_server_socket,ssl_port):
    while tcp_server_socket != '':
        try:
            sock, addr = tcp_server_socket.accept()
            sock.settimeout(60)
            recv_tcp = sock.recv(8192)
            if recv_tcp == b'':
                #print(str(client_addr) + " ???")
                recv_tcp = sock.recv(8192)
                if recv_tcp == b'':
                    #print(str(client_addr) + " ???")
                    sock.close()
            if recv_tcp != b'':
                if recv_tcp[:3] == b'GET':
                    res = b''
                    recv_tcp_buff = recv_tcp.split(b'\r\n')
                    host = recv_tcp.split(b'Host: ')[1].split(b'\r\n')[0]
                    res = res + ('HTTP/1.1 307 Temporary Redirect\r\n'.encode("utf-8"))
                    res = res + ('Location: https://'.encode("utf-8"))
                    res = res + (host)
                    res = res + (recv_tcp_buff[0].split(b' ')[1])
                    res = res + ('\r\n'.encode("utf-8"))
                    res = res + (("Server: JCM/" + Versino + "\r\n").encode("utf-8"))
                    res = res + ("Connection: close\r\n".encode("utf-8"))
                    res = res + ("Content-Length: 0\r\n".encode("utf-8"))
                    res = res + ('\r\n\r\n\r\n'.encode("utf-8"))

                    sock.send(res)
                    #sock.close()
                    #print()
                    recv_tcp = sock.recv(8192)
                    if recv_tcp == b'':
                        #print(str(client_addr) + " ???")
                        recv_tcp = sock.recv(8192)
                        if recv_tcp == b'':
                            #print(str(client_addr) + " ???")
                            sock.close()
                        else:
                            print("6")
                    else:
                        print("9")
                else:
                    t = threading.Thread(target=tcptossllink, args=(sock,ssl_port,recv_tcp))
                    t.start()
        except Exception as e:
            if e.args[0] != "timed out":
                print(e.args)

def main(info):
    global session_
    global a
    global run_
    global update
    global OS
    global ttime
    global sent_before
    global recv_before
    global Versino
    global exit

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
            t = threading.Thread(target=tcptossl, args=(tcp_server_socket,ssl_port))
            t.start()
            #tcptossl(tcp_server_socket,ssl_port)
        except Exception as e:
            print(e.args)
            time.sleep(1)
            tcp_server_socket_run = tcp_server_socket
    a = 1
    while a < 10:
        try:
            print("start")
            while run_ < 10:
                try:
                    sock, addr = tcp_server_socket_run.accept()
                    sock.settimeout(60)
                    tcplink(sock, addr , info)
                except Exception as e:
                    if run_ == 9:
                        run_ = 16
                    if e.args[0] != "timed out":
                        print(e.args)
        except Exception as e:
            print(e.args)
    sock.close()
    tcp_server_socket.close()
    if exit == "reboot":
        imp.load_source("server/init.py","server/init.py")
        #os.system("\"" + info["python"] + '\" server/init.py')
    sys.exit() 

if __name__ == "__main__":
    info = {}
    info["Versino"] = 'V0.0'
    info["python"] = sys.executable
    info["dir"] = os.getcwd()
    info["OS"] = OS_
    info["OS_name"] = OS
    info["port"] = 8888
    info['debug'] = False
    main(info)
