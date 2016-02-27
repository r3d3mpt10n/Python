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
        BDIR = input("Which directory would you like to backup too?\n ")
        DIR = input("Which directory would you like to create a backup of?\n ")
        BFILE = BDIR + "/Home.backup" + date + "tar.bz2"

        delta = datetime.timedelta(30)
        self.now30 = now - delta
        self.check(BDIR, DIR, BFILE)



    def check(self, BDIR, DIR, BFILE):
        try:
            exists = os.path.isdir(BDIR)
            self.runBackup(BFILE, DIR, BDIR)
        except OSError as e:
            print("'%s' Does not exist. This program will now exit\n "
                "Error is %s" % (BDIR, e))
        return(exists)




    def runBackup(self, BFILE, DIR, BDIR):

        with tarfile.open(BFILE, 'w:bz2') as tar:
            tar.add(DIR, arcname=os.path.basename(DIR))
        self.removeOld(BDIR)


    def removeOld(self, BDIR):
        for name in os.listdir(BDIR):
            fname = os.path.join(BDIR, name)
            if os.path.isfile(fname):
                t = os.path.getmtime(fname)
                dt = datetime.datetime.utcfromtimestamp(t)
                if dt <= self.now30:
                    print("Deleting %s" % (fname))
                # os.remove(fname)  # This is commented out while debugging.
                else:
                    print ("%s are not old enough to not be deleted" % (fname))


BackUp()

