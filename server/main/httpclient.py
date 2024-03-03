# coding=utf-8
#!/bin/python

import os
import sys
import time
import imp
import hashlib
import binascii
import socket


# 加密
def enctry(k,s):
    #k =  'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
    encry_str = ""
    for i,j in zip(s,k):
        # i为字符，j为秘钥字符
        temp = str(ord(i)+ord(j))+'_' # 加密字符 = 字符的Unicode码 + 秘钥的Unicode码
        encry_str = encry_str + temp
    return encry_str

def dectry(k,p):
    #k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
    dec_str = ""
    for i,j in zip(p.split("_")[:-1],k):
        # i 为加密字符，j为秘钥字符
        ttemp = ord(j)
        temp = int(i)
        temp = temp - ttemp
        temp = chr(temp) # 解密字符 = (加密Unicode码字符 - 秘钥字符的Unicode码)的单字节字符
        dec_str = dec_str+temp
    return dec_str

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
            if c.split('\t')[0] == ip:
                fsdata = fsdata + 'Cookie: ' + c.split('\t')[2] + '\r\n'
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
                return "502",e.args[-1].encode("utf-8")
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
                    fs.write(b'\t')
                    fs.write(str(dk).encode('utf-8'))
                    fs.write(b'\t')
                    fs.write(hhhh[0])
                    fs.write(b'\n')
                    fs.close()
                    #print(hhh)
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
    return "502","502".encode("utf-8")

def Clientchar(ip,dk,dir,post):
    try:
        if dk == "":
            dk = 80
        socket.setdefaulttimeout(5)
        client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
        #client.connect(('openwrt.lan',80))
        fsdata = 'POST ' + dir + ' HTTP/1.1\r\n'
        if post == b'':
            fsdata = 'GET ' + dir + ' HTTP/1.1\r\n'
        fsdata = fsdata + 'Host: ' + ip + ':' + str(dk) + '\r\n'
        fs = open(".config/main/cookie","rb")
        for c in fs.read().decode("utf-8").split('\n'):
            if c.split('\t')[0] == ip:
                fsdata = fsdata + 'Cookie: ' + c.split('\t')[2] + '\r\n'
        client.connect((ip,dk))
        client.send((fsdata + '\r\n').encode("utf-8") + post)
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
                    fs.write(b'\t')
                    fs.write(str(dk).encode('utf-8'))
                    fs.write(b'\t')
                    fs.write(hhhh[0])
                    fs.write(b'\n')
                    fs.close()
                    print(hhh)
            ma = data[len(b'HTTP/1.1 '):len(b'HTTP/1.1 ') + 3].decode('utf-8')
            dat = data[len(data.split(b'\r\n\r\n')[0]) + 4:]
            jvav = '6'
            h = data.split(b'\r\n\r\n')[0].split(b'\r\n')
            for i in h:
                i = i.split(b':')
                if i[0] == b'Content-Type':
                    jvav = i[1]
            return ma,dat,jvav.decode('utf-8')
        if data[:len(b'HTTP/1.1 ')] == b'HTTP/1.1 ':
            ma = data[len(b'HTTP/1.1 '):len(b'HTTP/1.1 ') + 3].decode('utf-8')
            dat = data[len(data.split(b'\r\n\r\n')[0]) + 4:]
            jvav = '6'
            h = data.split(b'\r\n\r\n')[0].split(b'\r\n')
            for i in h:
                i = i.split(b':')
                if i[0] == b'Content-Type':
                    jvav = i[1]
            return ma,dat,jvav.decode('utf-8')
    except Exception as e:
        #print(e.args)
        return "500",e.args[-1].encode("utf-8"),'text/html'
    socket.setdefaulttimeout(0)
    return "502",b"502",'text/html'

def logindev(devname):
    fs = open(".config/main/lits.json", "rb")
    hosts = fs.read().decode("utf-8").split('\n')
    for i in range(len(hosts)-1):
        ii = hosts[i].split('"')
        if ii[3] == devname:
            dd = ''
            a = ii[11]
            b = ii[15]
            b = dectry(ii[3],b)
            a = enctry("djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd",enctry(time.strftime(" %Y-%m-%d %H:%M ", time.localtime()),a))
            b = enctry("djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd",enctry(time.strftime(" %Y-%m-%d %H:%M ", time.localtime()),b))
            cdata = Client(ii[7],int(ii[19]),'/login/dev','a=' + a + '&b=' + b)
            return cdata