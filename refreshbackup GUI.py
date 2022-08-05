
import os
import copyNewFiles as cnf
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

sourcepath = "O:\\"
backuppath = "H:\\BackupTest\\"


# eigenen Pfad herausfinden = Ziel-Gerät
backuppath  = os.path.dirname(os.path.abspath(__file__))
backuppath = os.path.join(backuppath, "O") # Backup im Unterordner O 
# if not os.path.isdir(backuppath):
#     print("Backup-Ordner wird angelegt")
#     os.mkdir(backuppath)
backuppath = "H:\\BackupTest\\"


def startbackup():
    print("go")
    # if len(textarea.get("1.0", tk.END))>0:
    #     l=len(textarea.get("1.0", tk.END))
    #     textarea.delete("1.0", l)

    if not os.path.isdir(backuppath):
        textarea.insert(tk.END,"Backup-Ordner wird angelegt")
        os.mkdir(backuppath)
    
    textarea.insert(tk.END, "### Aktualisierungen für gesicherte Dateien suchen ###\n")
    out, updatedfiles = cnf.copynewerfiles(backuppath, sourcepath)
    textarea.insert(tk.END, out)
    if debug:
        textarea.insert(tk.END, updatedfiles)
    textarea.insert(tk.END, "\n\n")


    # prüfe im Quellsystem auf neue Ordner, die im Backup noch nicht vorhanden sind
    textarea.insert(tk.END, "### Neue Ordner im Quellverzeichnis suchen ###\n")
    out, newdirs = cnf.scanfornewdirs(backuppath, sourcepath)
    textarea.insert(tk.END, out)
    if debug:
        textarea.insert(tk.END, newdirs)
    textarea.insert(tk.END, "\n\n")

    # prüfe auf neue Dateien im Quellsystem, die im Backup noch nicht vorhanden sind
    textarea.insert(tk.END, "### Neue Dateien im Quellverzeichnis suchen ###\n")
    out, newfiles = cnf.scanfornewfiles(backuppath, sourcepath)
    textarea.insert(tk.END, out)
    if debug:
        textarea.insert(tk.END, newfiles)
    textarea.insert(tk.END, "\n\n")


def toggledebug():
    pass

def choosesourcefolder():
    global sourcepath
    sourcepath = filedialog.askdirectory(initialdir = sourcepath, title = "Select the Source Directory")
    entry_source.delete(0, len(entry_source.get()))
    entry_source.insert(0,sourcepath)


def choosedestfolder():
    global backuppath
    backuppath = filedialog.askdirectory(initialdir = backuppath, title = "Select the Backup Directory")
    entry_dest.delete(0, len(entry_dest.get()))
    entry_dest.insert(0,backuppath)

window = tk.Tk()
window.title("Backup (Refresher)")

tk.Label(window, width=20, text="Quellpfad", bg="grey", fg="white").grid(row=0, column=0, sticky=tk.E)
entry_source = tk.Entry(window, width=40, bg="white", fg="black")
entry_source.grid(row=0, column=1, sticky=tk.EW)
entry_source.insert(0,sourcepath)
button_changesource = tk.Button(master=window, text='...', command=choosesourcefolder).grid(row=0, column=2, sticky=tk.W)

tk.Label(window, width=20, text="Backuppfad", bg="grey", fg="white").grid(row=1, column=0, sticky=tk.E)
entry_dest = tk.Entry(window, width=40, bg="white", fg="black")
entry_dest.grid(row=1, column=1, sticky=tk.EW)
entry_dest.insert(0,backuppath)
button_changedest = tk.Button(master=window, text='...', command=choosedestfolder).grid(row=1, column=2, sticky=tk.W)

button_backup = tk.Button(master=window, width=10, height=2,text='Backup', command=startbackup).grid(row=0, column=3, rowspan=2, sticky=tk.NS)

debug = tk.BooleanVar()
cb1 = tk.Checkbutton(window, text='Debug',variable=debug, onvalue=True, offvalue=False, command=toggledebug)
cb1.grid(row = 2, column=0, sticky=tk.N)

textarea = tk.Text(window, height=20, width=60, bg="black", fg="white")
textarea.grid(row=3, column=0, columnspan = 4, sticky=tk.N)


window.mainloop()


# # eigenen Pfad herausfinden = Ziel-Gerät
# backuppath  = os.path.dirname(os.path.abspath(__file__))
# backuppath = os.path.join(backuppath, "O") # Backup im Unterordner O 
# if not os.path.isdir(backuppath):
#     print("Backup-Ordner wird angelegt")
#     os.mkdir(backuppath)


# backuppath += "\\"

# # nur während der Ausführung aus Projektordner
# # targetprefix = "I:\\O\\"
# backuppath = "H:\\BackupTest\\"

# print("Backup-Ordner: " + backuppath)


# # prüfe alle vorhandenen Dateien auf Änderungen im Quellsystem
# files, updated, error = cnf.copynewerfiles(backuppath, sourcepath)
# #print(updated)

# # prüfe im Quellsystem auf neue Ordner, die im Backup noch nicht vorhanden sind
# dirs, newdirs = cnf.scanfornewdirs(backuppath, sourcepath)
# #print(newdirs)

# # prüfe auf neue Dateien im Quellsystem, die im Backup noch nicht vorhanden sind
# files, newfiles = cnf.scanfornewfiles(backuppath, sourcepath)
# #print(newfiles)