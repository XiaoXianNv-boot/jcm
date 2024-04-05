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
            if len(os.listdir(dir)) == 0:
                os.rmdir(dir)
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
                    mvrun(new_client_socket,httpserver,sql,x[0].decode('utf-8') + indir + '/' + i,fsdata)
            else:
                httpserver.websockfsstr(new_client_socket,('f ' + x[1].decode('utf-8') + indir + '/' + i + '\t' + fsdata[1].decode('utf-8') + '\t' + i + '\r\n').encode("utf-8"))
                mvrun(new_client_socket,httpserver,sql,x[0].decode('utf-8') + indir + '/' + i,fsdata)

def mvrun(new_client_socket,httpserver,sql,indir,fsdata):
    size = os.stat(indir).st_size / 1024 / 1024 + 100
    outdir = ''
    for i in sql.catall(".config/filenocopy/outdir.db"):
        i = i.split(b'\t')
        outsize = get_free_space_mb(i[0].decode("utf-8"))
        if size < outsize:
            outdir = i
            break
    if outdir == '':
        httpserver.websockfsstr(new_client_socket,('b ' + '剩余空间不够' + '\r\n').encode("utf-8"))
    elif os.stat(indir).st_size == 0:
        httpserver.websockfsstr(new_client_socket,('b ' + '文件损坏' + '\r\n').encode("utf-8"))
    else:
        md5 = get_file_md5(new_client_socket,httpserver,sql,indir,"md5")
        dir = outdir[0] + b'/' + outdir[1] + b'/' + fsdata[1] + b'/' + fsdata[0]
        dir = dir.decode("utf-8")
        if not os.path.exists(dir):
            cpcp(new_client_socket,httpserver,sql,indir,outdir,fsdata)
        outmd5 = get_file_md5(new_client_socket,httpserver,sql,outdir[0].decode("utf-8") + '/' + outdir[1].decode("utf-8") + '/' + fsdata[1].decode("utf-8") + "/" + indir.split('/')[-1],"verify")
        if md5 == outmd5:
            data = {}
            if not os.path.exists(".config/filenocopy/data.db"):
                data["name"] = "name"
                data["dir"] = "dir"
                data["md5"] = "md5"
                data["diskname"] = "diskname"
                data["diakdir"] = "diakdir"
                sql.new(".config/filenocopy/data.db",data)
            data["name"] = fsdata[0].decode("utf-8")
            data["dir"] = fsdata[1].decode("utf-8")
            data["md5"] = outmd5
            data["diskname"] = outdir[1].decode("utf-8")
            data["diakdir"] = outdir[0].decode("utf-8")
            if sql.prin(".config/filenocopy/data.db",data):
                if sql.rmt(".config/filenocopy/temp.db",fsdata[0].decode("utf-8"),0):

                    os.remove(indir)
                    if os.path.exists(indir):
                        httpserver.websockfsstr(new_client_socket,("b " + "Delete old file ERROR" + '\r\n').encode("utf-8"))
                    else:
                        httpserver.websockfsstr(new_client_socket,("b " + "OK" + '\r\n').encode("utf-8"))
                else:
                    httpserver.websockfsstr(new_client_socket,("b " + "SQL Delet error" + '\r\n').encode("utf-8"))
            else:
                httpserver.websockfsstr(new_client_socket,("b " + "SQL write error" + '\r\n').encode("utf-8"))


def cpcp(new_client_socket,httpserver,sql,file,outdata,outdir):
    '''
    复制文件
    :param new_client_socket: socket
    :param httpserver: httpserver
    :param sql: sql
    :param file_name: 文件
    :param outdata: 目录
    :return: md5值
    '''
    #print()
    import time
    if os.path.exists(outdata[0].decode('utf-8') + "/" + outdata[1].decode('utf-8') + '/' + outdir[1].decode('utf-8') + '') == False:
        name = outdir[1].decode('utf-8').split('/')
        for nnnnnnn in name[1:]:
            if os.path.exists(outdata[0].decode('utf-8') + "/" + outdata[1].decode('utf-8') + '/' + name[0] + '') == False:
                os.mkdir(outdata[0].decode('utf-8') + "/" + outdata[1].decode('utf-8') + '/' + name[0] + '')
            name[0] = name[0] + '/' + nnnnnnn
        name = name[0]
        if os.path.exists(outdata[0].decode('utf-8') + "/" + outdata[1].decode('utf-8') + '/' + outdir[1].decode('utf-8') + '') == False:
            os.mkdir(outdata[0].decode('utf-8') + "/" + outdata[1].decode('utf-8') + '/' + outdir[1].decode('utf-8') + '')
    cpsize = 1024 * 1024 * 1
    size = os.stat(file).st_size
    wsize=0
    cptt = '--s '
    cpsd = 0
    cptemp = 0
    cptime = time.strftime("%S", time.localtime())
    ramall = ""
    if size < 1024:
        ramall = str(size)[:4] + "B" 
    elif size < (1024 * 1024):
        ramall = str(size / 1024)[:4] + "KB"
    elif size < (1024 * 1024 * 1024):
        ramall = str(size / 1024 / 1024)[:4] + "MB"
    elif size < (1024 * 1024 * 1024 * 1024):
        ramall = str(size / 1024 / 1024 / 1024)[:4] + "GB"
    #m = hashlib.md5()   #创建md5对象
    res = "cp " + ramall + ' <br>' 
    res = res + str(wsize) + ' / ' + str(size) + ' <br>'
    res = res + 'percent: {:.2%}'.format(wsize/size) + ' <br>'
    res = res + cptt
    cpsd += cptemp
    httpserver.websockfsstr(new_client_socket,("b " + res + '\r\n').encode("utf-8"))
    fsw = open(outdata[0].decode('utf-8') + "/" + outdata[1].decode('utf-8') + '/' + outdir[1].decode('utf-8') + '/' + file.split("/")[-1],'wb')
    with open(file,'rb') as fobj:
        while True:
            data = fobj.read(cpsize)
            wsize = wsize + len(data)
            cpsd += len(data)
            if cptime != time.strftime("%S", time.localtime()):
                cptime = time.strftime("%S", time.localtime())
                res = "cp " + ramall + ' <br>' 
                res = res + str(wsize) + ' / ' + str(size) + ' <br>'
                res = res + 'percent: {:.2%}'.format(wsize/size) + ' <br>'
                res = res + cptt
                if cpsd != 0:
                    cpss = (size - wsize) // cpsd
                else:
                    cpss = 0
                cpttk = len(cptt)
                if cpss < 60:
                    cptt = str(cpss)
                    cptt += 's '
                elif cpss < 3600:
                    cptt = str(cpss // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                else:
                    cptt = str(cpss // 3600)
                    cptt += 'h'
                    cptt += str((cpss % 3600) // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                if len(cptt) < cpttk:
                    cpttk = cpttk - len(cptt)
                else:
                    cpttk = 0
                if cpsd < 1024:
                    cpsdB = str(cpsd)[:6] + "B" 
                elif cpsd < (1024 * 1024):
                    cpsdB = str(cpsd / 1024)[:6] + "KB"
                elif cpsd < (1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024)[:6] + "MB"
                elif cpsd < (1024 * 1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024 / 1024)[:6] + "GB"
                cpsd = 0
                res += cpsdB
                res += '/s'
                cpttrun = cpttk
                while cpttrun != 0:
                    res += ' '
                    cpttrun = cpttrun - 1
                httpserver.websockfsstr(new_client_socket,("b " + res + '\r\n').encode("utf-8"))
            if not data:
                res = "cp " + ramall + ' <br>' 
                res = res + str(wsize) + ' / ' + str(size) + ' <br>'
                res = res + 'percent: {:.2%}'.format(wsize/size) + ' <br>'
                res = res + cptt
                if cpsd != 0:
                    cpss = (size - wsize) // cpsd
                else:
                    cpss = 0
                cpttk = len(cptt)
                if cpss < 60:
                    cptt = str(cpss)
                    cptt += 's '
                elif cpss < 3600:
                    cptt = str(cpss // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                else:
                    cptt = str(cpss // 3600)
                    cptt += 'h'
                    cptt += str((cpss % 3600) // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                if len(cptt) < cpttk:
                    cpttk = cpttk - len(cptt)
                else:
                    cpttk = 0
                if cpsd < 1024:
                    cpsdB = str(cpsd)[:6] + "B" 
                elif cpsd < (1024 * 1024):
                    cpsdB = str(cpsd / 1024)[:6] + "KB"
                elif cpsd < (1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024)[:6] + "MB"
                elif cpsd < (1024 * 1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024 / 1024)[:6] + "GB"
                cpsd = 0
                res += cpsdB
                res += '/s'
                cpttrun = cpttk
                while cpttrun != 0:
                    res += ' '
                    cpttrun = cpttrun - 1
                httpserver.websockfsstr(new_client_socket,("b " + res + '\r\n').encode("utf-8"))
                break
            #m.update(data)  #更新md5对象
            fsw.write(data)
    fsw.close()


def get_file_md5(new_client_socket,httpserver,sql,file_name,md5text):
    '''
    计算文件的md5
    :param new_client_socket: socket
    :param httpserver: httpserver
    :param sql: sql
    :param file_name: 文件
    :return: md5值
    '''
    import time
    import hashlib
    cpsize = 1024 * 1024 * 1
    size = os.stat(file_name).st_size
    wsize=0
    cptt = '--s '
    cpsd = 0
    cptemp = 0
    cptime = time.strftime("%S", time.localtime())
    ramall = ""
    if size < 1024:
        ramall = str(size)[:4] + "B" 
    elif size < (1024 * 1024):
        ramall = str(size / 1024)[:4] + "KB"
    elif size < (1024 * 1024 * 1024):
        ramall = str(size / 1024 / 1024)[:4] + "MB"
    elif size < (1024 * 1024 * 1024 * 1024):
        ramall = str(size / 1024 / 1024 / 1024)[:4] + "GB"
    m = hashlib.md5()   #创建md5对象
    res = md5text + " " + ramall + ' <br>' 
    res = res + str(wsize) + ' / ' + str(size) + ' <br>'
    res = res + 'percent: {:.2%}'.format(wsize/size) + ' <br>'
    res = res + cptt
    cpsd += cptemp
    httpserver.websockfsstr(new_client_socket,("b " + res + '\r\n').encode("utf-8"))
    with open(file_name,'rb') as fobj:
        while True:
            data = fobj.read(cpsize)
            wsize = wsize + len(data)
            cpsd += len(data)
            if cptime != time.strftime("%S", time.localtime()):
                cptime = time.strftime("%S", time.localtime())
                res = md5text + " " + ramall + ' <br>' 
                res = res + str(wsize) + ' / ' + str(size) + ' <br>'
                res = res + 'percent: {:.2%}'.format(wsize/size) + ' <br>'
                res = res + cptt
                if cpsd != 0:
                    cpss = (size - wsize) // cpsd
                else:
                    cpss = 0
                cpttk = len(cptt)
                if cpss < 60:
                    cptt = str(cpss)
                    cptt += 's '
                elif cpss < 3600:
                    cptt = str(cpss // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                else:
                    cptt = str(cpss // 3600)
                    cptt += 'h'
                    cptt += str((cpss % 3600) // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                if len(cptt) < cpttk:
                    cpttk = cpttk - len(cptt)
                else:
                    cpttk = 0
                if cpsd < 1024:
                    cpsdB = str(cpsd)[:6] + "B" 
                elif cpsd < (1024 * 1024):
                    cpsdB = str(cpsd / 1024)[:6] + "KB"
                elif cpsd < (1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024)[:6] + "MB"
                elif cpsd < (1024 * 1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024 / 1024)[:6] + "GB"
                cpsd = 0
                res += cpsdB
                res += '/s'
                cpttrun = cpttk
                while cpttrun != 0:
                    res += ' '
                    cpttrun = cpttrun - 1
                httpserver.websockfsstr(new_client_socket,("b " + res + '\r\n').encode("utf-8"))
            if not data:
                res = md5text + " " + ramall + ' <br>' 
                res = res + str(wsize) + ' / ' + str(size) + ' <br>'
                res = res + 'percent: {:.2%}'.format(wsize/size) + ' <br>'
                res = res + cptt
                if cpsd != 0:
                    cpss = (size - wsize) // cpsd
                else:
                    cpss = 0
                cpttk = len(cptt)
                if cpss < 60:
                    cptt = str(cpss)
                    cptt += 's '
                elif cpss < 3600:
                    cptt = str(cpss // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                else:
                    cptt = str(cpss // 3600)
                    cptt += 'h'
                    cptt += str((cpss % 3600) // 60)
                    cptt += 'm'
                    cptt += str(cpss % 60)
                    cptt += 's '
                if len(cptt) < cpttk:
                    cpttk = cpttk - len(cptt)
                else:
                    cpttk = 0
                if cpsd < 1024:
                    cpsdB = str(cpsd)[:6] + "B" 
                elif cpsd < (1024 * 1024):
                    cpsdB = str(cpsd / 1024)[:6] + "KB"
                elif cpsd < (1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024)[:6] + "MB"
                elif cpsd < (1024 * 1024 * 1024 * 1024):
                    cpsdB = str(cpsd / 1024 / 1024 / 1024)[:6] + "GB"
                cpsd = 0
                res += cpsdB
                res += '/s'
                cpttrun = cpttk
                while cpttrun != 0:
                    res += ' '
                    cpttrun = cpttrun - 1
                httpserver.websockfsstr(new_client_socket,("b " + res + '\r\n').encode("utf-8"))
                break
            m.update(data)  #更新md5对象
    return m.hexdigest()    #返回md5对象

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

    #data = httpserver.websockrx(new_client_socket)
    #data = httpserver.websockrx(new_client_socket)

    #httpserver.websockfsstr(new_client_socket,b'6')
    run(new_client_socket,httpserver,sql)

    httpserver.websockendstr(new_client_socket,b"END\r\n")
    
def get_free_space_mb(folder):
    import platform
    import ctypes
    import os
    """
    获取磁盘剩余空间
    :param folder: 磁盘路径 例如 D:\\
    :return: 剩余空间 单位 G
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize / 1024 / 1024
