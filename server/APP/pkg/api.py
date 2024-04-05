# coding=utf-8
#!/bin/python

import imp
import traceback

def main(data):
    
    new_client_socket = data["new_client_socket"]
    RUL_CS            = data["RUL_CS"]
    post_data         = data["post_data"]
    Headers           = data["Headers"]
    info              = data["info"]
    user              = data["user"]
    Versino = "V1.0"
    post = RUL_CS
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.websockinit(new_client_socket,Headers,info)
    data = httpserver.websockrx(new_client_socket)
    #httpserver.websockfs(new_client_socket,data[0])

    try:
        sh = imp.load_source("server/APP/pkg.py","server/APP/pkg.py")
        sh.main(new_client_socket,post,Versino,Headers,info,user)
    except Exception as e:
        #print(e.args)
        run = imp.load_source("server/run.py","server/run.py")
        run.logsprnt("ERROR",info,e.args)
        err = traceback.format_exc().split('\n')[:-1]
        for ee in err:
            httpserver.websockfs(new_client_socket,('0' + ee + '\r\n').encode("utf-8"))
        httpserver.websockend(new_client_socket,b"exit")

