@echo off
echo The environment is loading
mkdir Tools\7z 
xcopy lib\7z\* Tools\7z\
mkdir Tools\.python
Tools\7z\7z.exe x lib\python.7z -r -aoa 
mkdir Tools\.bash
Tools\7z\7z.exe x lib\bash.zip -r -oTools\ -aoa 

Tools\.python\python.exe Tools\install.py