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
os.system("rm -rf .jcm/*/Packages")

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
            os.mkdir(".out/language")
            os.mkdir(".out/language/server")
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
                os.system("rm -rf " + dir + name)
            else:
                rm(dir + p + '/',name)

rm('./','__pycache__')

print("out files .jcm/ ")

mkdir("jcm")
mkdir("jcm/pkg")
mkdir("jcm/install")
os.system("cp .jcm/pkg/* jcm/pkg/")

print("make Windows exe ...")
# apt install p7zip-full
# sudo dpkg --add-architecture i386 
# sudo mkdir -pm755 /etc/apt/keyrings
# sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
# Ubuntu 22.04	
# sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources
# Ubuntu 20.04
# Linux Mint 20.x
# sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/focal/winehq-focal.sources
# Ubuntu 18.04
# Linux Mint 19.x
# sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/bionic/winehq-bionic.sources
# Debian 12 Bookworm
# sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bookworm/winehq-bookworm.sources
# Debian 11 Bullseye
# sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bullseye/winehq-bullseye.sources

# sudo apt update
# sudo apt install --install-recommends winehq-stable



os.system("rm -rf .out")
os.mkdir(".out")
# #为注释,不执行此命令
os.system("cd .out \
    && 7z x ../lib/python-3.6.7.7z \
    && cd Tools/.python/  \
    && wine python.exe -m pip install pyinstaller \
    && wine python.exe -m pip install requests \
    && cp ../../../Tools/install.py ./ \
    && wine Scripts/pyinstaller.exe -F --hidden-import requests -c --uac-admin install.py \
    && cp dist/install.exe ../../../jcm/install/ ")
os.system("cp Tools/install.py jcm/install/")
os.system("cp Tools/install.sh jcm/install/")
os.system("cp language/Tools/install.py jcm/install/language -rf")
os.system("rm -rf .out")