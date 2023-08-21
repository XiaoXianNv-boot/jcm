#!/bin/sh

#apt install -y python3
#yum install -y python3
#opkg install -y python3

export dir=https://jiang144.i234.me/jcm/

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

if [ ! -f "/bin/python3" ]; then
	if [ -f "/bin/apt" ]; then
		apt install python3
	fi
	if [ -f "/bin/yum" ]; then
		yum install python3
	fi
	if [ -f "/bin/opkg" ]; then
        opkg update
		opkg install python3
	fi
fi

python3 Tools/install.py
