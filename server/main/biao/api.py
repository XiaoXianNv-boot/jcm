
# coding=utf-8
#!/bin/python

import os
import sys
import time
import imp
import hashlib
import socket

def main(new_client_socket,post,Headers,info,user):
    link = ''
    path = ''
    res = ''
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'link':
            link = tmp[1]
        if tmp[0] == 'path':
            path = tmp[1]
    fs = open(".config/main/lits.json", "rb")
    hosts = fs.read().decode("utf-8").split('\n')
    
    res += '{"data":[ \r\n'
    for i in range(len(hosts)-1):
        ii = hosts[i].split('"')
        if i== 0:
            res += '{"name":"' + ii[3] + '","data": [ \r\n'
        else:
            res += ',{"name":"' + ii[3] + '","data": [ \r\n'
        if ii[7] == "127.0.0.1":
            fs = open("./server/server.ini", "rb")
            pat = fs.read().decode("utf-8")
            path = pat.split('\n')
            biao = ''
            fo = 0
            for p in path:
                p = "server/" + p.split('\r')[0]
                #print(p)
                if os.path.isdir(p):
                    if os.path.isfile(p + "/biao.json"):
                        fs = open(p + "/biao.json", "rb")
                        fo += 1
                        bbt = fs.read().decode("utf-8")
                        bb = bbt.split('\"')
                        biao = biao + bbt + ","
            res += biao + '{}]} \r\n'
        else:
            url = "http://" + ii[7] + ":" + ii[19] + "/main/biao/dev"
            sh = imp.load_source("server/main/httpclient","server/main/httpclient.py")
            #cat,cdata = sh.Client(ii[7],int(ii[19]),"/main/biao/dev")
            cat,cdata = sh.Client(ii[7],int(ii[19]),'/main/biao/dev','')
            if cdata == b'Connection refused':
                res += '{\n    "name":"Connection refused",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
            else:
                if cat == "404":
                    res += '{\n    "name":"404",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                elif cat == "502":
                    res += '{\n    "name":"无响应",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                elif cat == '401':

                    obj = hashlib.md5()
                    md = ii[11]
                    md += time.strftime("I %Y-%m-%d %H:%M ", time.localtime())
                    obj.update((md).encode('utf-8'))
                    a = obj.hexdigest()
                    if info['debug']:
                        print(md)
                        print(a)
                    obj = hashlib.md5()
                    md = ii[15]
                    md += time.strftime("I %Y-%m-%d %H:%M ", time.localtime())
                    obj.update((md).encode('utf-8'))
                    b = obj.hexdigest()
                    if info['debug']:
                        print(md)
                        print(b)
                    cat,cdata = sh.Client(ii[7],int(ii[19]),'/login/dev','a=' + a + '&b=' + b)
                    if cat == '200':
                        cdata = cdata.decode("utf-8")
                        if cdata == '{"data":"login"}\r\n\r\n':
                            cat,cdata = sh.Client(ii[7],int(ii[19]),"/main/biao/dev")
                            if cat == "404":
                                res += '{\n    "name":"404",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                            elif cat == '502':
                                res += '{\n    "name":"无响应",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                            elif cat == '401':
                                res += '{\n    "name":"登录失败",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                            elif cdata == '<!DOCTYPE html>':
                                res += '{\n    "name":"响应错误",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                            else:
                                cdata = cdata.decode("utf-8")[9:]
                                res += cdata
                                res += '{}]} \r\n'
                        else:
                            cdata = cdata.split('":"')
                            cdata = cdata[1].split('","')
                    else:
                        if cat == "404":
                            res += '{\n    "name":"404",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                        elif cat == '502':
                            res += '{\n    "name":"无响应",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                        elif cat == '401':
                            res += '{\n    "name":"登录失败",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                        elif cdata == '<!DOCTYPE html>':
                            res += '{\n    "name":"响应错误",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                        else:
                            cdata = cdata.decode("utf-8")[9:]
                            res += cdata
                            res += '{}]} \r\n'
                elif cdata == '<!DOCTYPE html>':
                    res += '{\n    "name":"响应错误",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n'
                else:
                    cdata = cdata.decode("utf-8")[9:]
                    res += cdata
                    res += '{}]} \r\n'
                    #new_client_socket.send('{\n    "name":"无响应",\n    "link":"",\n    "fa":"fa-tachometer"\n},' + '{}]} \r\n').encode("utf-8"))
    res +=  ']} \r\n'
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)