#!/usr/bin/python3

import tarfile
import os
import datetime

class BackUp(object):

    def __init__(self):
        """
        __init__ will define the variables to be used by the class. First by setting the directory to be backed up and defining time variables.
        """

        self.now = datetime.datetime.now()
        self.date = str(self.now)
        self.BDIR = input("Which directory would you like to backup too?\n ")
        self.DIR = input("Which directory would you like to create a backup of?\n ")
        self.BFILE = self.BDIR + "/Home.backup" + self.date + "tar.bz2"

        self.delta = datetime.timedelta(30)
        self.now30 = self.now - self.delta
        



    def check(self):
        """
        Check the directory exists
        """
        try:
            exists = os.path.isdir(self.BDIR)
        except OSError as e:
            print("'%s' Does not exist. This program will now exit\n "
                "Error is %s" % (self.BDIR, e))
        return(exists)




    def runBackup(self):

        """
        Creates a tar.bz2 file backup of the specified directory
        """
        with tarfile.open(self.BFILE, 'w:bz2') as tar:
            tar.add(self.DIR, arcname=os.path.basename(self.DIR))
        


    def removeOld(self):
        """
        Checks for old backup, removes backups older than 30 days
        """
        for name in os.listdir(self.BDIR):
            fname = os.path.join(self.BDIR, name)
            if os.path.isfile(fname):
                t = os.path.getmtime(fname)
                dt = datetime.datetime.utcfromtimestamp(t)
                if dt <= self.now30:
                    print("Deleting %s" % (fname))
                # os.remove(fname)  # This is commented out while debugging.
                else:
                    print ("%s are not old enough to not be deleted" % (fname))




new = BackUp()
print(new.check())