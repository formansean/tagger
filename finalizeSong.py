import os
import sys
import numpy as np
import shutil


def finalizeSong(dirRoot, fileRoot, old_file_name, fileLocation, newFileName, folderPath, songTags):
    src_dir = fileRoot
    pathToFile = fileRoot.replace(dirRoot, '')

    newFileName = cleanFileName(newFileName)

    if not os.path.exists(dirRoot + "pathsToSongs.npy"):
        pathsToSongs = {"dirRoot": dirRoot}
        np.save(dirRoot + "pathsToSongs.npy", pathsToSongs)
    else:
        pathsToSongs = np.load(
            dirRoot + "pathsToSongs.npy", allow_pickle=True).item()

    if folderPath == "finished":
        if not os.path.exists(dirRoot + folderPath + "/" + pathToFile):
            os.makedirs(dirRoot + folderPath + "/" + pathToFile)
        dst_dir = dirRoot + folderPath + "/" + pathToFile
    else:
        if not os.path.exists(dirRoot + folderPath + "/"):
            os.makedirs(dirRoot + folderPath + "/")
        dst_dir = dirRoot + folderPath + "/"

        pathsToSongs[newFileName] = pathToFile
        np.save(dirRoot + "pathsToSongs.npy", pathsToSongs)

    src_file = os.path.join(src_dir, old_file_name)
    shutil.copy(src_file, dst_dir)
    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, newFileName)

    try:
        os.rename(dst_file, new_dst_file_name)
    except Exception as e:
        if not os.path.exists(dirRoot + "/songIssues.txt"):
            f = open(dirRoot + "/songIssues.txt", "w")
        else:
            f = open(dirRoot + "/songIssues.txt", "a")
        f.write("title = " + songTags[title] + "\n")
        f.write("artist = " + songTags[artist] + "\n")
        f.write("destination file name - " + src_dir +
                "  ---  " + old_file_name + "\n")
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
