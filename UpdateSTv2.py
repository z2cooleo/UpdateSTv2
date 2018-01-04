if __name__ == '__main__':

    print("Data gathering")
    version = "6.0"
    path = "\\\\192.168.1.206\\builds\\" + version

    from Info import Info
    RawKey = Info.GetCurrentVersion()
    curVersion = int(RawKey.replace(version+'.', ""))
    import os
    Folder, NumberFolder = Info.GetNumberFolder(os.listdir(path), version)
    

    if(int(curVersion) < int(NumberFolder)):

        import subprocess
        from NeedUpdate import *
        app = NeedUpdate(version, path, RawKey)
        Info("http://pg-build.pg.local","/guestAuth/app/rest/buildTypes/id:SecureTowerGit_StorageServer/builds/","6.0."+str(curVersion),"6.0."+str(NumberFolder)).GetInfo()
        threading.Thread(target=Info.RunWork, args=(path, version, Folder, app)).start()        
        app.mainloop()
    else:
        print("Installed the latest version")
        import time
        time.sleep(5)
    print("\a")
