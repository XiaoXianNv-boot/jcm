
# coding=utf-8
#!/bin/python

import os
import sys
import time
import imp
import hashlib
import socket

def main(data):
    
    new_client_socket = data["new_client_socket"]
    RUL_CS            = data["RUL_CS"]
    post_data         = data["post_data"]
    Headers           = data["Headers"]
    info              = data["info"]
    user              = data["user"]
    link = ''
    path = ''
    res = '{}'
    for i in RUL_CS:
        tmp = i.split('=')
        if tmp[0] == 'link':
            link = tmp[1]
        if tmp[0] == 'path':
            path = tmp[1]

    res = '{"data":"OK"}'
    run = imp.load_source('run',"server/run.py")
    run.shutdown("reset")


    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)