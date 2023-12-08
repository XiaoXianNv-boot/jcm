# coding=utf-8
#!/bin/python

import socket
import os
import imp
import hashlib

def main(new_client_socket,post,Headers,info,user):
    if len(post) == 3:
        link = ''
        sw = ''
        data = ''
        res = ''
        httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
        XIngressPath = httpserver.catHeaders("X-Ingress-Path",Headers)
        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'link':
                link = tmp[1]
            if tmp[0] == 'sw':
                sw = tmp[1]
            if tmp[0] == 'data':
                data = tmp[1]
        #sw = sw + '?link=' + link + '&data=' + data
        sw = XIngressPath + sw
        #print(Headers)
        cd = os.stat("web/Ace_Admin/main/ttytou.html").st_size
        cd += os.stat("web/Ace_Admin/main/ttywei.html").st_size
        cd += len(sw)
        he = info["Headers"]
        he += "Connection: close\r\n"
        he += "Accept-Ranges: bytes\r\n"
        he = he + 'Content-Length:' + str(cd) + "\r\n"
        he += "Content-Type: " + "text/html" + "\r\n"
        he = he + '\r\n'
        he = "HTTP/1.1 " + "200" + " OK \r\n" + he
        new_client_socket.send(he.encode("utf-8"))
        with open("web/Ace_Admin/main/ttytou.html", 'rb') as fp:
            while True:
                data = fp.read(4096)
                if not data:
                    break
                new_client_socket.send(data)

        new_client_socket.send(sw.encode("utf-8"))
        with open("web/Ace_Admin/main/ttywei.html", 'rb') as fp:
            while True:
                data = fp.read(4096)
                if not data:
                    break
                new_client_socket.send(data)

    else:
        he = info["Headers"]
        he += "Connection: close\r\n"
        he += "Accept-Ranges: bytes\r\n"
        he = he + 'Content-Length:' + str(len('{"login":Falsh}')) + "\r\n"
        he += "Content-Type: " + "application/json" + "\r\n"
        he = he + '\r\n'
        he = "HTTP/1.1 " + "200" + " OK \r\n" + he
        new_client_socket.send(he.encode("utf-8"))
        new_client_socket.send(b'{"login":Falsh}')
