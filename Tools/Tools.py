


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