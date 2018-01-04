from pip._vendor import requests
from xml.etree import ElementTree
from winreg import *
import os
import subprocess
import sys
from datetime import datetime


class Info:
    def __init__(self, domainUrl, Url, oldVersion, newVersion):
        self.oldVersion = oldVersion
        self.newVersion = newVersion
        self.domainUrl = domainUrl
        self.url = Url

    def GetInfo(self):
        if "6.0" in self.oldVersion:
            listVer = Info.Request(self, self.domainUrl+self.url)
            for item in listVer:
                if str(item.get("number")) != str(self.oldVersion):
                    build = self.Request(self.domainUrl + item.get("href"))
                    changes = self.Request(self.domainUrl + build.find("changes").get("href"))
                    print("-----------" + item.get("number"))
                    for ch in changes:
                        comm = self.Request(self.domainUrl + ch.get("href"))
                        print(comm.find("comment").text)
                else:
                    return 1
    def Request(self, url):
        file = requests.get(url)
        tree = ElementTree.fromstring(file.content)
        return tree

    def GetTime():
        dt = datetime.now()
        return dt.microsecond

    def RunWork(path, version, Folder, Tk):
        lastVersion = str(version)+'.'+str(Folder)
        Tk.SetVersion(lastVersion)
        file = "FalcongazeSecureTowerSetup.exe"
        path = path +"\\"+ lastVersion + "\\" + file
        par = "/silent"
        src = path
        dst = "C:\\Windows\\Temp\\" + file
        source_size = os.stat(src).st_size
        copied = 0
        buffer = 32768
        source = open(src, 'rb')
        target = open(dst, 'wb')
        while True:
            t0 = Info.GetTime()
            chunk = source.read(buffer)
            target.write(chunk)
            copied += len(chunk) 
            t1 = Info.GetTime()
            Tk.SetPercent(int(round(copied * 100 / source_size)))            
            if (t1 - t0) == 0:
                t1 = t1 + 1
            x = t1 - t0
            #Tk.SetSpeed((1000*buffer)/x)
            if not chunk:
                source.close()
                target.close() 
                subprocess.call(dst+" "+par)
                os.remove(dst)
                Tk.Quit()

    def GetCurrentVersion():
        return QueryValueEx(OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\FalconGaze\SecureTower",0,KEY_READ), "ProductVersion")[0]

    def GetNumberFolder(folders, version): 
        NumberFolder=0
        folder=""
        for fld in folders:
            fld = str(fld)
            fld = fld.replace(version+'.', "")
            fldName = ""
            for char in fld:
                    if char.isnumeric():
                            fldName = fldName + char
            if(fldName.__str__() != '' and int(fldName) > int(NumberFolder)):
                    Folder = fld
                    NumberFolder = fldName

        print("In Rep: " + version + "." + str(NumberFolder))
        print()
        return Folder, NumberFolder

