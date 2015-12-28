#!/usr/bin/python3
## This script will create monthly backups of $HOME and delete backups older than 30 days.
##
import tarfile
import os
import datetime

now = datetime.datetime.now()
date = str(now)
BDIR = '<YOUR_BACKUP_DIR>' #ADD YOUR BACKUP DIRECTORY HERE BEFORE RUNNING
DIR = '<YOUR_HOME>' #ADD YOUR HOME DIR HERE BEFORE RUNNING
BFILE = BDIR + 'Home.backup'+ date + 'tar.bz2'

delta = datetime.timedelta(30)
now30 = now - delta

def check():
    if os.path.isdir(BDIR):
        exists = 'true'
        runBackup(exists, BFILE, DIR)
    else:
        exists = 'false'
        print(BDIR, 'Does not exist. This program will now exit')
        exit()
        
        
def runBackup(exists, BFILE, DIR):
    with tarfile.open(BFILE, 'w:bz2') as tar:
        tar.add(DIR, arcname=os.path.basename(DIR))
	removeOld()
    
def removeOld():
    for name in os.listdir(BDIR):
        fname = os.path.join(BDIR, name)
        if os.path.isfile(fname):
            t = os.path.getmtime(fname)
            dt = datetime.datetime.utcfromtimestamp(t)
            if dt <= now30:
                print('Deleting', repr(fname))
                # os.remove(fname)  # This is commented out while debugging.
            else:
                print (repr(fname), '  are not old enough to not be deleted')
    	



check()

