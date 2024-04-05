
import os
import sys
import time
import imp

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    type = ""

    post = RUL_CS
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'type':
            type = tmp[1]

    if type == "index":
        data = '\
            <div class="tabbable" >\
                <ul class="nav nav-tabs" id="myTab">\
                    <li style="float: right">\
                        <a data-toggle="tab" href="#tabdata" onclick="click:addtab();return false;">\
                            &nbsp;&nbsp;&nbsp;&nbsp;添加 &nbsp;&nbsp;&nbsp;&nbsp;\
                        </a>\
                    </li>\
                </ul>\
                <div class="tab-content" style="height: 100%;" id="tabn">\
                    <div id="tabdata" class="tab-pane fade">\
                        <div id="tabs"></div>\
                    </div>\
                </div>\
            </div>\
            <script type="text/javascript">\
                //function index(){\
                    document.getElementById("biaotou").innerHTML = "123";\
                //}\
            </script>'
        httpserver.httppostchar(new_client_socket,"200",data.encode("utf-8"),"text/html;charset=UTF-8",Headers,info)
        return
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"400","400 bad request".encode("utf-8"),"text/html;charset=UTF-8",Headers,info)

