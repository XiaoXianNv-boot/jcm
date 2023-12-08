# coding=utf-8
#!/bin/python

import os
import sys
import imp
import threading

def run(info,no):
    if os.path.exists("/tmp/jcm/frpc/logs") == False:
        print("boot frpc...")
        sh = imp.load_source("server/frpc/api/api.py","server/frpc/api/api.py")
        sh.run_shell_frpc(info,no)


def boot(info):
    if os.path.exists(".config/frpc/boot"):
        t = threading.Thread(target=run, args=(info,"no"))
        t.start()
        