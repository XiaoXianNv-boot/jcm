# coding=utf-8
#!/bin/python

import os
import sys
import time
import imp
import hashlib
import binascii
import socket

def Client(ip,dk,dir,post):
    try:
        if dk == "":
            dk = 80
        socket.setdefaulttimeout(1)
        client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
        #client.connect(('openwrt.lan',80))
        fsdata = 'POST ' + dir + ' HTTP/1.1\r\n'
        fsdata = fsdata + 'Host: ' + ip + ':' + str(dk) + '\r\n'
        fs = open(".config/main/cookie","rb")
        for c in fs.read().decode("utf-8").split('\n'):
            if c.split(':')[0] == ip:
                fsdata = fsdata + 'Cookie: ' + c.split(':')[1] + '\r\n'
        client.connect((ip,dk))
        client.send((fsdata + '\r\n' + post).encode("utf-8"))
        data = b''
        run = 0
        d = ''
        while run == 0:
            try:
                d = client.recv(1024)
            except Exception as e:
                #print(e.args)
                #if len(d) != 1024:
                #    run = 1
                if data == b'':
                    data = b"404\r\n\r\n404"
                else:
                    run = 1
                    if e.args[0] == 'timed out':
                        d = False
                #break
            if d:
                data = data + d
                if dir == '/assets/info':
                    if data[-1] == '}':
                        run = 1
            else:
                run = 1
        #print(data)
        client.close()
        if data[:len(b'HTTP/1.1 200')] == b'HTTP/1.1 200':
            catdatah = data.split(b'\r\n\r\n')[0].split(b'\r\n')
            for hh in catdatah[1:]:
                hhh = hh.split(b': ')
                if hhh[0] == b'set-Cookie':
                    hhhh = hhh[1].split(b';')
                    fs = open(".config/main/cookie","ab")
                    fs.write(ip.encode('utf-8'))
                    fs.write(b':')
                    fs.write(hhhh[0])
                    fs.write(b'\n')
                    fs.close()
                    print(hhh)
            datad = b''
            for ddd in data.split(b'\r\n\r\n')[1:]:
                datad = datad + b'\r\n\r\n' + ddd
            return '200',datad[4:]
        if data[:len(b'HTTP/1.1 ')] == b'HTTP/1.1 ':
            return data[len(b'HTTP/1.1 '):len(b'HTTP/1.1 ') + 3].decode('utf-8'),data[len(b'HTTP/1.1 '):len(b'HTTP/1.1 ') + 3]
    except Exception as e:
        #print(e.args)
        return "404",e.args[-1].encode("utf-8")
    socket.setdefaulttimeout(0)

def main(new_client_socket,post,Headers,info,user):
    res = ''
    devname = ''
    devrul = ''
    devuser = ''
    devpassword = ''
    devport = ''
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'devname':
            devname = tmp[1]
        if tmp[0] == 'devrul':
            devrul = tmp[1]
        if tmp[0] == 'devuser':
            devuser = tmp[1]
        if tmp[0] == 'devpassword':
            devpassword = tmp[1]
        if tmp[0] == 'devport':
            devport = tmp[1]
    

    obj = hashlib.md5()
    md = devuser
    md += time.strftime("I %Y-%m-%d %H:%M ", time.localtime())
    obj.update((md).encode('utf-8'))
    a = obj.hexdigest()
    if info['debug']:
        print(md)
        print(a)
    obj = hashlib.md5()
    md = binascii.hexlify(hashlib.pbkdf2_hmac("sha256",devpassword.encode("utf-8"),b"jcm",1000)).decode()
    md += time.strftime("I %Y-%m-%d %H:%M ", time.localtime())
    obj.update((md).encode('utf-8'))
    b = obj.hexdigest()
    if info['debug']:
        print(md)
        print(b)
    cat,cdata = Client(devrul,int(devport),'/login/dev','a=' + a + '&b=' + b)
    if cat == '200':
        cdata = cdata.decode('utf-8')
    elif cat == '404':
        data = os.popen('ping ' + devrul + ' -c 1 | grep icmp_seq').read()
        if len(data.split('icmp_seq=1 ttl=64')) == 2:
            cdata = '{"name": "'
            cdata += devname
            cdata +=  '","host": "'
            cdata += devrul
            cdata += '","user": "'
            cdata += devuser
            cdata +=  '","password": "'
            cdata += binascii.hexlify(hashlib.pbkdf2_hmac("sha256",devpassword.encode("utf-8"),b"jcm",1000)).decode()
            cdata += '","port": "'
            cdata += devport
            cdata += '"},\n'
            fs = open(".config/main/lits.json","ab")
            fs.write(cdata.encode("utf-8"))
            fs.close()
            res += "{\"data\":\"添加成功\"}"
        else:
            if cdata == b'getaddrinfo failed':
                res += "{\"data\":\"找不到主机\"}"
            elif cdata == b'timed out':
                res += "{\"data\":\"连接超时\"}"
            else:
                res += "{\"data\":\"" + cdata + "\"}"
    else:
        if cdata == b'getaddrinfo failed':
            res += "{\"data\":\"找不到主机\"}"
        elif cdata == b'timed out':
            res += "{\"data\":\"连接超时\"}"
        else:
            res += "{\"data\":\"" + cdata.decode("utf-8") + "\"}"
    
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)