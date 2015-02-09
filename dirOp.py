import sys,os
import time

def ensure_dir(f):
        """
          ensure_dir(string) --> int
        ensure the dir with the specified name is present otherwise create one dir.
        on success return 0 on failure return 1.
        e.g. ensure_dir(string)
                1
        """
        ERROR = 0
        d = os.path.dirname(f)
        try:
                os.makedirs(d)
        except OSError:
                if os.path.isdir(d):
                        if os.path.isfile(f):
                                print "File with same name is present."
                                ERROR = 1
                        else:
                                print "Directory already present."
                else:
                        print "Directory can't be created."
                        ERROR = 1
                        raise
        return ERROR


def print_dir(dir):
        """
           print dir(string)  --> stdout
        print the files and folders present in a directory in case the direcory does not exists return NONE:
        """
        if os.path.isdir(dir):
                dirList = os.listdir(dir)
                for d in dirList:
                        d=dir+d
                        if os.path.isdir(d):
                                stat = os.stat(d)
                                created = os.stat(d).st_mtime
                                asciiTime = time.asctime(time.gmtime(created))
                                print d, "is a direcory (created ", asciiTime , ")"
                        else:
                                stat = os.stat(d)
                                created = os.stat(d).st_mtime
                                asciiTime = time.asctime(time.gmtime(created))
                                print d, "is a file (created ", asciiTime , ")"
        else :
                print "NONE"
