
# coding=utf-8
#!/bin/python

import os
import sys
import time
import imp
import hashlib
import socket
import threading

def run(info,no):
    if os.path.exists("/sbin/reboot"): 
        time.sleep(30)
        os.system('/sbin/reboot')
    else:
        os.system("shutdown -r -t 30")

def reboot(info):
    t = threading.Thread(target=run, args=(info,""))
    t.start()
    return "30S reboot"

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    link = ''
    path = ''
    res = '{}'
    for i in RUL_CS:
        tmp = i.split('=')
        if tmp[0] == 'link':
            link = tmp[1]
        if tmp[0] == 'path':
            path = tmp[1]

    res = '{"data":"' + reboot(info) + '"}'
    


    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)