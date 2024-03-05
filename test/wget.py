# coding=utf-8
#!/bin/python

#http 客户端测试

import os
import socket
import ssl

def prinout(new_client_socket,data):
    print(data,end="")

def start(data,lens,lenmax,new_client_socket,datas,hasattr):
    for d in hasattr:
        print(d)
    print("[" + str(lens) + " / " + str(lenmax) + "]\r",end="")
    return datas
def loop(data,lens,lenmax,new_client_socket,datas):
    print("[" + str(lens) + " / " + str(lenmax) + "]\r",end="")
    return datas

def wget(rul,new_client_socket,file,datas,start,loop,stop):
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

    socket.setdefaulttimeout(10)
    client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象

    if ruldir[0] == "https://":
        client = ssl.wrap_socket(client,cert_reqs=ssl.CERT_REQUIRED,ca_certs='server/main/DigiCert Global Root CA.crt')
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
    if os.path.exists(".config/main/cookie"):
        fs = open(".config/main/cookie","rb")
        for c in fs.read().decode("utf-8").split('\n'):
            if c.split(':')[0] == host:
                fsdata = fsdata + 'Cookie: ' + c.split(':')[1] + '\r\n'

    client.connect((host,port))
    client.send((fsdata + '\r\n').encode("utf-8"))
    data = b''

    lens = 0     #已经下载长度
    lenmax = -1  #总长度
    run = 0
    hasattr = ""
    fs = ''
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
    return hasattr,data
    hasattr = data.split(b'\r\n\r\n')
    hasattr = hasattr[0]
    hasattr = hasattr.split(b'\r\n')
    if len(data.split(b'\r\n\r\n')) > 1:
        for ddd in hasattr:
            dddd = ddd.split(b': ')
            if dddd[0] == b'Content-Length':
                lenmax = int(dddd[1])
    lens = len(data[len(data.split(b'\r\n\r\n')[0])+4:])
    data = data[len(data.split(b'\r\n\r\n')[0])+4:]
    datas = start(data,lens,lenmax,new_client_socket,datas,hasattr)
    fs = ''
    if hasattr[0].split(b" ")[1] == b"200":
        if file != '':
            fs = open(file,'wb')
            fs.write(data)
            




rul = "https://github.com/XiaoXianNv-boot/jcm/releases/download/pkg/frpc_V0.2.pkg"
print(rul)
hasattr,data = wget(rul,
    "",
    "tmp.tar.gz",
    "",
    start,loop)
if hasattr[0].split(b" ")[1] == b"302":
    for d in hasattr:
        dd = d.split(b': ')
        if dd[0] == b'Location':
            rul = d[len(dd[0] + b": "):].decode("utf-8")
    print(rul)
    hasattr,data = wget(rul,
    "",
    "tmp.tar.gz",
    "",
    start,loop)

