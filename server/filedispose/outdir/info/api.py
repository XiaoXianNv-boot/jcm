# coding=utf-8
#!/bin/python

import imp
import os
import psutil

def main(new_client_socket,RUL_CS,post_data,Headers,info,user):
    httpserver = imp.load_source("server/main/httpserver.py","server/main/httpserver.py")
    sql = imp.load_source("server/main/filesql.py","server/main/filesql.py")

    json = ''
    fo = sql.catlen(".config/filenocopy/outdir.db")

    json += '{"fo":' + str(fo) + ',"data":['
    for i in sql.catall(".config/filenocopy/outdir.db"):
        i = i.split(b'\t')
        if os.path.exists(i[0].decode("utf-8")):
            size = get_free_space_mb(i[0].decode("utf-8"))
            if size > 10000:
                size = size / 1000
                size = str(size).split('.')
                if len(size) == 1:
                    size = size[0] + '.' +  "00G"
                else:
                    size = size[0] + '.' + size[1][:4] + "G"
            else:
                size = str(size).split('.')
                if len(size) == 1:
                    size = size[0] + '.' +  "00M"
                else:
                    size = size[0] + '.' + size[1][:4] + "M"
            disk = psutil.disk_usage(i[0].decode("utf-8")).total
            disk = disk / 1000
            disk = disk / 1000 
            if disk > 10000:
                disk = disk / 1000 
                disk = str(disk).split('.')
                if len(disk) == 1:
                    disk = disk[0] + '.' +  "00G"
                else:
                    disk = disk[0] + '.' + disk[1][:4] + "G"
            else:
                disk = str(disk).split('.')
                if len(disk) == 1:
                    disk = disk[0] + '.' +  "00M"
                else:
                    disk = disk[0] + '.' + disk[1][:4] + "M"
            if os.path.exists(i[0].decode("utf-8") + '/' + i[1].decode("utf-8") + '.db'):
                json += '{"dir":"' + i[0].decode("utf-8") + '","name":"' + i[1].decode("utf-8") +'","Size":"' + disk + ' / ' + size + '","status":"正常"},'
            else:
                json += '{"dir":"' + i[0].decode("utf-8") + '","name":"' + i[1].decode("utf-8") +'","Size":"' + disk + ' / ' + size + '","status":"数据库不见了"},'
        else:
            json += '{"dir":"' + i[0].decode("utf-8") + '","name":"' + i[1].decode("utf-8") +'","Size":"ERR","status":"No Dir"},'
    json += '{}]}'
    httpserver.httppostchar(new_client_socket,"200",json.encode('utf-8'),"application/json",Headers,info)

def get_free_space_mb(folder):
    import platform
    import ctypes
    import os
    """
    获取磁盘剩余空间
    :param folder: 磁盘路径 例如 D:\\
    :return: 剩余空间 单位 G
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize / 1024 / 1024