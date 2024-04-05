# coding=utf-8
#!/bin/python

import imp
import os

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    sql = imp.load_source("server/main/filesql.py","server/main/filesql.py")

    json = ''
    fo = sql.catlen(".config/filenocopy/indir.db")

    json += '{"fo":' + str(fo) + ',"data":['
    for i in sql.catall(".config/filenocopy/indir.db"):
        i = i.split(b'\t')
        if os.path.exists(i[0].decode("utf-8")):
            json += '{"dir":"' + i[0].decode("utf-8") + '","status":"正常"},'
        else:
            json += '{"dir":"' + i[0].decode("utf-8") + '","status":"No Dir"},'
    json += '{}]}'
    httpserver.httppostchar(new_client_socket,"200",json.encode('utf-8'),"application/json",Headers,info)
