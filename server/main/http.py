# coding=utf-8
#!/bin/python

import socket
import os
import imp
import hashlib

'''
通用头
z 状态码
'''
def hea(Headers,Versino,h,z):
    res = "HTTP/1.1 " + z + " OK \r\n"
    res = res + "Server: JCM/" + Versino + "\r\n"
    res = res + "Connection: close\r\n"
    res = res + "Accept-Ranges: bytes\r\n"
    return res + h


def file(new_client_socket,post,Versino,RUL,user,Headers,info):
    byt = "",""
    filedir = "./web/" + info["theme"] + RUL
    if RUL == "/favicon.ico":
        RUL = "./web" + RUL
    elif os.path.isfile(filedir):
        RUL = filedir
    else:
        filedir = "./web/" + "Ace_Admin" + RUL
        if os.path.isfile(filedir):
            RUL = filedir
    fsdd = open(RUL, "rb")
    size = os.stat(RUL)
    for i in Headers:
        ii = i.split(":")
        if ii[0] == "Range":
            iii = ii[1].split("=")
            if iii[0] == ' bytes':
                iiii = iii[1].split('-')
                byt = iiii
    if byt[0] == '':
        if RUL == "./web/" + info["theme"] + "/login.html":
            if RUL[:len("./web/" + info["theme"] + "/assets")] == "./web/" + info["theme"] + "/assets":
                sstr = hea(Headers,Versino,"","200").encode("utf-8")
            else:
                sstr = hea(Headers,Versino,"","401").encode("utf-8")
        else:
            sstr = hea(Headers,Versino,"","200").encode("utf-8")
        sstr = sstr + ("Content-Range: bytes 0-" + str(size.st_size) + "/" + str(size.st_size) + "\r\n").encode("utf-8")
        sstr = sstr + "Content-Length:".encode("utf-8") + str(size.st_size).encode("utf-8") + "\r\n".encode("utf-8")
        new_client_socket.send(sstr)
        sstr = b''
    elif byt[0] == "0":
        sstr = hea(Headers,Versino,"","206").encode("utf-8")
        sstr = sstr + ("Content-Range: bytes 0-" + str(size.st_size) + "/" + str(size.st_size) + "\r\n").encode("utf-8")
        sstr = sstr + "Content-Length:".encode("utf-8") + str(size.st_size).encode("utf-8") + "\r\n".encode("utf-8")
        new_client_socket.send(sstr)
        sstr = b''
    else:
        file_md5 = ""
        with open(RUL, 'rb') as fp:
            file_md5= hashlib.md5(fp.read()).hexdigest()
        sstr = "ETag: \"" + file_md5 + "\"\r\n".encode("utf-8")
        sstr = hea(Headers,Versino,str,"206").encode("utf-8")
        if byt[1] == "":
            sstr = sstr + "Content-Length:".encode("utf-8") + str(size.st_size - int(byt[0])).encode("utf-8") + "\r\n".encode("utf-8")
            sstr = sstr + ("Content-Range: bytes " + byt[0] + "-" + str(size.st_size) + "/" + str(size.st_size) + "\r\n").encode("utf-8")
        else:
            sstr = sstr + "Content-Length:".encode("utf-8") + str(int(byt[1]) - int(byt[0]) - 1).encode("utf-8") + "\r\n".encode("utf-8")
            sstr = sstr + ("Content-Range: bytes " + byt[0] + "-" + byt[1] + "/" + str(size.st_size) + "\r\n").encode("utf-8")
        new_client_socket.send(sstr)
        sstr = b''
    tmp2 = RUL.split(".")
    res = ""
    if tmp2[-1] == 'htm':
        res = res + "Content-Type: text/html;charset=UTF-8\r\n"
    elif tmp2[-1] == 'html':
        res = res + "Content-Type: text/html;charset=UTF-8\r\n"
    elif tmp2[-1] == 'css':
        res = res + "Cache-Control: public, max-age=31536000\r\n"
        res = res + "Content-Type: text/css;charset=UTF-8\r\n"
    elif tmp2[-1] == 'js':
        res = res + "Cache-Control: public\r\n"
        res = res + "Content-Type: application/javascript;charset=UTF-8\r\n"
    elif tmp2[-1] == 'svg':
        res = res + "Cache-Control: public, max-age=31536000\r\n"
        res = res + "Content-Type: image/svg+xml\r\n"
    elif tmp2[-1] == 'woff2':
        res = res + "Cache-Control: public, max-age=31536000\r\n"
        res = res + "Content-Type: font/woff2\r\n"
    else:
        res = res + "Content-Type: text/plain;charset=UTF-8\r\n"
    sstr = sstr + res.encode("utf-8")
    fsdd = open(RUL, "rb")
    new_client_socket.send(sstr)
    fsd = fsdd.read()
    new_client_socket.send("\r\n".encode("utf-8"))
    fsdd.close()
    for dd in range(0,len(fsd),4096):
        new_client_socket.send(fsd[dd:dd+4096])

def textpost(new_client_socket,Versino,text,z,type):
    sstr = ''
    text = text.encode("utf-8")
    cd = str(len(text))
    sstr = hea("",Versino,type,z).encode("utf-8")
    sstr = sstr + b'\r\nContent-Length:' + cd.encode("utf-8")
    sstr = sstr + b'\r\n\r\n'
    new_client_socket.send(sstr)
    new_client_socket.send(text)

def setsession_(session_,w):
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
    return session_,data

def catsession_(session_,w):
    print("No Edit")
    return session_,data