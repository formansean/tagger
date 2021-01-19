from util import clearScreen, getDirToRun, getAllFiles
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from finalizeSong import finalizeSong
import os
import sys
import shutil


def passive():
    clearScreen()
    dirRoot = os.getcwd() + "/"
    dirToUse = getDirToRun()
    fileList = getAllFiles(dirToUse)
    for fileLocation in fileList:
        if fileLocation.endswith(".mp3"):
            fileName = fileLocation.rsplit('/', 1)[1]
            fileRoot = fileLocation.rsplit('/', 1)[0] + "/"
            mp3 = MP3File(fileLocation)

            title = "N/A"
            artist = "N/A"
            album = "N/A"
            genre = "N/A"

            try:
                tags = mp3.get_tags()
            except:
                if not os.path.exists(dirRoot + "/songIssues.txt"):
                    f = open(dirRoot + "/songIssues.txt", "w")
                else:
                    f = open(dirRoot + "/songIssues.txt", "a")
                f.write("tag error - " + fileLocation)
                f.write("\n")
            try:
                title = tags["ID3TagV2"]["song"]
                title = str(title)
            except:
                pass

            try:
                artist = tags["ID3TagV2"]["artist"]
                artist = str(artist)
            except:
                pass

            try:
                album = tags["ID3TagV2"]["album"]
                album = str(album)
            except:
                pass

            try:
                genre = tags["ID3TagV2"]["genre"]
                genre = str(genre)
            except:
                pass

            songTags = {"title": title, "artist": artist,
                        "album": album, "genre": genre}

            if title != "N/A" and artist != "N/A" and album != "N/A" and genre != "N/A":
                newFileName = artist + " - " + title + ".mp3"

                finalizeSong(dirRoot, fileRoot, fileName, fileLocation,
                             newFileName, "finished", songTags)
            else:
                newFileName = artist + " - " + title + ".mp3"
                finalizeSong(dirRoot, fileRoot, fileName, fileLocation,
                             fileName, "missing-tags", songTags)
        else:
            continue
