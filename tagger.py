import os
import sys
# import numpy as np
from passive import passive
from util import clearScreen
from organize import insertRecordsToDbFromDict
from aidScan import aidScan
from lastFmScan import lastFmScan
import numpy as np
import os
import _pickle as pickle


def selectMode():
    clearScreen()
    print ("**THIS PROGRAM MUST BE RAN IN THE SAME FOLDER WITH THE MP3S TO BE EDITED**")
    print ("**ALL MP3S WILL BE DELETED AFETR EDITING AND FILE NAMES WILL BE CHANGED**")
    print ("Current folder: " + "\"" + os.getcwd() + "\"")
    print ("")
    print ("Select mode:")
    print ("1.) Passive")
    print ("2.) Show Dict")
    option = input("Choose an option: ")
    if option == "1":
        passive()
        insertRecordsToDbFromDict()
        aidScan()
        lastFmScan()
        aidScan()
        lastFmScan()
        clearScreen()
        print("All done!")
    elif option == "2":
        showDict()
    else:
        print ("Invlaid Selection!")
        time.sleep(3)
        selectMode()


def showDict():
    dirRoot = os.getcwd() + "/"
    pathsToSongs = np.load(dirRoot + "allSongsDict.npy",
                           allow_pickle=True, encoding='latin1').item()
    print(pathsToSongs)
    for k, v in pathsToSongs.items():
        title = v["title"]
        artist = v["artist"]
        album = v["album"]
        genre = v["genre"]
        fileName = k

        print("k = " + str(k))
        print("v = " + str(v))
        print(v["title"])


selectMode()
