# coding=utf-8
#!/bin/python

import imp
import os

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    sql = imp.load_source("server/main/filesql.py","server/main/filesql.py")
    import json
    post_data = post_data.decode("utf-8")
    post_data = json.loads(post_data,strict=False)
    dir = post_data["dir"]
    name = post_data["name"]
    id = post_data["id"]
    json = '{"id":"' + id + '",'

    if name == "":
        json += '"data":"名称呢"'
    else:
        if not os.path.exists(".config/filenocopy"):
            os.mkdir(".config/filenocopy")
        if not os.path.exists(".config/filenocopy/temp.db"):
            data = {}
            data["name"] = "name"
            data["dir"] = "dir"
            sql.new(".config/filenocopy/temp.db",data)
        fo = sql.catlen(".config/filenocopy/temp.db")
        fsdata = sql.cat(".config/filenocopy/temp.db",name,0)
        if not fsdata:
            data = {}
            data["name"] = name
            data["dir"] = dir
            sql.prin(".config/filenocopy/temp.db",data)
            json += '"data":"添加成功"'
        else:
            json += '"data":"已存在"'
    json += "}"
    httpserver.httppostchar(new_client_socket,"200",json.encode('utf-8'),"text/html;charset=UTF-8",Headers,info)
