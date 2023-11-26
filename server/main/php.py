# coding=utf-8
#!/bin/python

import socket
import os
import imp
import hashlib

def phpf(new_client_socket,post,RUL,user,Headers,strr,info,res):
    dir = ""
    theme = ''
    rull = RUL.split("/")
    for rulll in rull:
        if rulll == rull[-1]:
            rull[-1] = rull[-1]
        else:
            dir = dir + rulll + "/"
    if dir == '//':
        dir = '/'
    rulfile = ''#文件地址
    if os.path.isfile("./web/" + info["theme"] + RUL):
        rulfile = "./web/" + info["theme"] + RUL
        theme = info["theme"] + ''
    else:
        filedir = "./web/" + "Ace_Admin" + RUL
        if os.path.isfile(filedir):
            rulfile = "./web/" + "Ace_Admin" + RUL
            theme = "Ace_Admin"  + ''
    fs = open(rulfile, "rb")
    ini = fs.read().decode("utf-8").split("<?php")
    for p in ini:
        pp = p.split("?>")
        if len(pp) == 1:
            res += pp[0]
            #new_client_socket.send(pp[0].encode("utf-8"))
        else:
            ppp = pp[0].split(" ")
            if ppp[1] == "echo":
                if ppp[2][0] == "$":
                    nr = ppp[2][8:-3]
                    if ppp[2][1:-1] == "user":
                        res += user
                        #new_client_socket.send(user.encode("utf-8"))
                    elif ppp[2][1:7] == "_POST[":
                        _post = {}
                        for po in post:
                            pos = po.split('=')
                            _post[pos[0]] = po[len(pos[0])+1:]
                        try:
                            #new_client_socket.send(_post[ppp[2][8:-3]].encode("utf-8"))
                            res += _post[ppp[2][8:-3]]
                        except Exception as e:
                            #new_client_socket.send("NULL".encode("utf-8"))
                            res += "NULL"
                    else:
                        try:
                            #new_client_socket.send(strr[ppp[2][1:-1]].encode("utf-8"))
                            res += strr[ppp[2][1:-1]]
                        except Exception as e:
                            #new_client_socket.send("NULL".encode("utf-8"))
                            res += "NULL"
                else:
                    #new_client_socket.send(ppp[2][:-1].encode("utf-8"))
                    res += ppp[2][:-1]
            elif ppp[1] == "include":
                pppp = ppp[2][:-1].split(".")
                if pppp[-1] == "php'":
                    res = phpf(new_client_socket,post,Versino,ppp[2][:-1],user,Headers,strr,info,res)
                else:
                    fileincdir = "web/" + theme + dir + ppp[2][1:-2]
                    fss = open(fileincdir, "rb")
                    res += fss.read().decode("utf-8")
                    #new_client_socket.send(fss.read())
            #new_client_socket.send(pp[1].encode("utf-8"))
            res += pp[1]
    return res


def php(new_client_socket,post,RUL,user,Headers,info,strr = {}):
    res = ''
    res = phpf(new_client_socket,post,RUL,user,Headers,strr,info,res)
    return res