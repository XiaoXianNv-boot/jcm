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
