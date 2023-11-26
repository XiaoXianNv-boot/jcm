
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
    res = '{}'
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'link':
            link = tmp[1]
        if tmp[0] == 'path':
            path = tmp[1]

    fo = 0
    data = {}
    void = {}
    names = {}
    nn = ""
    Depends = {}
    License = {}
    ruls = {}
    pkginme = {}

    yuan = os.listdir(".config/APP/data/")
    yuan.sort(reverse=True)
    for y in yuan:
        fs = open(".config/APP/data/" + y,'r')
        yrul = fs.read().split('\n')[1:-1]
        for i in yrul:
            i = i.split(',')
            name = i[0].split('"')[3]
            n = i[1].split('"')[3]
            d = i[7].split('"')[3]
            v = i[2].split('"')[3]
            de = i[3].split('"')[3]
            l = i[4].split('"')[3]
            r = i[5].split('"')[3]
            p = i[6].split('"')[3]
            try:
                void[name] = void[name] + "\t" + v
                pkginme[name + v] = p
            except Exception as e:
                data[name] = d
                void[name] = v
                names[name] = n
                nn += name + '\t'
                Depends[name] = de
                License[name] = l
                ruls[name] = r
                pkginme[name + v] = p


    res = '{"for":"' + str(len(void)) + '","server":[\r\n'
    fo = 0
    for i in nn.split('\t')[:-1]:
        v = '00'
        fo += 1
        vv = void[i]
        vv = vv.split('\t')
        for f in vv:
            ff = f[1:]
            vv = v[1:]
            if ff > vv:
                v = f
        res += '{"Package":"' + i +'","name":"' + names[i] +'","Version":"' + v +'","Depends":"' + Depends[i] + '","License":"' + License[i] + '","rul":"' + ruls[i] + '","Description":"' + data[i] +'"}'
        if fo != len(void):
            res += ','
    res += ']}'
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)