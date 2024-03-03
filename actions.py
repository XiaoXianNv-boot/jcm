# coding=utf-8
#!/bin/python

import os
import sys
import imp
import urllib3
urllib3.disable_warnings()


os.system("sudo apt-get install -y python3-requests")

rul = "https://github.com/XiaoXianNv-boot/jcm/releases/download/"

def prin(new_client_socket,data):
    print(data.decode("utf-8"),end='')

def mkdir(name):
    if os.path.exists(name) == False:
        os.mkdir(name)

def Build_pkg(name):
    p = "server/" + name
    if os.path.isdir(p):
        if os.path.isfile(p + "/Package.py"):
            Package = ''
            name = ''
            Version = ''
            Depends = ''
            License = ''
            issued = 'pkg'
            Description = ''.split('\r')[0]

            pkg = imp.load_source('run',"" + p + "/Package.py")
            data = pkg.info()
            Package = data["Package"]
            name = data["names"]
            namei = data["namei"]
            Version = data["Version"]
            Depends = data["Depends"]
            License = data["License"]
            issued = data["issued"]
            Description = data["Description"]
            Descriptions = data["Descriptions"]

            os.system("rm -rf .out")
            os.mkdir(".out")
            os.mkdir(".out/language")
            os.mkdir(".out/language/server")
            os.mkdir(".out/server")
            os.mkdir(".out/web")
            os.mkdir('.out/web/Ace_Admin')
            pkg.out()
            os.system("tar czf .pkg.tar.xz .out")
            mkdir(".jcm")
            mkdir(".jcm/" + issued)
            os.system("mv .pkg.tar.xz .jcm/" + issued + "/" + Package + '_' + Version + '.pkg')
            print(Package + '_' + Version + '.pkg')


def progress_bar( nb_traits,name,d,prin,new_client_socket):
	prin(new_client_socket,('\r' + name + d + ' : Downloading [').encode("utf-8"))
	for i in range(0, nb_traits):
		if i == nb_traits - 1:
			prin(new_client_socket,'>'.encode("utf-8"))
		else:
			prin(new_client_socket,'='.encode("utf-8"))
	for i in range(0, 49 - nb_traits):
		prin(new_client_socket,' '.encode("utf-8"))
	prin(new_client_socket,']'.encode("utf-8"))

def down(rul,dir,d,prin,new_client_socket):
    import requests
    prin(new_client_socket,(dir.split('/')[-1] + d + ' : Downloading...').encode("utf-8"))
    
    bresp = requests.get(rul, stream=True, verify=False)
    if (bresp.status_code != 200): # When the layer is located at a custom URL
        if(bresp.status_code == 404):
            prin(new_client_socket,('\rERROR: Cannot download layer {} [HTTP {}]'.format(dir.split('/')[-1], bresp.status_code, "")).encode("utf-8"))
            prin(new_client_socket,(str(bresp.content)).encode("utf-8"))
            return
        bresp = requests.get(layer['urls'][0], headers=auth_head, stream=True, verify=False)
        if (bresp.status_code != 200):
            prin(new_client_socket,('\rERROR: Cannot download layer {} [HTTP {}]'.format(dir.split('/')[-1], bresp.status_code, bresp.headers['Content-Length'])).encode("utf-8"))
            prin(new_client_socket,(str(bresp.content)).encode("utf-8"))
            return
            #exit(1)
    # Stream download and follow the progress
    bresp.raise_for_status()
    unit = int(bresp.headers['Content-Length']) / 50
    acc = 0
    nb_traits = 0
    progress_bar( nb_traits,dir.split('/')[-1],d,prin,new_client_socket)
    with open(dir + ".downtmp", "wb") as file:
        for chunk in bresp.iter_content(chunk_size=8192): 
            if chunk:
                file.write(chunk)
                acc = acc + 8192
                if acc > unit:
                    nb_traits = nb_traits + 1
                    progress_bar( nb_traits,dir.split('/')[-1],d,prin,new_client_socket)
                    acc = 0
    prin(new_client_socket,("\r{}".format(dir.split('/')[-1]) + d + " : Extracting...{}".format(" "*50)).encode("utf-8")) # Ugly but works everywhere
    os.rename(dir + ".downtmp",dir)

    prin(new_client_socket,("\r{}".format(dir.split('/')[-1]) + d + " : Pull complete [{}]".format(bresp.headers['Content-Length'])).encode("utf-8"))


def download_all():
    print('download all ')
    os.system("mkdir -p .jcm")
    down(rul + "pkg/Packages",".jcm/pkg/Packages","\t",prin,"")
    print("")
    #os.system("wget https://github.com/XiaoXianNv-boot/jcm/releases/download/pkg/Packages -c -O .jcm/pkg/Packages")
    fs = open(".jcm/pkg/Packages","rb")
    fsdata = fs.read().split(b"\n\n")
    for da in fsdata[:-1]:
        da = da.split(b"\n")
        name = da[0].split(b":")[-1].decode("utf-8")
        name = name + "_" + da[2].split(b":")[-1].decode("utf-8") + ".pkg"
        down(rul + "pkg/" + name,".jcm/pkg/" + name,"\t",prin,"")
        print("")

    fsdata = fsdata
    fsdata = fsdata

print('pkg out V1.0')

#os.system("rm -rf .jcm/pkg/Packages")
os.system("rm -rf .jcm/*/Packages")

download_all()

path = os.listdir("./server")
for p in path:
    Build_pkg(p)

print( 'out Packages file....')
os.system("rm .jcm/pkg/Packages")
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

        pkg = imp.load_source('run',".out/server/" + p.split('_')[0] + "/Package.py")
        data = pkg.info()
        Package = data["Package"]
        name = data["names"]
        namei = data["namei"]
        Version = data["Version"]
        Depends = data["Depends"]
        License = data["License"]
        issued = data["issued"]
        Description = data["Description"]
        Descriptions = data["Descriptions"]

        #shrun = os.popen("\"" + sys.executable + "\" .out/server/" + p.split('_')[0] + "/Package.py prin")
        #data = shrun.buffer.read().decode(encoding='utf8')
        #datas = data.split('\n')
        
        #for p in datas:
        #    pp = p.split(':')
        #    if pp[0] == "Package":
        #        Package = pp[1].split('\r')[0]
        #    if pp[0] == "name":
        #        name = pp[1].split('\r')[0]
        #    if pp[0] == "Version":
        #        Version = pp[1].split('\r')[0]
        #    if pp[0] == "Depends":
        #        Depends = pp[1].split('\r')[0]
        #    if pp[0] == "License":
        #        License = pp[1].split('\r')[0]
        #    if pp[0] == "issued":
        #        issued = pp[1].split('\r')[0]
        #    if pp[0] == "Description":
        #        Description = pp[1].split('\r')[0]
        import hashlib
        md5 = ""
        with open(fr'.jcm/' + i + "/" + p, 'rb') as f:
            md5 = hashlib.md5(f.read()).hexdigest()
        
        fs = open(".jcm/" + i + "/Packages","ab")
        fs.write(('Package:' + Package + '\n').encode("utf-8"))
        fs.write(('name:' + name + '\n').encode("utf-8"))
        for key in namei:
            fs.write(('namei_' + key + ':').encode("utf-8") + namei[key] + '\n'.encode("utf-8"))
        fs.write(('Version:' + Version + '\n').encode("utf-8"))
        fs.write(('Depends:' + Depends + '\n').encode("utf-8"))
        fs.write(('License:' + License + '\n').encode("utf-8"))
        fs.write(('md5:' + md5 + '\n').encode("utf-8"))
        for key in Descriptions:
            fs.write(('Description_' + key + ':').encode("utf-8") + Descriptions[key] + '\n'.encode("utf-8"))
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