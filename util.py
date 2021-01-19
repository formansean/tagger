import os
import sys
import shutil


def getDirToRun():
    dirs = {}
    dirCounter = 1
    dirCounterDisplay = 1
    for x in os.listdir(os.getcwd()):
        if os.path.isdir(x):
            if x != "finished" and x != ".git":
                dirs[dirCounter] = x
                dirCounter = dirCounter + 1
    clearScreen()
    while dirCounter > 1:
        print (str(dirCounterDisplay) + ": " + dirs[dirCounterDisplay])
        dirCounterDisplay = dirCounterDisplay + 1
        dirCounter = dirCounter - 1
    option = input("Press select a directory to use: ")
    try:
        return dirs[int(option)]
    except:
        clearScreen()
        print ("***Invalid choice***")
        time.sleep(3)
        active()


def getAllFiles(dirToUse):
    r = []
    subdirs = [x[0] for x in os.walk(os.getcwd() + "/" + dirToUse)]
    for subdir in subdirs:
        files = os.walk(subdir).__next__()[2]
        if (len(files) > 0):
            for file in files:
                r.append(subdir + "/" + file)

    return r


def clearScreen():
    try:
        os.system('clear')
        #clear = lambda: os.system('cls')
        # clear()
    except:
        pass
