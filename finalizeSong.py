import os
import sys
import numpy as np
import shutil


def finalizeSong(fileRoot, oldFileName, fileLocation, newFileName, folderPath, songTags):
    dirRoot = os.getcwd() + "/"
    src_dir = fileRoot
    pathToFile = fileRoot.replace(dirRoot, '')
    print(pathToFile)

    newFileName = cleanFileName(newFileName)

    """ if not os.path.exists(dirRoot + "pathsToSongs.npy"):
        pathsToSongs = {"dirRoot": dirRoot}
        np.save(dirRoot + "pathsToSongs.npy", pathsToSongs)
    else:
        pathsToSongs = np.load(
            dirRoot + "pathsToSongs.npy", allow_pickle=True).item() """

    if folderPath == "finished":
        path = dirRoot + folderPath + "/" + \
            songTags["artist"] + "/" + songTags["album"]
        if not os.path.exists(path):
            os.makedirs(path)
        dst_dir = path
    else:
        if not os.path.exists(dirRoot + folderPath + "/"):
            os.makedirs(dirRoot + folderPath + "/")
        dst_dir = dirRoot + folderPath + "/"

        """ pathsToSongs[newFileName] = pathToFile
        np.save(dirRoot + "pathsToSongs.npy", pathsToSongs) """

    src_file = os.path.join(src_dir, oldFileName)
    shutil.copy(src_file, dst_dir)
    dst_file = os.path.join(dst_dir, oldFileName)
    new_dst_file_name = os.path.join(dst_dir, newFileName)

    try:
        os.rename(dst_file, new_dst_file_name)
    except Exception as e:
        if not os.path.exists(dirRoot + "/songIssues.txt"):
            f = open(dirRoot + "/songIssues.txt", "w")
        else:
            f = open(dirRoot + "/songIssues.txt", "a")
        #f.write("title = " + songTags[title] + "\n")
        #f.write("artist = " + songTags[artist] + "\n")
        f.write("destination file name - " + src_dir +
                "  ---  " + oldFileName + "\n")
        f.write("new file name" + new_dst_file_name)
        f.write("\n")

        print (newFileName + " - FAILED")
        print (e)
        print ("-----------------------------------------------------------")

    if folderPath == "cleaned":
        os.remove(src_file)


def cleanFileName(newFileName):
    newFileName = newFileName.replace('"', '')
    newFileName = newFileName.replace('|', '--')
    newFileName = newFileName.replace('?', '')
    newFileName = newFileName.replace('*', '')
    newFileName = newFileName.replace('¿', '')
    newFileName = newFileName.replace(':', '')
    newFileName = newFileName.replace('~', '')
    newFileName = newFileName.replace('+', '')

    return newFileName
