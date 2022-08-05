#from dataclasses import replace
import os
import shutil

updatedfiles = []
files = []
readerror = []

dirs = []
newdirs = []

newfiles = []

def copynewerfiles(backuppath, sourcepath):
    global updatedfiles, files, readerror
    files = []
    readerror = []
    copynewerfiles_worker(backuppath, backuppath, sourcepath)
    return ("{0:d} Dateien gefunden und geprüft.\n{1:d} Neuere Dateien kopiert\n{2:d} Pfade ohne Zugriff".format(len(files), len(updatedfiles), len(readerror)), updatedfiles)



def copynewerfiles_worker(currentpath, backuppath, sourcepath):
    global updatedfiles, files, readerror
    try:
        dirfiles = os.listdir(currentpath)
    except: 
        print("Konnte Verzeichnis nicht lesen (" + currentpath + ")")
        readerror.append(currentpath)
    else:
        for item in dirfiles:
            itemfullpath = os.path.join(currentpath, item)
            
            if os.path.isfile(itemfullpath):
                files.append(itemfullpath)
                itemsourcepath = itemfullpath.replace(backuppath, sourcepath) 
                try:
                    if os.path.getmtime(itemsourcepath)>os.path.getmtime(itemfullpath):
                        print("neuere Version gefunden: {0}".format(itemsourcepath))
                        updatedfiles.append(itemsourcepath)
                        shutil.copy2(itemsourcepath, itemfullpath)
                except Exception as e:
                    print(e)
            if os.path.isdir(itemfullpath):
                copynewerfiles_worker(itemfullpath, backuppath, sourcepath)

def scanfornewdirs(backuppath, sourcepath):
    global dirs, newdirs
    dirs = []
    newdirs = []
    scanfornewdirs_worker(sourcepath, backuppath, sourcepath)
    return ("{0:d} Verzeichnisse wurden gefunden.\n{1:d} Neue Verzeichnisse wurden gefunden und kopiert".format(len(dirs), len(newdirs)), newdirs)

def scanfornewdirs_worker(currentpath, backuppath, sourcepath):
    global dirs, newdirs
    #print(currentpath)
    try:
        dirfiles = os.listdir(currentpath)
    except:
        print("Konnte Verzeichnis nicht lesen (" + currentpath + ")")
        #readerror.append(currentpath)
    else:
        for item in dirfiles:
            itemsourcepath = os.path.join(currentpath, item)
            if os.path.isdir(itemsourcepath):
                dirs.append(itemsourcepath)
                itembackuppath = itemsourcepath.replace(sourcepath, backuppath)
                if not os.path.isdir(itembackuppath):
                    newdirs.append(itemsourcepath)
                    try:
                        shutil.copytree(itemsourcepath, itembackuppath)
                        print("Copy from " + itemsourcepath + " TO " + itembackuppath)
                    except Exception as e:
                        print(e)
                else:
                    scanfornewdirs_worker(itemsourcepath, backuppath, sourcepath)

def scanfornewfiles(backuppath, sourcepath):
    global files, newfiles
    files = []
    newfiles = []
    scanfornewfiles_worker(sourcepath, backuppath, sourcepath)
    return ("{0:d} Dateien wurden gefunden.\n{1:d} Neue Dateien wurden gefunden und kopiert".format(len(files), len(newfiles)), newfiles)

def scanfornewfiles_worker(currentpath, backuppath, sourcepath):
    try:
        dirfiles = os.listdir(currentpath)
    except:
        print("Konnte Verzeichnis nicht lesen (" + currentpath + ")")
    else:
        for item in dirfiles:
            itemsourcepath = os.path.join(currentpath, item)
            if os.path.isfile(itemsourcepath) and item[0]!="$":
                files.append(itemsourcepath)
                itembackuppath = itemsourcepath.replace(sourcepath, backuppath)
                if not os.path.isfile(itembackuppath):
                    newfiles.append(itemsourcepath)
                    print("Neue Datei wird gesichert: {0}".format(itemsourcepath))
                    shutil.copy2(itemsourcepath, itembackuppath)
            if os.path.isdir(itemsourcepath):
                scanfornewfiles_worker(itemsourcepath, backuppath, sourcepath)


