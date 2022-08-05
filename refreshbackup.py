
import os
import copyNewFiles as cnf


sourcepath = 'O:\\'

# eigenen Pfad herausfinden = Ziel-Gerät
backuppath  = os.path.dirname(os.path.abspath(__file__))
backuppath = os.path.join(backuppath, "O") # Backup im Unterordner O 
if not os.path.isdir(backuppath):
    print("Backup-Ordner wird angelegt")
    os.mkdir(backuppath)


backuppath += "\\"

# nur während der Ausführung aus Projektordner
# targetprefix = "I:\\O\\"
backuppath = "H:\\BackupTest\\"

print("Backup-Ordner: " + backuppath)


# prüfe alle vorhandenen Dateien auf Änderungen im Quellsystem
print("\n### Aktualisierungen für gesicherte Dateien suchen ###")
out, updated = cnf.copynewerfiles(backuppath, sourcepath)
print(out)
print(updated)

# prüfe im Quellsystem auf neue Ordner, die im Backup noch nicht vorhanden sind
print("\n\n### Neue Verzeichnisse auf Quell-System suchen ###")
out, newdirs = cnf.scanfornewdirs(backuppath, sourcepath)
print(out)
print(newdirs)

# prüfe auf neue Dateien im Quellsystem, die im Backup noch nicht vorhanden sind
print("\n\n### Neue Dateien auf Quell-System suchen ###")
out, newfiles = cnf.scanfornewfiles(backuppath, sourcepath)
print(out)
print(newfiles)