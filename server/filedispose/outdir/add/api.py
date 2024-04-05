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

    if name == "":
        name = dir.split('/')[-1]

    json = ''
    if os.path.exists(dir):
        if not os.path.exists(".config/filenocopy"):
            os.mkdir(".config/filenocopy")
        if not os.path.exists(".config/filenocopy/outdir.db"):
            data = {}
            data["dir"] = "dir"
            data["name"] = "name"
            sql.new(".config/filenocopy/outdir.db",data)
        fo = sql.catlen(".config/filenocopy/outdir.db")
        fsdata = sql.cat(".config/filenocopy/outdir.db",dir,0)
        if not fsdata:
            if not os.path.exists(dir + "/" + name):
                if not os.path.exists(dir + "/" + name + ".db"):
                    data = {}
                    data["dir"] = "dir"
                    data["name"] = "name"
                    sql.new(dir + "/" + name + ".db",data)
                    data = {}
                    data["dir"] = dir
                    data["name"] = name
                    sql.prin(".config/filenocopy/outdir.db",data)
                    sql.prin(dir + "/" + name + ".db",data)
                    os.mkdir(dir + "/" + name)
                    json = '添加成功'
                else:
                    json = '存在数据库文件'
            else:
                json = '目录非空'
        else:
            json = '目录已添加'
    else:
        json = '目录不存在'

    httpserver.httppostchar(new_client_socket,"200",json.encode('utf-8'),"text/html;charset=UTF-8",Headers,info)
