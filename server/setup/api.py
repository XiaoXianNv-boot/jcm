
# coding=utf-8
#!/bin/python

import os
import sys
import time
import imp
import hashlib
import socket

def poskuan(name,data,l):
    return '\
<div class="col-xs-12 col-sm-' + l + ' widget-container-col" id="widget-container-col-6">\
    <div class="widget-box widget-color-dark light-border" id="widget-box-6">\
        <div class="widget-header">\
            <h5 class="widget-title smaller">' + name + '</h5>\
\
        </div>\
\
        <div class="widget-body">\
            <div class="widget-main padding-6">\
                ' + data + '\
            </div>\
        </div>\
    </div>\
</div>'

def resys(res,info):
    l2 = ''
    l2js = ''
    if info['OS'] == "Linux":
        l2 = '<button class="btn btn-sm" onclick="sysstop();return false;">停止系统</button>\r\n'
        l2js = 'function sysstop(){\r\n\
                    bootbox.confirm("停止系统,不关闭电源", function (result) {\r\n\
                        if(result){\r\n\
                            const cpuHttp = new XMLHttpRequest();\r\n\
                            cpuHttp.open("GET", \'setup/sys/stop\');\r\n\
                            cpuHttp.send();\r\n\
                            cpuHttp.onreadystatechange = function() {\r\n\
                                if(cpuHttp.readyState == 4 && cpuHttp.status == 200){\r\n\
                                    var data = JSON.parse(cpuHttp.responseText);\
                                    bootbox.confirm(data.data, function (result) {})\r\n\
                                }\
                            }\
                        }\r\n\
                    });\r\n\
                }\r\n'
    elif info['OS'] == "Windows":
        l2 = '<button class="btn btn-sm" onclick="sysstop();return false;">休眠</button>\r\n'
        l2js = 'function sysstop(){\r\n\
                    bootbox.confirm("休眠", function (result) {\r\n\
                        if(result){\r\n\
                            const cpuHttp = new XMLHttpRequest();\r\n\
                            cpuHttp.open("GET", \'setup/sys/shutdown\');\r\n\
                            cpuHttp.send();\r\n\
                            cpuHttp.onreadystatechange = function() {\r\n\
                                if(cpuHttp.readyState == 4 && cpuHttp.status == 200){\r\n\
                                    var data = JSON.parse(cpuHttp.responseText);\
                                    bootbox.confirm(data.data, function (result) {})\r\n\
                                }\
                            }\
                        }\r\n\
                    });\r\n\
                }\r\n'

    data = '\
        <p>\r\n\
            <button class="btn btn-sm " onclick="sysreset();return false;">重启系统</button>\r\n\
            <button class="btn btn-sm" onclick="sysexit();return false;">关机</button>\r\n' + l2 +'\
            <script type="text/javascript">\r\n\
function sysreset(){\r\n\
    bootbox.confirm("重启系统", function (result) {\r\n\
        if(result){\r\n\
            const cpuHttp = new XMLHttpRequest();\r\n\
            cpuHttp.open("GET", \'setup/sys/reset\');\r\n\
            cpuHttp.send();\r\n\
            cpuHttp.onreadystatechange = function() {\r\n\
                if(cpuHttp.readyState == 4 && cpuHttp.status == 200){\r\n\
                    var data = JSON.parse(cpuHttp.responseText);\
                    bootbox.confirm(data.data, function (result) {})\r\n\
                }\
            }\
        }\r\n\
    });\r\n\
}\r\n\
function sysexit(){\r\n\
    bootbox.confirm("关机", function (result) {\r\n\
        if(result){\r\n\
            const cpuHttp = new XMLHttpRequest();\r\n\
            cpuHttp.open("GET", \'setup/sys/poweroff\');\r\n\
            cpuHttp.send();\r\n\
            cpuHttp.onreadystatechange = function() {\r\n\
                if(cpuHttp.readyState == 4 && cpuHttp.status == 200){\r\n\
                    var data = JSON.parse(cpuHttp.responseText);\
                    bootbox.confirm(data.data, function (result) {})\r\n\
                }\
            }\
        }\r\n\
    });\r\n\
}\r\n' + l2js + '\
            </script>\
        </p>'
    res += poskuan("系统控制",data,"4")
    return res
def main(new_client_socket,post,Headers,info,user):
    link = ''
    path = ''
    res = '{}'
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'link':
            link = tmp[1]
        if tmp[0] == 'path':
            path = tmp[1]

    res = '{}'
    data = '\
        <p>\r\n\
            <button class="btn btn-sm btn-success" onclick="jcmreset();return false;">重启面板</button>\r\n\
            <button class="btn btn-sm" onclick="jcmexit();return false;">退出面板</button>\r\n\
            <script type="text/javascript">\r\n\
function jcmreset(){\r\n\
    bootbox.confirm("重启面板", function (result) {\r\n\
        if(result){\r\n\
            const cpuHttp = new XMLHttpRequest();\r\n\
            cpuHttp.open("GET", \'setup/jcmreset/reset\');\r\n\
            cpuHttp.send();\r\n\
            cpuHttp.onreadystatechange = function() {\r\n\
                if(cpuHttp.readyState == 4 && cpuHttp.status == 200){\r\n\
                    var data = JSON.parse(cpuHttp.responseText);\
                    bootbox.confirm(data.data, function (result) {})\r\n\
                }\
            }\
        }\r\n\
    });\r\n\
}\r\n\
function jcmexit(){\r\n\
    bootbox.confirm("退出面板", function (result) {\r\n\
        if(result){\r\n\
            const cpuHttp = new XMLHttpRequest();\r\n\
            cpuHttp.open("GET", \'setup/jcmreset/exit\');\r\n\
            cpuHttp.send();\r\n\
            cpuHttp.onreadystatechange = function() {\r\n\
                if(cpuHttp.readyState == 4 && cpuHttp.status == 200){\r\n\
                    var data = JSON.parse(cpuHttp.responseText);\
                    bootbox.confirm(data.data, function (result) {})\r\n\
                }\
            }\
        }\r\n\
    });\r\n\
}\r\n\
            </script>\
        </p>'
    res = poskuan("重启面板",data,"3")
    res = resys(res,info)
    strr = {}
    strr["data"] = res
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    sh = imp.load_source("server/main/php.py","server/main/php.py")
    data = sh.php(new_client_socket,"post","/setup.php",user,Headers,info,strr)
    httpserver.httppostchar(new_client_socket,"200",data.encode("utf-8"),"text/html;charset=UTF-8",Headers,info)
    #httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json",Headers,info)