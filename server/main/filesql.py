# coding=utf-8
#!/bin/python

import imp
import os

def new(file,data):
    if os.path.exists(file) == False:
        fs = open(file,"wb")
        fs.write(b"filesql V1.0\r\n")
        for i in data:
            fs.write(data[i].encode('utf-8'))
            fs.write(b"\t")
        fs.write(b"\r\n")
        fs.close()

def catlen(file):
    if os.path.exists(file):
        fs = open(file,"rb")
        fsdata = fs.read()
        fsdata = fsdata.split(b'\r\n')
        lens = len(fsdata[2:])
        lens = lens - 1
        fs.close()
        return lens
    else:
        return 0
def catall(file):
    if os.path.exists(file):
        fs = open(file,"rb")
        fsdata = fs.read()
        fsdata = fsdata.split(b'\r\n')
        fs.close()
        return fsdata[2:-1]
    else:
        return b''
def cat(file,data,i):
    if os.path.exists(file):
        fs = open(file,"rb")
        fsdata = fs.read()
        fsdata = fsdata.split(b'\r\n')
        for x in fsdata[2:-1]:
            x = x.split(b'\t')
            try:
                if x[i] == data.encode('utf-8'):
                    return x
            except Exception as e:
                x = x
        return False
    else:
        return False

def prin(file,data):
    if os.path.exists(file):
        fs = open(file,"ab")
        for i in data:
            fs.write(data[i].encode('utf-8'))
            fs.write(b'\t')
        fs.write(b'\r\n')
        fs.close()
        return True
    else:
        return False
def rmt(file,name,i):
    if os.path.exists(file):
        fs = open(file,"rb")
        fsw = open(file + '.tmp',"wb")
        fsdata = fs.read()
        fsdata = fsdata.split(b'\r\n')
        fsw.write(fsdata[0])
        fsw.write(b'\r\n')
        fsw.write(fsdata[1])
        fsw.write(b'\r\n')
        for xx in fsdata[2:-1]:
            x = xx.split(b'\t')
            try:
                if x[i] != name.encode('utf-8'):
                    fsw.write(xx)
                    fsw.write(b'\r\n')
            except Exception as e:
                fsw.write(xx)
                fsw.write(b'\r\n')
        fs.close()
        fsw.close()
        os.remove(file)
        os.rename(file + ".tmp",file)
        return True
    else:
        return False
