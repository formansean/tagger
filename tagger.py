import os
import sys
#import numpy as np
from passive import passive
from util import clearScreen


def selectMode():
    clearScreen()
    print ("**THIS PROGRAM MUST BE RAN IN THE SAME FOLDER WITH THE MP3S TO BE EDITED**")
    print ("**ALL MP3S WILL BE DELETED AFETR EDITING AND FILE NAMES WILL BE CHANGED**")
    print ("Current folder: " + "\"" + os.getcwd() + "\"")
    print ("")
    print ("Select mode:")
    print ("1.) Passive")
    print ("2.) Active")
    print ("3.) Upload to S3")
    option = input("Choose an option: ")
    if option == "1":
        passive()
    elif option == "2":
        active()
    else:
        print ("Invlaid Selection!")
        time.sleep(3)
        selectMode()


selectMode()
