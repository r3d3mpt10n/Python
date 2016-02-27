#!/usr/bin/python3
"""
This script will create monthly backups of $HOME and delete backups older than 30 days.
"""
import tarfile
import os
import datetime

class BackUp(object):

    def __init__(self):

        now = datetime.datetime.now()
        date = str(now)
        BDIR = '/media/Storage/Server.Backup/home_backups/'  # ADD YOUR BACKUP DIRECTORY HERE BEFORE RUNNING
        DIR = '/home/shep/'  # ADD YOUR HOME DIR HERE BEFORE RUNNING
        BFILE = BDIR + 'Home.backup' + date + 'tar.bz2'

        delta = datetime.timedelta(30)
        now30 = now - delta
        self.check(BDIR, DIR, BFILE)



    def check(self, BDIR, DIR, BFILE):
        try:
            exists = os.path.isdir(BDIR)
            self.runBackup(BFILE, DIR)
        except OSError as e:
            print("'%s' Does not exist. This program will now exit\n "
                "Error is %s" % (BDIR, e))
        return(exists)




    def runBackup(self, BFILE, DIR):

        with tarfile.open(BFILE, 'w:bz2') as tar:
            tar.add(DIR, arcname=os.path.basename(DIR))
        self.removeOld()


    def removeOld(self, BDIR):
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


BackUp()

