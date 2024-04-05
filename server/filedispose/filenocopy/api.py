# coding=utf-8
#!/bin/python

import imp
import os
import sys

def runn(new_client_socket,httpserver,sql,x,indir):
    dirn = os.listdir(x[0].decode('utf-8') + indir)
    dirn.sort(reverse=False)
    for i in dirn:
        dir = x[0].decode('utf-8') + indir + '/' + i
        if os.path.isdir(dir):
            httpserver.websockfsstr(new_client_socket,('d ' + x[1].decode('utf-8') + indir + '/' + i + '\r\n').encode("utf-8"))
            runn(new_client_socket,httpserver,sql,x,indir + '/' + i)
        else:
            fsdata = sql.cat(".config/filenocopy/data.db",i,0)
            if not fsdata:
                fsdata = sql.cat(".config/filenocopy/temp.db",i,0)
                if not fsdata:
                    addr = sql.cat(".config/filenocopy/default.db",i.split('.')[-1],0)
                    if not addr:
                        addr = indir[1:]
                    else:
                        addr = addr[1].decode('utf-8')
                    httpserver.websockfsstr(new_client_socket,('n ' + x[1].decode('utf-8') + indir + '/' + i + '\t' + addr + '\t' + i + '\r\n').encode("utf-8"))
                else:
                    httpserver.websockfsstr(new_client_socket,('f ' + x[1].decode('utf-8') + indir + '/' + i + '\t' + fsdata[1].decode('utf-8') + '\t' + i + '\r\n').encode("utf-8"))
            else:
                httpserver.websockfsstr(new_client_socket,('f ' + x[1].decode('utf-8') + indir + '/' + i + '\t' + fsdata[1].decode('utf-8') + '\t' + i + '\r\n').encode("utf-8"))

    forxh = 0
def run(new_client_socket,httpserver,sql):
    sys.setrecursionlimit(3000)
    #forxh = 0
    for i in sql.catall(".config/filenocopy/indir.db"):
        i = i.split(b'\t')
        runn(new_client_socket,httpserver,sql,i,'')

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    sql = imp.load_source("server/main/filesql.py","server/main/filesql.py")
    httpserver.websockinit(new_client_socket,Headers,info)

    data = sql.catlen(".config/filenocopy/disk.db")
    #data = httpserver.websockrx(new_client_socket)
    #data = httpserver.websockrx(new_client_socket)

    #httpserver.websockfsstr(new_client_socket,b'6')
    run(new_client_socket,httpserver,sql)

    httpserver.websockendstr(new_client_socket,b"END\r\n")