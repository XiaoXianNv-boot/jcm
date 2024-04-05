
@echo off

if /i '%1%' == 'boot' goto boot

:start
echo=
echo ******************************
echo=          菜单
echo     1: 开启服务
echo     0: 高级设置
echo     q: 退出

set /p a=请输入菜单编号
if /i '%a%' == '0' goto gaoji
if /i '%a%' == '1' goto run
if /i '%a%' == 'q' goto exit
goto exit

:gaoji
echo=
echo ******************************
echo         高级设置
echo     1: 设置Windows 免登录
echo     2: 修复Windows 10 免登录
echo     3: 设置PATH

set /p a=请输入菜单编号

if /i '%a%' == '1' Netplwiz
if /i '%a%' == '2' reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\PasswordLess\Device" /v "DevicePasswordLessBuildVersion" /t REG_DWORD /d 0x0000 /f
if /i '%a%' == '3' set PATH=%PATH%;%~dp0.bash\bin;%~dp0.python;%~dp0.python\Scripts;


goto start

:boot
goto run

:run
::set PATH=%PATH%;C:\Tools\.python;C:\Tools\.bash\bin
Tools\.python\python.exe server\jcm.py

:exit