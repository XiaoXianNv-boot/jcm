# coding=utf-8
#!/bin/python

import os
import sys
import imp

def mkdir(name):
    if os.path.exists(name) == False:
        os.mkdir(name)

print('pkg out V1.0')

#os.system("rm -rf .jcm/pkg/Packages")
os.system("rm -rfv .jcm/*/Packages")

path = os.listdir("./server")
for p in path:
    p = "server/" + p
    if os.path.isdir(p):
        if os.path.isfile(p + "/Package.py"):
            Package = ''
            name = ''
            Version = ''
            Depends = ''
            License = ''
            issued = 'pkg'
            Description = ''.split('\r')[0]
            shrun = os.popen("\"" + sys.executable + "\" " + p + "/Package.py prin")
            data = shrun.buffer.read().decode(encoding='utf8')
            datas = data.split('\n')
            for p in datas:
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
            os.system("rm -rf .out")
            os.mkdir(".out")
            os.mkdir(".out/server")
            os.mkdir(".out/web")
            os.mkdir('.out/web/Ace_Admin')
            runout = imp.load_source('run',"server/" + Package + "/Package.py")
            runout.out()
            os.system("tar czf .pkg.tar.xz .out")
            mkdir(".jcm")
            mkdir(".jcm/" + issued)
            os.system("mv .pkg.tar.xz .jcm/" + issued + "/" + Package + '_' + Version + '.pkg')
            print(Package + '_' + Version + '.pkg')

print( 'out Packages file....')
jcm = os.listdir(".jcm")
for i in jcm:
    path = os.listdir(".jcm/" + i)
    print( 'out ' + i)
    for p in path:
        #print('.')
        Package = ''
        name = ''
        Version = ''
        Depends = ''
        License = ''
        issued = 'pkg'
        os.system("rm -rf .out")
        os.mkdir(".out")
        os.system("tar xzf .jcm/" + i + "/" + p + " .out")
        shrun = os.popen("\"" + sys.executable + "\" .out/server/" + p.split('_')[0] + "/Package.py prin")
        data = shrun.buffer.read().decode(encoding='utf8')
        datas = data.split('\n')
        for p in datas:
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
        fs = open(".jcm/" + i + "/Packages","ab")
        fs.write(('Package:' + Package + '\n').encode("utf-8"))
        fs.write(('name:' + name + '\n').encode("utf-8"))
        fs.write(('Version:' + Version + '\n').encode("utf-8"))
        fs.write(('Depends:' + Depends + '\n').encode("utf-8"))
        fs.write(('License:' + License + '\n').encode("utf-8"))
        fs.write(('Description:' + Description + '\n\n').encode("utf-8"))
        fs.close()
        print(Package + '_' + Version + '.pkg')
print('end')

def rm(dir,name):
    path = os.listdir(dir)
    for p in path:
        if os.path.isdir(dir + p):
            if p == name:
                os.system("rm -rfv " + dir + name)
            else:
                rm(dir + p + '/',name)

rm('./','__pycache__')

print("out files .jcm/ ")
mkdir("lib")
mkdir("lib/pkg")
os.system("cp .jcm/pkg/* lib/pkg/")