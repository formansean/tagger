import os
import sys
from util import clearScreen
import numpy as np
import _pickle as pickle
from databaseUtil import insertRecords


def insertRecordsToDbFromDict():
    clearScreen()
    print("builidng database with scanned songs....")
    dirRoot = os.getcwd() + "/"
    allSongs = np.load(dirRoot + "allSongsDict.npy",
                       allow_pickle=True, encoding='latin1').item()
    failedSongsDict = {}
    successSongsDict = {}
    for k, v in allSongs.items():
        title = allSongs[k]["title"].strip()
        artist = allSongs[k]["artist"].strip()
        album = allSongs[k]["album"].strip()
        genre = allSongs[k]["genre"].strip()
        fileName = k
        songObj = {"title": title, "artist": artist,
                   "album": album, "genre": genre, "fileLocation": k}
        isGood = checkASCII(title, artist, album, genre)
        if isGood == True and title != "None" and title != "" and artist != "None" and artist != "":
            successSongsDict[k] = songObj
        else:
            failedSongsDict[k] = songObj
    insertRecords(successSongsDict, "songsWithTags", "songs")
    insertRecords(failedSongsDict, "songsWithIssues", "songs")
    # print(len(successSongsDict))
    # print(len(failedSongsDict))


def checkASCII(title, artist, album, genre):
    try:
        title.encode(encoding='utf-8').decode('ascii')
        artist.encode(encoding='utf-8').decode('ascii')
        album.encode(encoding='utf-8').decode('ascii')
        genre.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


""" def organize():
    clearScreen()
    dirRoot = os.getcwd() + "/"
    allSongs = np.load(dirRoot + "songsDict.npy",
                       allow_pickle=True, encoding='latin1').item()
    artists = []
    artistsDict = {}
    for k, v in allSongs.items():
        title = allSongs[k]["title"]
        artist = v["artist"].strip().lower()
        album = allSongs[k]["album"]
        genre = allSongs[k]["genre"]
        fileName = k
        isGood = checkASCII(artist)
        if isGood == True:
            if artist not in artists:
                artistsDict[artist] = 1
                artists.append(artist)
            else:
                artistsDict[artist] = artistsDict[artist] + 1
        else:
            failedSongsDict[k] = v

    print(len(successSongsDict))
    print(len(failedSongsDict)) """
