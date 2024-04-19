

def soket(token):
    print(token)
    token = token.split("_")
    pair = "unix_socket:/run/jcm/qemu/vnc/" + token[1] + ".vnc"
    return pair.split(':')