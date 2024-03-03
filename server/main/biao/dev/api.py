
# coding=utf-8
#!/bin/python

import os
import sys
import time
import imp
import hashlib
import socket

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    link = ''
    path = ''
    res = ''
    post = RUL_CS
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'link':
            link = tmp[1]
        if tmp[0] == 'path':
            path = tmp[1]
    fs = open(".config/main/lits.json", "rb")
    hosts = fs.read().decode("utf-8").split('\n')
    
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
    #res += biao + '{}]} \r\n'


    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)