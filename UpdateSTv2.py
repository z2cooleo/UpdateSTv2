import sys


if __name__ == '__main__':
    
    from Info import Info
    try:
        RawKey = Info.GetCurrentVersion()
        isCurVerUpdate = False
    except:
            if(len(sys.argv) > 1):
                RawKey = sys.argv[1]+".1"
                isCurVerUpdate = True
            else:
                print("Приложение не установленно. Укажите желаемую версию. Пример 6.0")
                sys.exit(0)        
    verArray = RawKey.split('.')
    version = verArray[0]+"."+verArray[1]
    curVersion = int(RawKey.replace(version+'.', ""))    
    path = "\\\\192.168.1.206\\builds\\" + version    
    import os
    Folder, NumberFolder = Info.GetNumberFolder(os.listdir(path), version)
    if(isCurVerUpdate): 
        curVersion = int(NumberFolder)-1
        RawKey = verArray[0]+"."+verArray[1]+"."+str(curVersion)

    if(int(curVersion) < int(NumberFolder)):

        import subprocess
        from NeedUpdate import *
        app = NeedUpdate(version, path, RawKey)
        if(version == "6.0"): idVar = "SecureTowerGit_StorageServer"
        elif(version == "6.1"): idVar = "SecureTowerGit_Release61"
        elif(version == "6.2"): idVar = "SecureTowerGit_Develop"
        Info("http://pg-build.pg.local","/guestAuth/app/rest/buildTypes/id:"+idVar+"/builds/",version+"."+str(curVersion),version+"."+str(NumberFolder)).GetInfo()
        threading.Thread(target=Info.RunWork, args=(path, version, Folder, app)).start()        
        app.mainloop()
    else:
        print("Installed the latest version")
        import time
        time.sleep(5)
    print("\a")
