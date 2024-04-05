#!/bin/sh

case $1 in
boot)
    for i in {10..0}
    do
        echo -en "等待  $i 秒，按一个键继续 ... \r"
        sleep 1
    done
    echo  等待  0 秒，按一个键继续 ...;  
    python3 server/init.py
    ;;
esac