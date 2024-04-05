# coding=utf-8
#!/bin/python

import imp
import os

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    sql = imp.load_source("server/main/filesql.py","server/main/filesql.py")

    dir = ''
    name = ''
    post = RUL_CS
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'dir':
            dir = tmp[1]
        if tmp[0] == 'name':
            name = tmp[1]
    json = ''

    if name == "":
        json = '名称呢'
    else:
        if not os.path.exists(".config/filenocopy"):
            os.mkdir(".config/filenocopy")
        if not os.path.exists(".config/filenocopy/default.db"):
            data = {}
            data["name"] = "name"
            data["dir"] = "dir"
            sql.new(".config/filenocopy/default.db",data)
        fo = sql.catlen(".config/filenocopy/default.db")
        fsdata = sql.cat(".config/filenocopy/default.db",name,0)
        if not fsdata:
            data = {}
            data["name"] = name
            data["dir"] = dir
            sql.prin(".config/filenocopy/default.db",data)
            json = '添加成功'
        else:
            json = '已存在'

    httpserver.httppostchar(new_client_socket,"200",json.encode('utf-8'),"text/html;charset=UTF-8",Headers,info)
