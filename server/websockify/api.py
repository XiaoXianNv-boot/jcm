import os
import sys
import imp
import socket
import multiprocessing 

def jscswebsock(data):
    if len(data) > 4:
        try:
            i = 0
            FIN = data[i] & 128 >> 7
            RSV = data[i] & 112 >> 5
            Opcode = data[i] & 15 >> 0
            if len(data) == 0:
                Opcode = 0
            i += 1
            Mask = data[i] & 128
            datalength = data[i] & 127 >> 0
            Maskingkey = ''
            datas = b''
            if Mask > 1:
                i += 1
                Maskingkey = data[i:i+4]
            lens = len(data)
            ifdata = datalength + i + 4
            if lens >= ifdata:
                return True,ifdata
            return True,i
        except:
            return False,0
    else:
        return False,0
    data = data
def cswebsock(data):
    if len(data) > 3:
        lens = data[0]
        ifdata = bytes.fromhex('82')[0]
        if lens == ifdata:
            lens = data[1]
            ifdata = len(data) - 2
            if lens <= ifdata:
                return True,lens + 2
    else:
        return False,0
    data = data

def mw(sock,uinx):
    data = b''
    while True:
        data = sock.recv(102400)
        if data:
            #boot,int = jscswebsock(data)
            #while boot:
            uinx.send(data)
            #data = data[int:]
                #boot,int = jscswebsock(data)
        else:
            uinx.close()
            sock.close()
            break
def wm(uinx,sock):
    data = b''
    while True:
        data = uinx.recv(102400)
        if data:
            #boot,int = cswebsock(data)
            #while boot:
            sock.send(data)
            #data = b""#data[int:]
                #boot,int = cswebsock(data)
        else:
            uinx.close()
            sock.close()
            break

def main(data):
    new_client_socket = data["new_client_socket"]
    RUL_CS            = data["RUL_CS"]
    post_data         = data["post_data"]
    Headers           = data["Headers"]
    info              = data["info"]
    user              = data["user"]

    post = RUL_CS
    token = ""
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'token':
            token = tmp[1]

    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    #httpserver.websockinit(new_client_socket,Headers,info)
    #httpserver.websockfs()
    s = socket.socket(family=socket.AF_UNIX,type=socket.SOCK_STREAM)
    s.connect("/run/jcm/qemu/vnc.sock")
    data = "GET /websockify?token=" + token + " HTTP/1.1\r\n"
    s.send(data.encode("utf-8"))
    for h in Headers[1:]:
        s.send(h.encode("utf-8") + b'\r\n')
    s.send(b'\r\n')
    data = s.recv(102400)
    datas = data.split(b'\r\n\r\n')
    while len(datas) < 2:
        data += s.recv(102400)
        datas = data.split(b'\r\n\r\n')
    for d in datas[0].split(b"\r\n"):
        new_client_socket.send(d)
        new_client_socket.send(b"\r\n")
    new_client_socket.send(b"Connection: close")
    new_client_socket.send(b"\r\n")
    new_client_socket.send(b"\r\n")
    datas = data[len(datas[0]) + 4:]
    boot,int = cswebsock(datas)
    while not boot:
        datas += s.recv(102400)
        boot,int = cswebsock(datas)
    new_client_socket.send(datas[:int])
    datas = datas[int:]
    p1 = multiprocessing.Process(target=mw,args=(new_client_socket,s))
    p2 = multiprocessing.Process(target=wm,args=(s,new_client_socket))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
