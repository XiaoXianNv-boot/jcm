#!/bin/bash

export dir=https://jiang144.i234.me/jcm/

if [ ! -e /bin/curl ]; then
    if [ -e /bin/apt ]; then
        apt update
        apt install -y curl
    else
        if [ -e /bin/yum ]; then
            yum install -y curl
        else
            if [ -e /bin/opkg ]; then
                opkg update
                opkg install -y curl
            fi
        fi
    fi
fi
if [ ! -e /bin/python3 ]; then
    if [ -e /bin/apt ]; then
        apt update
        apt install -y python3
    else
        if [ -e /bin/yum ]; then
            yum install -y python3
        else
            if [ -e /bin/opkg ]; then
                opkg update
                opkg install python3
            fi
        fi
    fi
fi

mkdir -p jcm_install
cd jcm_install

mkdir -p Tools
cd Tools
curl -#fL -o install.py -C - $dir/Tools/install.py
cd ..
mkdir -p lib
cd lib
mkdir -p pkg
cd pkg
curl -#fL -o APP_V0.2.pkg -C - $dir/pkg/APP_V0.2.pkg
curl -#fL -o main_V0.2.pkg -C - $dir/pkg/main_V0.2.pkg
cd ..
cd ..

python3 Tools/install.py %1 %2 %3 %4 %5