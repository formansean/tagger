from util import clearScreen, getDirToRun, getAllFiles
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import numpy as np
import os
import sys
import shutil


def passive():
    clearScreen()
    print("Scanning for all MP3s....")
    dirRoot = os.getcwd() + "/"
    dirToUse = getDirToRun()
    fileList = getAllFiles(dirToUse)
    allSongs = {}
    for fileLocation in fileList:
        if fileLocation.endswith(".mp3"):
            fileName = fileLocation.rsplit('/', 1)[1]
            fileRoot = fileLocation.rsplit('/', 1)[0] + "/"
            mp3 = MP3File(fileLocation)

            try:
                tags = mp3.get_tags()
            except:
                if not os.path.exists(dirRoot + "/songIssues.txt"):
                    f = open(dirRoot + "/songIssues.txt", "w")
                else:
                    f = open(dirRoot + "/songIssues.txt", "a")
                f.write("tag error - " + fileLocation)
                f.write("\n")

            # get as much information about from the existing tags as possible
            title = getTagInfo("song", tags)
            artist = getTagInfo("artist", tags)
            album = getTagInfo("album", tags)
            genre = getTagInfo("genre", tags)

            songTags = {"title": title, "artist": artist,
                        "album": album, "genre": genre, "fileLocation": fileLocation}
            allSongs[fileLocation] = songTags
        else:
            continue

    np.save(dirRoot + "allSongsDict.npy", allSongs)


def getTagInfo(tagName, tags):
    tagInfo = "N/A"
    # attempt to first get V2 tags and use V1 tags as a fallback
    try:
        tagInfo = tags["ID3TagV2"][tagName]
    except:
        try:
            tagInfo = tags["ID3TagV1"][tagName]
        except:
            pass
    return str(tagInfo)
