#!/bin/bash

export gitdir=https://github.com/XiaoXianNv-boot/jcm/raw/master
export gitdir=https://github.com/XiaoXianNv-boot/jcm/releases/download/
export mirrordir=http://jiang144.i234.me/data/jcm
#export dir=https://github.com/XiaoXianNv-boot/jcm/releases/download/Preview
export dir=http://jiang144.i234.me/data/jcm

if [ ! -e /usr/bin/curl ]; then
    if [ -e /bin/apt ]; then
        apt update
        apt install -y curl
    else
        if [ -e /bin/yum ]; then
            yum install -y curl
        else
            if [ -e /sbin/apk ]; then
                apk add --no-cache curl
            else
                if [ -e /bin/opkg ]; then
                    opkg update
                    opkg install -y curl
                fi
            fi
        fi
    fi
fi
    if [ -e /bin/apt ]; then
        apt update
        apt install -y python3
        apt install -y python3-venv
        apt install -y python3-pip
    else
        if [ -e /bin/yum ]; then
            yum install -y python3
            yum install -y python3-venv
            yum install -y python3-pip
        else
            if [ -e /sbin/apk ]; then
                apk add --no-cache python3
                apk add --no-cache python3-venv
                apk add --no-cache python3-pip
            else
                if [ -e /bin/opkg ]; then
                    opkg update
                    opkg install python3
                    opkg install python3-venv
                    opkg install python3-pip
                    opkg install python3-dev
                fi
            fi
        fi
    fi


mkdir -p jcm_install
cd jcm_install

mkdir -p Tools
cd Tools
curl -#fL -o install.py -C - $gitdir/install/install.py
if [ ! -e install.py ]; then
    curl -#fL -o install.py -C - $mirrordir/install/install.py
fi
cd ..
mkdir -p lib
cd lib
mkdir -p pkg
cd pkg
#curl -#fL -o APP_V0.2.pkg -C - $dir/APP_V0.2.pkg
#curl -#fL -o main_V0.2.pkg -C - $dir/pkg/main_V0.2.pkg
cd ..
cd ..

python3 Tools/install.py %1 %2 %3 %4 %5
