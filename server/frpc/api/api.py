# coding=utf-8
#!/bin/python

import os
import sys
import threading
import time
import imp
from configparser import ConfigParser

def run_shell_frpc(info,no):
    os.system("mkdir -p " + info['tmp'])
    os.system("mkdir -p " + info['tmp'] + "/frpc")
    os.system("rm " + info['tmp'] + "/frpc/logs_")
    if os.path.exists("./Tools/.frp/jcm_frpc.ini") == False:
        os.system("cp ./Tools/.frp/frpc.ini ./Tools/.frp/jcm_frpc.ini")
    os.system("Tools/.frp/frpc -c ./Tools/.frp/jcm_frpc.ini >" + info['tmp'] + "/frpc/logs 2>" + info['tmp'] + "/frpc/logs ")
    os.system("echo stop >> " + info['tmp'] + "/frpc/logs ")
    os.system("mv " + info['tmp'] + "/frpc/logs " + info['tmp'] + "/frpc/logs_")

def catinfo(conf,section,option):
    if conf.has_section(section):
        if conf.has_option(section, option):
            return conf[section][option]
    return ''
            
def setinfo(conf,section,option,value):
    if conf.has_section(section) == False:
        conf.add_section(section)
    conf.set(section, option, value)
            

def main(new_client_socket,post,Headers,info,user):
    type = ""
    res = ""
    for i in post:
        tmp = i.split('=')
        if tmp[0] == 'type':
            type = tmp[1]
    if type == "run":
        res = '{'
        if os.path.exists(info['tmp'] + "/frpc/logs"):
            res += '"run":"run"'
        else:
            res += '"run":"norun"'
        if os.path.exists(".config/frpc/boot"):
            res += ',"boot":"yes"'
        else:
            res += ',"boot":"no"'
        if os.path.exists("./Tools/.frp/jcm_frpc.ini") == False:
            fs = open("Tools/.frp/frpc.ini", "rb")
            ini = fs.read()
            fs.close()
            fs = open("Tools/.frp/jcm_frpc.ini", "wb")
            fs.write(ini)
            fs.close()
        conf = ConfigParser()
        conf.read('Tools/.frp/jcm_frpc.ini')
        server_addr = catinfo(conf,'common','server_addr')
        server_port = catinfo(conf,'common','server_port')
        dashboard_port = catinfo(conf,'common','dashboard_port')
        dashboard_user = catinfo(conf,'common','dashboard_user')
        dashboard_pwd = catinfo(conf,'common','dashboard_pwd')
        dashboard_tls_mode = catinfo(conf,'common','dashboard_tls_mode')
        dashboard_tls_cert_file = catinfo(conf,'common','dashboard_tls_cert_file')
        dashboard_tls_key_file = catinfo(conf,'common','dashboard_tls_key_file')
        authentication_method = catinfo(conf,'common','authentication_method')
        oidc_client_id = catinfo(conf,'common','oidc_client_id')
        oidc_client_secret = catinfo(conf,'common','oidc_client_secret')
        oidc_audience = catinfo(conf,'common','oidc_audience')
        oidc_token_endpoint_url = catinfo(conf,'common','oidc_token_endpoint_url')
        admin_addr = catinfo(conf,'common','admin_addr')
        admin_port = catinfo(conf,'common','admin_port')
        admin_user = catinfo(conf,'common','admin_user')
        admin_pwd = catinfo(conf,'common','admin_pwd')
        tcp_mux = catinfo(conf,'common','tcp_mux')
        protocol = catinfo(conf,'common','protocol')
        pool_count = catinfo(conf,'common','pool_count')
        token = catinfo(conf,'common','token')

        res += ',"common":{'
        res += '"server_addr":"' + server_addr + '",'
        res += '"server_port":"' + server_port + '",'
        res += '"dashboard_port":"' + dashboard_port + '",'
        res += '"dashboard_user":"' + dashboard_user + '",'
        res += '"dashboard_pwd":"' + dashboard_pwd + '",'
        res += '"dashboard_tls_mode":"' + dashboard_tls_mode + '",'
        res += '"dashboard_tls_cert_file":"' + dashboard_tls_cert_file + '",'
        res += '"dashboard_tls_key_file":"' + dashboard_tls_key_file + '",'
        res += '"authentication_method":"' + authentication_method + '",'
        res += '"oidc_client_id":"' + oidc_client_id + '",'
        res += '"oidc_client_secret":"' + oidc_client_secret + '",'
        res += '"oidc_audience":"' + oidc_audience + '",'
        res += '"oidc_token_endpoint_url":"' + oidc_token_endpoint_url + '",'
        res += '"admin_addr":"' + admin_addr + '",'
        res += '"admin_port":"' + admin_port + '",'
        res += '"admin_user":"' + admin_user + '",'
        res += '"admin_pwd":"' + admin_pwd + '",'
        res += '"tcp_mux":"' + tcp_mux + '",'
        res += '"protocol":"' + protocol + '",'
        res += '"pool_count":"' + pool_count + '",'
        res += '"token":"' + token + '"'
        res += '},"data":['

        data = conf.sections()
        sh = os.popen("Tools/.frp/frpc status -c Tools/.frp/jcm_frpc.ini").read().split('\n')
        for i in data:
            if i != "common":
                name = i
                run = "加载失败"
                type        = catinfo(conf,i,'type')
                local_ip    = catinfo(conf,i,'local_ip')
                local_port  = catinfo(conf,i,'local_port')
                remote_port = catinfo(conf,i,'remote_port')
                error = 'frpc get status error:'
                if os.path.exists("" + info['tmp'] + "/frpc/logs"):
                    for s in sh:
                        ss = s.split(' ')
                        if ss[0] == name:
                            for sss in ss[1:]:
                                if sss != '':
                                    run = sss
                                    ss = s.split('  ')
                                    break
                            for sss in ss[1:]:
                                if sss != '':
                                    error = sss
                    if error != (server_addr + ":" + remote_port):
                        if error != ' ':
                            run = error
                            
                            
                else:
                    run = "no"

                res += '{"name":"' + name + '",'
                res += '"run":"' + run + '",'
                res += '"type":"' + type + '",'
                res += '"local_ip":"' + local_ip + '",'
                res += '"local_port":"' + local_port + '",'
                res += '"remote_port":"' + remote_port + '"},'


        res += '{}],\"datafo\":\"' 
        res += str(len(data) - 1)
        res += '\"}'
    elif type == "start":
        t = threading.Thread(target=run_shell_frpc, args=(info,"no"))
        t.start()
        time.sleep(5)
        if os.path.exists("" + info['tmp'] + "/frpc/logs"):
            res = '{"data":"OK"}'
        elif os.path.exists("" + info['tmp'] + "/frpc/logs_"):
            res = '{"data":"ERROR"}'
        else:
            res = '{"data":"time..."}'
    elif type == "server":
        server_addr = ''
        server_port = ''
        token = ''

        res = '{"data":"ERROR"}'

        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'server':
                server_addr = tmp[1]
            if tmp[0] == 'port':
                server_port = tmp[1]
            if tmp[0] == 'tocken':
                token = tmp[1]

        conf = ConfigParser()
        conf.read('Tools/.frp/jcm_frpc.ini')
        setinfo(conf,"common","server_addr",server_addr)
        setinfo(conf,"common","server_port",server_port)
        if token == '':
            conf.remove_option("common", "token")
        else:
            setinfo(conf,"common","token",token)
        with open('Tools/.frp/jcm_tmp_frpc.ini','w',encoding='utf-8') as f:
            conf.write(f)
        sh = os.popen('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini').read().split('\r')[0].split('\n')[0]
        if sh == 'frpc: the configuration file Tools/.frp/jcm_tmp_frpc.ini syntax is ok':
            os.system('rm Tools/.frp/jcm_frpc.ini')
            os.system('mv Tools/.frp/jcm_tmp_frpc.ini Tools/.frp/jcm_frpc.ini')
            os.system('Tools/.frp/frpc reload -c Tools/.frp/jcm_frpc.ini')
            res = '{"data":"OK"}'
        else:
            os.system('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini >/tmp/jcm/frpc/logs_tmp')
            res = '{"data":"ERROR"}'
    elif type == "web":
        admin_addr = ''
        admin_port = ''
        admin_user = ''
        admin_pwd  = ''

        res = '{"data":"ERROR"}'

        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'admin_addr':
                admin_addr = tmp[1]
            if tmp[0] == 'admin_port':
                admin_port = tmp[1]
            if tmp[0] == 'admin_user':
                admin_user = tmp[1]
            if tmp[0] == 'admin_pwd':
                admin_pwd = tmp[1]

        conf = ConfigParser()
        conf.read('Tools/.frp/jcm_frpc.ini')
        setinfo(conf,"common","admin_addr",admin_addr)
        setinfo(conf,"common","admin_port",admin_port)
        setinfo(conf,"common","admin_user",admin_user)
        setinfo(conf,"common","admin_pwd",admin_pwd)
        
        with open('Tools/.frp/jcm_tmp_frpc.ini','w',encoding='utf-8') as f:
            conf.write(f)
        sh = os.popen('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini').read().split('\r')[0].split('\n')[0]
        if sh == 'frpc: the configuration file Tools/.frp/jcm_tmp_frpc.ini syntax is ok':
            os.system('rm Tools/.frp/jcm_frpc.ini')
            os.system('mv Tools/.frp/jcm_tmp_frpc.ini Tools/.frp/jcm_frpc.ini')
            os.system('Tools/.frp/frpc reload -c Tools/.frp/jcm_frpc.ini')
            res = '{"data":"OK"}'
        else:
            os.system('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini >/tmp/jcm/frpc/logs_tmp')
            res = '{"data":"ERROR"}'
        
    elif type == "add":
        name = ''
        type = ''
        local_ip = ''
        local_port = ''
        remote_port  = ''

        res = '{"data":"ERROR"}'

        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'name':
                name = tmp[1]
            if tmp[0] == 'types':
                type = tmp[1]
            if tmp[0] == 'local_ip':
                local_ip = tmp[1]
            if tmp[0] == 'local_port':
                local_port = tmp[1]
            if tmp[0] == 'remote_port':
                remote_port = tmp[1]

        conf = ConfigParser()
        conf.read('Tools/.frp/jcm_frpc.ini')
        setinfo(conf,name,"type",type)
        setinfo(conf,name,"local_ip",local_ip)
        setinfo(conf,name,"local_port",local_port)
        setinfo(conf,name,"remote_port",remote_port)
        
        with open('Tools/.frp/jcm_tmp_frpc.ini','w',encoding='utf-8') as f:
            conf.write(f)
        sh = os.popen('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini').read().split('\r')[0].split('\n')[0]
        if sh == 'frpc: the configuration file Tools/.frp/jcm_tmp_frpc.ini syntax is ok':
            os.system('rm Tools/.frp/jcm_frpc.ini')
            os.system('mv Tools/.frp/jcm_tmp_frpc.ini Tools/.frp/jcm_frpc.ini')
            sh = os.popen('Tools/.frp/frpc reload -c Tools/.frp/jcm_frpc.ini').read().split('\r')[0].split('\n')[0]
            res = '{"data":"' + sh + '"}'
        else:
            os.system('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini >/tmp/jcm/frpc/logs_tmp')
            res = '{"data":"ERROR"}'
    elif type == "del":
        name = ''
        
        res = '{"data":"ERROR"}'

        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'name':
                name = tmp[1]

        conf = ConfigParser()
        conf.read('Tools/.frp/jcm_frpc.ini')
        conf.remove_section(name)

        with open('Tools/.frp/jcm_tmp_frpc.ini','w',encoding='utf-8') as f:
            conf.write(f)
        sh = os.popen('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini').read().split('\r')[0].split('\n')[0]
        if sh == 'frpc: the configuration file Tools/.frp/jcm_tmp_frpc.ini syntax is ok':
            os.system('rm Tools/.frp/jcm_frpc.ini')
            os.system('mv Tools/.frp/jcm_tmp_frpc.ini Tools/.frp/jcm_frpc.ini')
            sh = os.popen('Tools/.frp/frpc reload -c Tools/.frp/jcm_frpc.ini').read().split('\r')[0].split('\n')[0]
            res = '{"data":"' + sh + '"}'
        else:
            os.system('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini >/tmp/jcm/frpc/logs_tmp')
            res = '{"data":"ERROR"}'
        

    elif type == "edit":
        name = ''
        type = ''
        local_ip = ''
        local_port = ''
        remote_port  = ''
        id  = ''

        res = '{"data":"ERROR"}'

        for i in post:
            tmp = i.split('=')
            if tmp[0] == 'name':
                name = tmp[1]
            if tmp[0] == 'types':
                type = tmp[1]
            if tmp[0] == 'local_ip':
                local_ip = tmp[1]
            if tmp[0] == 'local_port':
                local_port = tmp[1]
            if tmp[0] == 'remote_port':
                remote_port = tmp[1]
            if tmp[0] == 'id':
                id = tmp[1]

        conf = ConfigParser()
        conf.read('Tools/.frp/jcm_frpc.ini')
        if id != name:
            conf.remove_section(id)
        setinfo(conf,name,"type",type)
        setinfo(conf,name,"local_ip",local_ip)
        setinfo(conf,name,"local_port",local_port)
        setinfo(conf,name,"remote_port",remote_port)
        
        with open('Tools/.frp/jcm_tmp_frpc.ini','w',encoding='utf-8') as f:
            conf.write(f)
        sh = os.popen('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini').read().split('\r')[0].split('\n')[0]
        if sh == 'frpc: the configuration file Tools/.frp/jcm_tmp_frpc.ini syntax is ok':
            os.system('rm Tools/.frp/jcm_frpc.ini')
            os.system('mv Tools/.frp/jcm_tmp_frpc.ini Tools/.frp/jcm_frpc.ini')
            sh = os.popen('Tools/.frp/frpc reload -c Tools/.frp/jcm_frpc.ini').read().split('\r')[0].split('\n')[0]
            res = '{"data":"' + sh + '"}'
        else:
            os.system('Tools/.frp/frpc verify -c Tools/.frp/jcm_tmp_frpc.ini >/tmp/jcm/frpc/logs_tmp')
            res = '{"data":"ERROR"}'
    elif type == "stop":
        sh = os.popen('ps aux | grep "Tools/.frp/frpc"').read().split('\n')
        kill = "0"
        res = "ERR"
        for s in sh:
            ss = s.split('2>')
            if len(ss) == 1:
                ss = s.split('./Tools/.frp/jcm_frpc.ini')
                if len(ss) == 2:
                    for sss in s.split(' ')[1:]:
                        if sss != "":
                            kill = sss
                            res = os.popen('kill ' + kill).read().split('\r')[0].split('\n')[0]
                            time.sleep(1)
                            break
        if os.path.exists("" + info['tmp'] + "/frpc/logs"):
            os.remove("" + info['tmp'] + "/frpc/logs")
        if res == "":
            res = "OK"
        res = '{"data":"' + res + '"}'
    elif type == "booton":
        if os.path.exists(".config/frpc") == False:
            os.mkdir(".config/frpc")
        os.system("echo boot >.config/frpc/boot")
        res = '{"data":"OK"}'
    elif type == "bootoff":
        os.remove(".config/frpc/boot")
        res = '{"data":"OK"}'
        

            


    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    httpserver.httppostchar(new_client_socket,"200",res.encode("utf-8"),"application/json;charset=UTF-8",Headers,info)