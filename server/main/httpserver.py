# coding=utf-8
#!/bin/python

import socket
import hashlib
import time
import os
import base64
import threading

def websockrx(new_client_socket):
    data = '0'
    while data != "":
        data = new_client_socket.recv(8192)
        if data == b'':
            return "",2
        i = 0
        FIN = data[i] & 128 >> 7
        RSV = data[i] & 112 >> 5
        Opcode = data[i] & 15 >> 0
        if len(data) == 0:
            Opcode = 0
        i += 1
        Mask = data[i] & 128
        datalength = data[i] & 127 >> 0
        Maskingkey = ''
        datas = b''
        if Mask > 1:
            i += 1
            Maskingkey = data[i:i+4]
            for x in range(0,datalength):
                #datas = datas + b' '
                dddddd = hex(data[x + i + 4])
                ddddddd = hex(Maskingkey[x % 4])
                dddddddd = int(dddddd,16) ^ int(ddddddd,16)
                dddddddd = hex(dddddddd)
                dddddddd = dddddddd[2:]
                if len(dddddddd) == 1:
                    dddddddd = '0' + dddddddd
                ddddd = bytes.fromhex(dddddddd)
                datas = datas + ddddd
        #print(datas)
        if (Opcode == 1) | (Opcode == 2):
            ifdata = datas[0]
            #if (ifdata == 49):
            #    return websockjs(new_client_socket)
            if (datas[0] == 48) & (Opcode == 2):
                if datas[1] == b'\x03':
                    Opcode = 0
                return datas,Opcode
            if datas[0] == b'\x03':
                Opcode = 0
        return datas,Opcode
def websockfs(new_client_socket,data):
    data = b'' + data
    if len(data.decode("utf-8")) > 101:
        data = data.decode("utf-8")
        cd = 0
        while cd != len(data):
            if len(data) < (cd + 100):
                if cd == 0:
                    websockfs(new_client_socket,data[cd:cd + 100].encode("utf-8"))
                else:
                    websockfs(new_client_socket,b'0' + data[cd:cd + 100].encode("utf-8"))
                cd = len(data)
            else:
                if cd == 0:
                    websockfs(new_client_socket,data[cd:cd + 100].encode("utf-8"))
                else:
                    websockfs(new_client_socket,b'0' + data[cd:cd + 100].encode("utf-8"))
                cd = cd + 100
    else:
        datab = b'12'
        if len(data) < 126:
            datab = bytes.fromhex('82')
            len_ = hex(len(data))[2:]
            if len(len_) == 1:
                len_ = '0' + len_
            datab += bytes.fromhex(len_)
            new_client_socket.send(datab)
            new_client_socket.send(data)
def websockend(new_client_socket,data):
    #websockfs(new_client_socket,b'2{"d":"disableLeaveAlert"}')
    data = b'0' + data
    if len(data.decode("utf-8")) > 101:
        data = data.decode("utf-8")
        cd = 0
        while cd != len(data):
            websockfs(new_client_socket,data[cd:cd + 100].encode("utf-8"))
            if len(data) < (cd + 100):
                cd = len(data)
            else:
                cd = cd + 100
    else:
        datab = b'12'
        if len(data) < 126:
            datab = bytes.fromhex('82')
            #datab += bytes.fromhex('03')
            #datab += bytes.fromhex('30')
            #datab += bytes.fromhex('0D')
            #datab += bytes.fromhex('0A')
            len_ = hex(len(data))[2:]
            if len(len_) == 1:
                len_ = '0' + len_
            datab += bytes.fromhex(len_)
            new_client_socket.send(datab)
            new_client_socket.send(data)
            datab = bytes.fromhex('88')
            datab += bytes.fromhex('02')
            datab += bytes.fromhex('03')
            datab += bytes.fromhex('E8')
            new_client_socket.send(datab)
    time.sleep(0.05)
def websocktime(new_client_socket):
    datab = bytes.fromhex('89')
    datab += bytes.fromhex('00')
    new_client_socket.send(datab)
    time.sleep(0.2)
    return websockrx(new_client_socket)

def websockinit(new_client_socket,Headers,info):
    Sec_WebSocket_Magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    SecWebSocketAccept = ''

    SecWebSocketKey = ''
    SecWebSocketProtocol = ''
    SecWebSocketVersion = ''
    for h in Headers[1:]:
        hh = h.split(': ')
        if hh[0] == 'Sec-WebSocket-Key':
            SecWebSocketKey = hh[1]
        elif hh[0] == 'Sec-WebSocket-Protocol':
            SecWebSocketProtocol = hh[1]
        elif hh[0] == 'Sec-WebSocket-Version':
            SecWebSocketVersion = hh[1]

    sha1 = hashlib.sha1()
    sha1.update(SecWebSocketKey.encode("utf-8"))
    sha1.update(b'258EAFA5-E914-47DA-95CA-C5AB0DC85B11')
    SecWebSocketAccept = base64.b64encode(sha1.digest()).decode("utf-8")

    he = ""
    he = info["Headers"]
    he += "Upgrade: websocket\r\n"
    he += "Connection: Upgrade\r\n"
    he += "Sec-WebSocket-Accept: " + SecWebSocketAccept + "\r\n"
    if SecWebSocketProtocol != '':
        he += "Sec-Websocket-Protocol: " + SecWebSocketProtocol + "\r\n"
    he = he + '\r\n'
    he = "HTTP/1.1 101 Switching Protocols \r\n" + he
    new_client_socket.send(he.encode("utf-8"))
    if SecWebSocketProtocol != '':
        #time.sleep(0.5)
        websockfs(new_client_socket,b"2{ }")

def http_to_char(data):
    rul_ = data.split('%')
    for y in range(len(rul_)):
        if y == 0:
            data = rul_[y].encode("utf-8")
        elif y == (len(rul_)+1):
            y=y
        else:
            hex = rul_[y][:2]
            charb = bytes.fromhex(hex)
            data = data + charb
            if len(rul_[y]) > 2:
                data = data + rul_[y][2:].encode("utf-8")
    data = data.decode("utf-8")    
    return data

def session(name,session_):
    tmp4 = session_.split('\n')
    for y in range(len(tmp4)):
        tmp5 = tmp4[y].split(',')
        tmp3t = tmp3[1].split(';')
        if tmp3t[0] == tmp5[0]:
            user = tmp5[1]
    return ""

def catHeaders(data,Headers):
    for h in Headers:
        tmp2 = h.split(' ')
        if tmp2[0] == (data + ":"):
            return h[len(tmp2[0] + " "):]
    return ''

def catCookie(data,Headers,session_):
    res = ""
    for h in Headers:
        tmp2 = h.split(' ')
        if tmp2[0] == "Cookie:":
            for x in range(0,len(tmp2)):
                tmp3 = tmp2[x].split('=')
                if(tmp3[0] == data):
                    if session_ == '':
                        res = tmp3[1].split(';')[0]
                    else:
                        for s in session_:
                            if s.split(",")[0] == tmp3[1].split(';')[0]:
                                res = tmp3[1].split(';')[0]
    return res

def tcplink(sock, addr , logs, info,void):
    global run_
    new_client_socket = sock
    client_addr = addr
    RUL = ''
    HTTPMethod = ''
    Headers = ''
    recv_data=""
    post_data=b''

    # ���տͻ��˷��͹���������
    recv_tcp = new_client_socket.recv(8192)
    while True:
        if recv_tcp:
            l = recv_tcp.split(b'\r\n\r\n')
            l = len(l) 
            if recv_tcp[:4] == b'POST':
                if l > 1:
                    os.system("./error.sh '" + "POST" + "'")
                    recv_data = recv_tcp.split(b'\r\n\r\n')
                    Headers = recv_data[0].decode("utf-8")
                    Headers = Headers.split('\r\n')
                    os.system("./error.sh '" + catHeaders("Content-Type",Headers) + "'")
                    if catHeaders("Content-Type",Headers)[:len("application/x-www-form-urlencoded")] == "application/x-www-form-urlencoded":
                        os.system("./error.sh '" + catHeaders("Transfer-Encoding",Headers) + "'")
                        if catHeaders("Transfer-Encoding",Headers)[:len("Transfer-Encoding")] == "chunked":
                            recv_data = recv_tcp.split(b'\r\n\r\n')
                            haslen = len(recv_data[0]) + 4
                            post_data = recv_tcp[haslen:]
                            os.system("./info.sh '" + post_data.decode("utf-8") + "'")
                            os.system("./info.sh '" + recv_tcp.decode("utf-8") + "'")
                            if post_data[-5:] == b'0\r\n\r\n':
                                os.system("./error.sh '" + "ENDTO" + "'")
                                if os.path.exists("error.sh"):
                                    try:
                                        os.system("./error.sh '" + post_data.decode("utf-8") + "'")
                                    except Exception as e:
                                        print()

                                print(post_data)
                                post_data = post_data.split(b'\r\n')
                                print(post_data)
                                post_data = post_data[1]
                                if os.path.exists("error.sh"):
                                    try:
                                        os.system("./info.sh '" + post_data.decode("utf-8") + "'")
                                    except Exception as e:
                                        print()

                                break
                            recv_tcp += new_client_socket.recv(8192)
                        else:
                            recv_data = recv_tcp.split(b'\r\n\r\n')
                            haslen = len(recv_data[0]) + 4
                            post_data = recv_tcp[haslen:]
                            recv_data = recv_data[0].decode("utf-8")
                            Headers = recv_data.split('\r\n')
                            break
                    else:
                        recv_data = recv_tcp.split(b'\r\n\r\n')
                        haslen = len(recv_data[0]) + 4
                        post_data = recv_tcp[haslen:]
                        recv_data = recv_data[0].decode("utf-8")
                        Headers = recv_data.split('\r\n')
                        break


#36\r\n
#name=admin password=admin type=username checkbox=false
#\r\n0\r\n\r\n
                else:
                    recv_tcp += new_client_socket.recv(8192)
            else:
                if l > 1:
                    recv_data = recv_tcp.split(b'\r\n\r\n')
                    haslen = len(recv_data[0]) + 4
                    post_data = recv_tcp[haslen:]
                    recv_data = recv_data[0].decode("utf-8")
                    Headers = recv_data.split('\r\n')
                    break
                else:
                    #if recv_tcp == b'':
                        #print(str(client_addr) + " ???")
                        recv_tcp += new_client_socket.recv(8192)
                    #    if recv_tcp == b'':
                            #print(str(client_addr) + " ???")
                    #        return 0
        else:
            return 0
    
    
    RUL = ''
    RUL_CS = ''
    RUL = Headers[0].split(' ')[1].split('?')[0].split('#')[0]
    RUL_CS = Headers[0].split(' ')
    RUL_CS = RUL_CS[1].split('?')
    if len(RUL_CS) == 1:
        RUL_CS = ''
    else:
        RUL_CS = http_to_char(RUL_CS[1])
    pr = (time.strftime("I %Y-%m-%d %H:%M:%S ", time.localtime()).encode("utf-8"))
    pr += ((str(client_addr) + ' ' + '' + Headers[0].split(' ')[1]).encode("utf-8"))
    logs("info",info,pr + b"\r\n")
    data = void(new_client_socket,RUL,RUL_CS,post_data,Headers,logs,info)
    if data != 0:
        run_ = data
    new_client_socket.close()
    return data

def server(tcp_server_socket,info,logs,void):
    global run_
    run_ = 1
    while run_ > -1:
        try:
            print("start")
            while run_ > -1:
                sock = ''
                try:
                    sock, addr = tcp_server_socket.accept()
                    sock.settimeout(60)
                    if info['debug']:
                        run__ = tcplink(sock, addr , logs, info,void)
                        if run__ != 0:
                            run_ = run__
                    else:
                        t = threading.Thread(target=tcplink, args=(sock, addr , logs, info,void))
                        t.start()
                    #sock.close()
                except Exception as e:
                    if run_ == 9:
                        run_ = 16
                    if e.args[0] != "timed out":
                        sock.close()
                        logs("ERROR",info,e.args)
        except Exception as e:
            #print(e.args)
            logs("ERROR",info,e.args)
    sock.close()
    tcp_server_socket.close()
    return run_

def httppostfile(new_client_socket,ma,RUL,cache,Headers,info):
    byt = "",""
    he = ""
    ContentType = ""
    tmp2 = RUL.split(".")
    if os.path.isfile(RUL) == False:
        httppostchar(new_client_socket,"404",b"404","text/html;charset=UTF-8",Headers,info)
        return
    res = ""
    if tmp2[-1] == 'htm':
        ContentType = "Content-Type: text/html;charset=UTF-8\r\n"
        cache = False
    elif tmp2[-1] == 'html':
        ContentType = "Content-Type: text/html;charset=UTF-8\r\n"
        cache = False
    elif tmp2[-1] == 'css':
        ContentType = "Cache-Control: public, max-age=31536000\r\n"
        ContentType = "Content-Type: text/css;charset=UTF-8\r\n"
    elif tmp2[-1] == 'ico':
        ContentType = "Cache-Control: public, max-age=333135\r\n"
        ContentType = "Content-Type: image/x-icon\r\n"
    elif tmp2[-1] == 'js':
        ContentType = "Cache-Control: public\r\n"
        ContentType = "Content-Type: application/javascript;charset=UTF-8\r\n"
    elif tmp2[-1] == 'svg':
        ContentType = "Cache-Control: public, max-age=31536000\r\n"
        ContentType = "Content-Type: image/svg+xml\r\n"
    elif tmp2[-1] == 'woff2':
        ContentType = "Cache-Control: public, max-age=31536000\r\n"
        ContentType = "Content-Type: font/woff2\r\n"
    else:
        ContentType = "Content-Type: text/plain;charset=UTF-8\r\n"

    if ma != "200":
        cache = False
    fsdd = open(RUL, "rb")
    size = os.stat(RUL)
    if cache:
        for i in Headers:
            ii = i.split(":")
            if ii[0] == "Range":
                iii = ii[1].split("=")
                if iii[0] == ' bytes':
                    iiii = iii[1].split('-')
                    byt = iiii
    if byt[0] == '':
        he = info["Headers"]
        he += "Connection: close\r\n"
        he += "Accept-Ranges: bytes\r\n"
        he += "Content-Range: bytes 0-" + str(size.st_size) + "/" + str(size.st_size) + "\r\n"
        he += "Content-Length:" + str(size.st_size) + "\r\n"
        he = "HTTP/1.1 " + ma + " OK \r\n" + he
        new_client_socket.send(he.encode("utf-8"))
        he = ''
    elif byt[0] == "0":
        he = info["Headers"]
        #file_md5 = ""
        #with open(RUL, 'rb') as fp:
        #    file_md5= hashlib.md5(fp.read()).hexdigest()
        #he += "ETag: \"" + file_md5 + "\"\r\n"
        he += "Connection: close\r\n"
        he += "Accept-Ranges: bytes\r\n"
        he += "Content-Range: bytes 0-" + str(size.st_size) + "/" + str(size.st_size) + "\r\n"
        he += "Content-Length:" + str(size.st_size) + "\r\n"
        he = "HTTP/1.1 " + "206" + " OK \r\n" + he
        new_client_socket.send(he.encode("utf-8"))
        he = ''
    else:
        he = info["Headers"]
        file_md5 = ""
        with open(RUL, 'rb') as fp:
            file_md5= hashlib.md5(fp.read()).hexdigest()
        he += "ETag: \"" + file_md5 + "\"\r\n"
        he += "Connection: close\r\n"
        he += "Accept-Ranges: bytes\r\n"
        if byt[1] == "":
            he += "Content-Length:" + str(size.st_size - int(byt[0])) + "\r\n"
            he += "Content-Range: bytes " + byt[0] + "-" + str(size.st_size) + "/" + str(size.st_size) + "\r\n"
        else:
            he += "Content-Length:" + str(int(byt[1]) - int(byt[0]) - 1) + "\r\n"
            he += "Content-Range: bytes " + byt[0] + "-" + byt[1] + "/" + str(size.st_size) + "\r\n"
        he = "HTTP/1.1 " + ma + " OK \r\n" + he
        new_client_socket.send(he.encode("utf-8"))
        he = ""
    new_client_socket.send(ContentType.encode("utf-8"))
    new_client_socket.send("\r\n".encode("utf-8"))

    with open(RUL, 'rb') as fp:
        while True:
            data = fp.read(4096)
            if not data:
                break
            new_client_socket.send(data)


def httppostchar(new_client_socket,ma,data,ContentType,Headers,info):
    he = ''
    cd = str(len(data))
    he = info["Headers"]
    he += "Connection: close\r\n"
    he += "Accept-Ranges: bytes\r\n"
    he = he + 'Content-Length:' + cd + "\r\n"
    he += "Content-Type: " + ContentType + "\r\n"
    he = he + '\r\n'
    he = "HTTP/1.1 " + ma + " OK \r\n" + he
    new_client_socket.send(he.encode("utf-8"))
    new_client_socket.send(data)

def logsprnt(live,info,data):
    print(live)
    print(data)
def filedir(new_client_socket,RUL,RUL_CS,post_data,Headers,logs,info):
    RUL = os.getcwd() + RUL
    if os.path.isdir(RUL):
        dirn = os.listdir(RUL)
        dirn.sort(reverse=False)
        data = ""
        for d  in dirn:
            if os.path.isdir(RUL + d):
                d += "/"
            data += "<a href=\"" + d + "\">" + d + "</a><br>"
        httppostchar(new_client_socket,"200",data.encode("utf-8"),"text/html;charset=UTF-8",Headers,info)
    else:
        httppostfile(new_client_socket,"200",RUL,True,Headers,info)
    return 0

if  __name__ == "__name__":
    info = {}
    info["port"] = 88
    info['debug'] = False
    #info['debug'] = True
    info["Headers"] = "Server: httpserver/1.0\r\n"
    print("init http server")
    port = info["port"]
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a = 1
    while a < 10:
        try:
            tcp_server_socket.bind(("", port))
            a = 16
        except Exception as e:
            print(e.args)
            time.sleep(1)
    tcp_server_socket.listen(100)
    server(tcp_server_socket,info,logsprnt,filedir)

