from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from Info import Info
import threading
import subprocess

class NeedUpdate(Tk):
    def __init__(self, version, path, RawKey):
        super().__init__()
        self._version = StringVar()
        self._percent = StringVar()
        self._speed = StringVar()
        self._version = StringVar()
        self._path = path + version
        self._RawKey = RawKey
        self._curVersion = int(RawKey.replace(version+'.', ""))        
        self.title("Updater ST 2.1")
        self.lblVersion = Label(self, textvariable=self._version, font="Arial 14").pack()
        self.lblPercent = Label(self, textvariable=self._percent, font="Arial 12").pack()
        self.lblNetSpeed = Label(self, textvariable=self._speed, font="Arial 7").pack()
        s = ttk.Style()
        s.theme_use('alt')
        s.configure("red.Horizontal.TProgressbar", foreground='blue', background='blue')
        #self.mpb = ttk.Progressbar(self, style="red.Horizontal.TProgressbar", orient ="horizontal",length = 200, mode ="determinate")
        #self.mpb.grid(row=1, column=2)
        #self.mpb["maximum"] = 100
        #self.mpb["value"] = self._progressPercent.get()
        #self.mpb.step(self._progressPercent.get())
        self.lblChange = Label(text="", font="Arial 7").pack()      
        #newInfo = Info("http://pg-build.pg.local","/guestAuth/app/rest/buildTypes/id:SecureTowerGit_StorageServer/builds/","6.0."+str(curVersion),"6.0."+str(NumberFolder)).GetInfo()

    def SetVersion(self, newValue):
        self._version.set("Install new version "+newValue)     
    def SetPercent(self, newValue):
        self._percent.set("Downloading "+str(newValue)+"%")
    def SetSpeed(self, newValue):
        self._speed.set('{:>4}'.format(round(newValue/1000, 2)))
    def lblChange(self, newValue):
        self._speed.set(newValue)
    def Quit(self):
        self.destroy()