
@echo off

if /i '%1%' == 'boot' goto boot

:start
echo=
echo ******************************
echo=          �˵�
echo     1: ��������
echo     0: �߼�����
echo     q: �˳�

set /p a=������˵����
if /i '%a%' == '0' goto gaoji
if /i '%a%' == '1' goto run
if /i '%a%' == 'q' goto exit
goto exit

:gaoji
echo=
echo ******************************
echo         �߼�����
echo     1: ����Windows ���¼
echo     2: �޸�Windows 10 ���¼
echo     3: ����PATH

set /p a=������˵����

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