# coding=utf-8
#!/bin/python

import sys
import os

def newuser(name,password,int):
    import base64
    fs = open(".config/main/user","ab")
    fs.write(name + b':')
    fs.write(base64.b64encode(password) + b':')
    fs.write(int + b'\n')
    fs.close()

def ifuser(name,password):
    import base64
    text = 'error'
    ifuser = ""
    ifpass = ""
    try:
        fs = open(".config/main/user","rb")
        users = fs.read().decode("utf-8").split('\n')
        for useri in users:
            userii = useri.split(':')
            if userii[0] == name:
                ifuser = userii[0]
                ifpass = userii[1]
    except Exception as e:
            print(e.args)
    if name == ifuser:
        ifpass = base64.b64decode(ifpass)
        if ifpass == password.encode("utf-8"):
            text = 'yes'
    return text

def port():
    if len(sys.argv) == 2:
        if os.path.exists(".config/main/port"):
            fs = open(".config/main/port", "rb")
            ini = fs.read().decode("utf-8")
            print("port [" + ini + "]")
    elif len(sys.argv) == 3:
        if not os.path.exists(".config"):
            os.mkdir(".config")
        if not os.path.exists(".config/main"):
            os.mkdir(".config/main")
        fs = open(".config/main/port","w")
        fs.write(str(int(sys.argv[2])))
        fs.close
        print("set port [" + sys.argv[2] + "]")
    else:
        print("port [port]")

def help():
    print("port [port]")

if __name__ == "__main__":
    dir = sys.argv[0][:-14]
    os.chdir(dir)
    if len(sys.argv) == 1:
        sys.argv = (sys.argv[0]+" port 8889").split(' ')
    if sys.argv[1] == "help": 
        help()
    elif sys.argv[1] == "port": 
        port()