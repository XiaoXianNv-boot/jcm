# coding=utf-8
#!/bin/python

import imp
import os

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    sql = imp.load_source("server/main/filesql.py","server/main/filesql.py")

    dir = ''
    post = RUL_CS
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'dir':
            dir = tmp[1]

    json = ''
    if os.path.exists(dir):
        if not os.path.exists(".config/filenocopy"):
            os.mkdir(".config/filenocopy")
        if not os.path.exists(".config/filenocopy/indir.db"):
            data = {}
            data["dir"] = "dir"
            sql.new(".config/filenocopy/indir.db",data)
        fo = sql.catlen(".config/filenocopy/indir.db")
        fsdata = sql.cat(".config/filenocopy/indir.db",dir,0)
        if not fsdata:
            data = {}
            data["dir"] = dir
            sql.prin(".config/filenocopy/indir.db",data)
            json = '添加成功'
        else:
            json = '目录已添加'
    else:
        json = '目录不存在'

    httpserver.httppostchar(new_client_socket,"200",json.encode('utf-8'),"text/html;charset=UTF-8",Headers,info)
