#!/bin/bash
#上传前的清理

python3 pkg.py
rm -rf .out
rm -rf server/dom -rf
rm -rf web/Ace_Admin/dom
rm -rf .jcm/dom