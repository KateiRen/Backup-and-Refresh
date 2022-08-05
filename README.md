# Backup-and-Refresh
 Creates a backup or copies new content

A simple python solution to keep a backup drive in sync with the source directory structure.


## Why?
I do not only want to catch up with new files in my source folder but also changes I made on some of them.
Therefore Windows "copy and skip exiting" was no option.
When updating my offline backup storage I always had to copy the entre content of my source system.

## How?
The solution comprises of three stages
- verify if any file already on the backup device has an updated counterpart in the source system and copy them over if any
- look for new directories in the source system and copy them over
- look for any new files on the source system not present onthe backup drive