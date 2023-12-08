# coding=utf-8
#!/bin/python

import imp
import os
import socket
import time
import ssl

def mkdir(name):
    if os.path.exists(name) == False:
        os.mkdir(name)

def prin(new_client_socket,data):
    if new_client_socket == 'null':
        print(data.decode("utf-8"),end='')
    else:
        httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
        httpserver.websockfs(new_client_socket,b'0' + data)



def main(new_client_socket,post,Versino,Headers,info,user):
    posts = post[2].split('=')
    if posts[0] == 'bash':
        if posts[1] == 'updata':
            update(new_client_socket,post,Versino,Headers,info)
            httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
            httpserver.websockend(new_client_socket,b"END\r\n")
        elif posts[1][:len('install')] == 'install':
            install(new_client_socket,post,Versino,Headers,info)
            httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
            httpserver.websockend(new_client_socket,b"END\r\n")
    else:
        prin(new_client_socket,('参数错误 \r\n').encode("utf-8"))
        httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
        httpserver.websockend(new_client_socket,b"END\r\n")

def install(new_client_socket,post,Versino,Headers,info):
    posts = post[2].split('=')
    rull = ''
    data = {}
    void = {}
    names = {}
    nn = ""
    Depends = {}
    License = {}
    ruls = {}
    pkginme = {}
    if posts[0] == 'bash':
        posts = posts[1].split('_')
        yuan = os.listdir(".config/APP/data/")
        yuan.sort(reverse=True)
        for y in yuan:
            fs = open(".config/APP/data/" + y,'r')
            yrul = fs.read().split('\n')[1:-1]
            for i in yrul:
                i = i.split(',')
                name = i[0].split('"')[3]
                n = i[1].split('"')[3]
                d = i[7].split('"')[3]
                v = i[2].split('"')[3]
                de = i[3].split('"')[3]
                l = i[4].split('"')[3]
                r = i[5].split('"')[3]
                p = i[6].split('"')[3]
                try:
                    void[name] = void[name] + "\t" + v
                    pkginme[name + v] = p
                except Exception as e:
                    data[name] = d
                    void[name] = v
                    names[name] = n
                    nn += name + '\t'
                    Depends[name] = de
                    License[name] = l
                    ruls[name] = r
                    pkginme[name + v] = p
    try:
        v = void[posts[1]]
    except Exception as e:
        prin(new_client_socket,("Package not found").encode("utf-8"))
        return
    prin(new_client_socket,b'wget ')
    vv = void[posts[1]]
    v = '00'
    vv = vv.split('\t')
    for f in vv:
        ff = f[1:]
        vv = v[1:]
        if ff > vv:
            v = f
    rul = ruls[posts[1]] + pkginme[posts[1]+v]
    if os.path.exists(".tmp/APP/dl/" + rul.split('/')[-1]):
        os.remove(".tmp/APP/dl/" + rul.split('/')[-1])
    if os.path.exists(".tmp") == False:
        os.mkdir(".tmp")
    if os.path.exists(".tmp/APP") == False:
        os.mkdir(".tmp/APP")
    if os.path.exists(".tmp/APP/dl") == False:
        os.mkdir(".tmp/APP/dl")
    cat,cdata = Client(rul,prin,new_client_socket,".tmp/APP/dl/" + rul.split('/')[-1])
    prin(new_client_socket,b'\r\n')
    if cat == '200':
        #cdata = cdata.decode('utf-8')
        #os.system("rm -rf .out")
        if os.path.exists(".out/" + rul.split('/')[-1]):
            os.system("rm -rf .out/" + rul.split('/')[-1])
        if not os.path.exists(".out"):
            os.mkdir(".out")
        os.mkdir(".out/" + rul.split('/')[-1])
        sh = "tar xzf .tmp/APP/dl/" + rul.split('/')[-1] + " -C .out/" + rul.split('/')[-1]
        os.system(sh)
        sh = ".out/"  + rul.split('/')[-1] + "/.out/server/" + posts[1] + "/Package.py"
        #os.system('cp ' + sh + ' ./')
        #sh = "Package.py"
        sh = imp.load_source(sh,sh)
        sh.install(new_client_socket,post,Versino,Headers,info,prin)
        #shrun = os.popen(sys.executable + " .out/server/" + p.split('_')[0] + "/Package.py prin")
        #data = shrun.buffer.read().decode(encoding='utf8')
        prin(new_client_socket,('').encode("utf-8"))
    else:
        prin(new_client_socket,(' \x1B[1;3;31mERROR: ' + cdata.decode('utf-8') + '\x1B[0m\r\n').encode("utf-8"))
        fs.close()
        

def Client(yyrul,prin,new_client_socket,file):

    prin(new_client_socket,(yyrul).encode("utf-8"))
    tmp = yyrul.split('/')
    tmpp = ''
    if tmp[0] == 'http:':
        tmpp = (tmp[2] + ':80').split(':')
    else:
        tmpp = (tmp[2] + ':443').split(':')
    ruldir = "/".split('/')
    ruldir[0] = tmp[0] + '//'
    if len(tmpp) == 2:
        ruldir[1] = yyrul[(len(ruldir[0] + tmpp[0])):]
    else:
        ruldir[1] = yyrul[(len(ruldir[0] + tmpp[0] + ':' + tmpp[1])):]
    #cat,cdata = Client(rul,prin,new_client_socket)
    #cat,cdata = run.Client(tmpp[0],int(tmpp[1]),ruldir[1] + '/Packages')
    cat,cdata = crul(tmpp[0],int(tmpp[1]),ruldir,prin,new_client_socket,file)
    if cat == '301':
        prin(new_client_socket,(' 301\r\n').encode("utf-8"))
        cat,cdata = Client(cdata.decode('utf-8'),prin,new_client_socket,file)
    elif cat == '302':
        prin(new_client_socket,(' 302\r\n        ').encode("utf-8"))
        cat,cdata = Client(cdata.decode('utf-8'),prin,new_client_socket,file)
    
    return cat,cdata

def crul(ip,dk,dir,prin,new_client_socket,file):
    try:
        if dk == "":
            dk = 80
        socket.setdefaulttimeout(10)
        client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
        #client.connect(('openwrt.lan',80))
        if dir[0] == "https://":
            client = ssl.wrap_socket(client,cert_reqs=ssl.CERT_REQUIRED,ca_certs='server/main/DigiCert Global Root CA.crt')
        fsdata = 'GET ' + dir[1] + ' HTTP/1.1\r\n'
        if dir[0] == "https://":
            if dk == 443:
                fsdata = fsdata + 'Host: ' + ip + '\r\n'
            else:
                fsdata = fsdata + 'Host: ' + ip + ':' + str(dk) + '\r\n'
        else: 
            if dk == 80:
                fsdata = fsdata + 'Host: ' + ip + '\r\n'
            else:
                fsdata = fsdata + 'Host: ' + ip + ':' + str(dk) + '\r\n'
        fsdata = fsdata + 'Referer: ' + dir[0] + ip + dir[1] + '\r\n'

        fs = open(".config/main/cookie","rb")
        for c in fs.read().decode("utf-8").split('\n'):
            if c.split(':')[0] == ip:
                fsdata = fsdata + 'Cookie: ' + c.split(':')[1] + '\r\n'
        client.connect((ip,dk))
        client.send((fsdata + '\r\n').encode("utf-8"))
        data = b''
        run = 0
        d = ''
        cd = 0
        cdt = ''
        dowscharcd = 0
        times = time.strftime("%S", time.localtime()) 
        fs = ''
        if file != '':
            fs = open(file,'wb')
        while run == 0:
            try:
                d = client.recv(10240000)
            except Exception as e:
                #print(e.args)
                #if len(d) != 1024:
                #    run = 1
                if data == b'':
                    return "404",e.args[-1].encode("utf-8")
                else:
                    run = 1
                    if e.args[0] == 'timed out':
                        d = False
                #break
            if d:
                if dowscharcd == 0:
                    data = data + d
                    if len(data.split(b'\r\n\r\n')) > 1:
                        for ddd in data.split(b'\r\n\r\n')[0].split(b'\r\n'):
                            dddd = ddd.split(b': ')
                            if dddd[0] == b'Content-Length':
                                dowscharcd = int(dddd[1])
                if dowscharcd != 0:
                    #cd = 0
                    if file == '':
                        data = data + d
                        cd = len(data[len(data.split(b'\r\n\r\n')[0])+4:])

                    else:
                        if cd == 0:
                            cd = len(data[len(data.split(b'\r\n\r\n')[0])+4:])
                            datas = data[len(data.split(b'\r\n\r\n')[0])+4:]
                            fs.write(datas)
                        else:
                            cd += len(d)
                            fs.write(d)
                    if dowscharcd == cd:
                        run = 1
                        jdcd = len(cdt)
                        while jdcd != 0:
                            prin(new_client_socket,('\b \b').encode("utf-8"))
                            jdcd = jdcd - 1
                        ramall = ""
                        size = dowscharcd
                        if size < 1024:
                            ramall = str(size)
                            ramall = ramall + "B"
                        elif size < (1024 * 1024):
                            ramall = str(size / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "KB"
                                else:
                                    ramall = ramall + "KB"
                            else:
                                ramall = ramall + "KB"
                        elif size < (1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "MB"
                                else:
                                    ramall = ramall + "MB"
                            else:
                                ramall = ramall + "MB"
                        elif size < (1024 * 1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "GB"
                                else:
                                    ramall = ramall + "GB"
                            else:
                                ramall = ramall + "GB"
                        
                        dows = ramall
                        ramall = ""
                        size = cd
                        if size < 1024:
                            ramall = str(size)
                            ramall = ramall + "B"
                        elif size < (1024 * 1024):
                            ramall = str(size / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "KB"
                                else:
                                    ramall = ramall + "KB"
                            else:
                                ramall = ramall + "KB"
                        elif size < (1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "MB"
                                else:
                                    ramall = ramall + "MB"
                            else:
                                ramall = ramall + "MB"
                        elif size < (1024 * 1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "GB"
                                else:
                                    ramall = ramall + "GB"
                            else:
                                ramall = ramall + "GB"
                        
                        cdt = " [" + dows + "/" + ramall + "] " + '{:.2%}'.format(cd/dowscharcd)
                        prin(new_client_socket,(cdt).encode("utf-8"))
                    if times != time.strftime("%S", time.localtime()):
                        times = time.strftime("%S", time.localtime())
                        jdcd = len(cdt)
                        ramall = ''
                        while jdcd != 0:
                            ramall += '\b \b'
                            jdcd = jdcd - 1
                        prin(new_client_socket,(ramall).encode("utf-8"))
                        ramall = ""
                        size = dowscharcd
                        if size < 1024:
                            ramall = str(size)
                            ramall = ramall + "B"
                        elif size < (1024 * 1024):
                            ramall = str(size / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "KB"
                                else:
                                    ramall = ramall + "KB"
                            else:
                                ramall = ramall + "KB"
                        elif size < (1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "MB"
                                else:
                                    ramall = ramall + "MB"
                            else:
                                ramall = ramall + "MB"
                        elif size < (1024 * 1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "GB"
                                else:
                                    ramall = ramall + "GB"
                            else:
                                ramall = ramall + "GB"
                            
                        dows = ramall
                        ramall = ""
                        size = cd
                        if size < 1024:
                            ramall = str(size)
                            ramall = ramall + "B"
                        elif size < (1024 * 1024):
                            ramall = str(size / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "KB"
                                else:
                                    ramall = ramall + "KB"
                            else:
                                ramall = ramall + "KB"
                        elif size < (1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "MB"
                                else:
                                    ramall = ramall + "MB"
                            else:
                                ramall = ramall + "MB"
                        elif size < (1024 * 1024 * 1024 * 1024):
                            ramall = str(size / 1024 / 1024 / 1024)
                            if len(ramall.split('.')) == 2:
                                if len(ramall.split('.')[1]) > 2:
                                    ramall = ramall.split('.')[0] + '.' + ramall.split('.')[1][:2] + "GB"
                                else:
                                    ramall = ramall + "GB"
                            else:
                                ramall = ramall + "GB"
                        if data[:len(b'HTTP/1.1 404')] == b'HTTP/1.1 404':
                            break
                        cdt = " [" + dows + "/" + ramall + "] " + '{:.2%}'.format(cd/dowscharcd)
                        prin(new_client_socket,(cdt).encode("utf-8"))
                    if dir[1] == '/assets/info':
                        if data[-1] == '}':
                            run = 1
            else:
                run = 1
        #print(data)
        client.close()
        if file != '':
            fs.close()
        if data[:len(b'HTTP/1.1 200')] == b'HTTP/1.1 200':
            datad = b''
            for ddd in data.split(b'\r\n\r\n')[1:]:
                datad = datad + b'\r\n\r\n' + ddd
            return '200',datad[4:]
        elif data[:len(b'HTTP/1.1 301')] == b'HTTP/1.1 301':
            datad = b''
            for ddd in data.split(b'\r\n\r\n')[0].split(b'\r\n'):
                dddd = ddd.split(b': ')
                if dddd[0] == b'Location':
                    return '301',dddd[1]
            return '500',b'301'
        elif data[:len(b'HTTP/1.1 302')] == b'HTTP/1.1 302':
            datad = b''
            for ddd in data.split(b'\r\n\r\n')[0].split(b'\r\n'):
                dddd = ddd.split(b': ')
                if dddd[0] == b'Location':
                    return '302',dddd[1]
            return '500',b'302'
        if data[:len(b'HTTP/1.1 ')] == b'HTTP/1.1 ':
            return data[len(b'HTTP/1.1 '):len(b'HTTP/1.1 ') + 3].decode('utf-8'),data.split(b'\r\n')[0][len(b'HTTP/1.1 '):]
    except Exception as e:
        #print(e.args)
        return "404",e.args[-1].encode("utf-8")
    socket.setdefaulttimeout(0)


def update(new_client_socket,post,Versino,Headers,info):
    sh = ''
    #prin(new_client_socket,('read software source \r\n').encode("utf-8"))
    #print('no edit')
    if os.path.exists(".config/APP/pkg/main") == False:
        if os.path.exists(".config/APP") == False:
            os.mkdir(".config/APP")
        if os.path.exists(".config/APP/pkg") == False:
            os.mkdir(".config/APP/pkg")
        if os.path.exists(".config/APP/pkg/main") == False:
            os.mkdir(".config/APP/pkg/main")
            fs = open(".config/APP/pkg/main/0","wb")
            fs.write(b"http://openwrt.lan/data/jcm/pkg")
            fs.close()
            fs = open(".config/APP/pkg/main/1","wb")
            fs.write(b"http://jiang144.i234.me/data/jcm/pkg")
            fs.close()
            fs = open(".config/APP/pkg/main/2","wb")
            fs.write(b"http://jiang144.i234.me/jcm/pkg")
            fs.close()
            fs = open(".config/APP/pkg/main/3","wb")
            fs.write(b"https://github.com/XiaoXianNv-boot/jcm/releases/download/Preview")
            fs.close()
    yuan = os.listdir(".config/APP/pkg/")
    yuan.sort(reverse=True)
    for y in yuan:
        if os.path.isdir(".config/APP/pkg/" + y):
            for i in range(len(os.listdir(".config/APP/pkg/" + y))):
                if os.path.exists(".config/APP/pkg/" + y + '/' + str(i)):
                    fs = open(".config/APP/pkg/" + y + '/' + str(i),'r')
                    yrul = fs.read().split('\n')
                    for yyrul in yrul:
                        if yyrul != '':
                            prin(new_client_socket,(y + '[' + str(i)+ ']\t').encode("utf-8"))
                            cat,cdata = Client(yyrul + '/Packages',prin,new_client_socket,'')
                            if cat == '200':
                                mkdir(".config/APP/data")
                                fsw = open(".config/APP/data/" + y + ".js",'bw')
                                fsw.write("[\r\n".encode("utf-8"))
                                cdata = cdata.decode('utf-8')
                                cdata = cdata.split("\n\n")
                                #prin(new_client_socket,(' ' + cdata + '\r\n').encode("utf-8"))
                                #os.system("rm -rf .config/APP/tmp")
                                #os.remove('.config/APP/tmp')
                                for pkgg in cdata:
                                    if pkgg != '':
                                        pkggg = pkgg.split('\n')
                                        Package = ''
                                        name = ''
                                        Version = ''
                                        Depends = ''
                                        License = ''
                                        issued = 'pkg'
                                        for p in pkggg:
                                            pp = p.split(':')
                                            if pp[0] == "Package":
                                                Package = pp[1].split('\r')[0]
                                            if pp[0] == "name":
                                                name = pp[1].split('\r')[0]
                                            if pp[0] == "Version":
                                                Version = pp[1].split('\r')[0]
                                            if pp[0] == "Depends":
                                                Depends = pp[1].split('\r')[0]
                                            if pp[0] == "License":
                                                License = pp[1].split('\r')[0]
                                            if pp[0] == "issued":
                                                issued = pp[1].split('\r')[0]
                                            if pp[0] == "Description":
                                                Description = pp[1].split('\r')[0]
                                        fsww = '{"Package":"' + Package + '","name":"' + name + '","Version":"' + Version + '","Depends":"' + Depends + '","License":"' + License + '","rul":"' + yyrul + '/' + '","file":"' + Package + '_' + Version + '.pkg","Description":"' + Description + '"},\r\n'
                                        fsw.write(fsww.encode("utf-8"))
                                prin(new_client_socket,( '\r\n').encode("utf-8"))
                                y = '\r'
                                fsw.write("{}]".encode("utf-8"))
                            else:
                                prin(new_client_socket,(' \x1B[1;3;31mERROR: ' + cdata.decode('utf-8') + '\x1B[0m\r\n').encode("utf-8"))
                                fs.close()
                                break
        else:
            fs = open(".config/APP/pkg/" + y,'r')
            yrul = fs.read().split('\n')
            for yyrul in yrul:
                if yyrul != '':
                    prin(new_client_socket,(y + '\t').encode("utf-8"))
                    cat,cdata = Client(yyrul + '/Packages',prin,new_client_socket,'')
                    if cat == '200':
                        mkdir(".config/APP/data")
                        fsw = open(".config/APP/data/" + y + ".js",'bw')
                        fsw.write("[\r\n".encode("utf-8"))
                        cdata = cdata.decode('utf-8')
                        cdata = cdata.split("\n\n")
                        #prin(new_client_socket,(' ' + cdata + '\r\n').encode("utf-8"))
                        #os.system("rm -rf .config/APP/tmp")
                        #os.remove('.config/APP/tmp')
                        for pkgg in cdata:
                            if pkgg != '':
                                pkggg = pkgg.split('\n')
                                Package = ''
                                name = ''
                                Version = ''
                                Depends = ''
                                License = ''
                                issued = 'pkg'
                                for p in pkggg:
                                    pp = p.split(':')
                                    if pp[0] == "Package":
                                        Package = pp[1].split('\r')[0]
                                    if pp[0] == "name":
                                        name = pp[1].split('\r')[0]
                                    if pp[0] == "Version":
                                        Version = pp[1].split('\r')[0]
                                    if pp[0] == "Depends":
                                        Depends = pp[1].split('\r')[0]
                                    if pp[0] == "License":
                                        License = pp[1].split('\r')[0]
                                    if pp[0] == "issued":
                                        issued = pp[1].split('\r')[0]
                                    if pp[0] == "Description":
                                        Description = pp[1].split('\r')[0]
                                fsww = '{"Package":"' + Package + '","name":"' + name + '","Version":"' + Version + '","Depends":"' + Depends + '","License":"' + License + '","rul":"' + yyrul + '/' + '","file":"' + Package + '_' + Version + '.pkg","Description":"' + Description + '"},\r\n'
                                fsw.write(fsww.encode("utf-8"))
                        prin(new_client_socket,( '\r\n').encode("utf-8"))
                        y = '\r'
                        fsw.write("{}]".encode("utf-8"))
                    else:
                        prin(new_client_socket,(' \x1B[1;3;31mERROR: ' + cdata.decode('utf-8') + '\x1B[0m\r\n').encode("utf-8"))
                        fs.close()
                        break
    fsw.close()
    fs.close()
    
    #prin(new_client_socket,b"end\a\r\nexit")
