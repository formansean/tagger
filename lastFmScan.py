import requests
import os
import sys
import json
import time
from databaseUtil import getCollection, insertRecords, getSingleDocument, deleteRecords


def lastFmScan():
    os.system('clear')
    count = 0
    toDelete = []
    successSongsDict = {}
    failedSongsDict = {}
    working = 0
    failed = 0
    collectionDict = getCollection("songsWithTags", "songs")
    for k, v in collectionDict.items():
        time.sleep(.4)
        os.system('clear')
        print("Scanning songs for extra information via LastFM....")
        print(str(count) + "/" + str(len(collectionDict)))
        print("working = " + str(working))
        print("failed = " + str(failed))
        title = v['title'].replace('&', 'and')
        artist = v['artist'].replace('&', 'and')
        title = v['title'].replace('#', '')
        artist = v['artist'].replace('#', '')
        r = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=d360fe82a519832dbc725da8ed5f4a2f&artist=' +
                         artist + '&track=' + title + '&format=json')
        try:
            trackJson = r.json()
            if "track" in trackJson:
                working = working + 1
                count = count + 1
                songTags = {"title": v["title"], "artist": v["artist"],
                            "album": v["album"], "genre": v["genre"], "fileLocation": v["fileLocation"], "lastFmData": trackJson}
                successSongsDict[v["_id"]] = songTags
                toDelete.append(v["_id"])
            else:
                songTags = {"title": v["title"], "artist": v["artist"],
                            "album": v["album"], "genre": v["genre"], "fileLocation": v["fileLocation"]}
                failedSongsDict[v["_id"]] = songTags
                toDelete.append(v["_id"])
                failed = failed + 1
                count = count + 1
        except:
            failed = failed + 1
            count = count + 1
            pass
    insertRecords(successSongsDict, "lastFmScanned", "songs")
    insertRecords(failedSongsDict, "songsWithIssues", "songs")
    deleteRecords(toDelete, "songsWithTags2", "songs")
    os.system('clear')
    print("working = " + str(working))
    print("failed = " + str(failed))


def checkSingle():
    os.system('clear')
    s = getSingleDocument(
        "songsWithTags", "songs", "600934555861f8a0b06e47e5")
    r = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=d360fe82a519832dbc725da8ed5f4a2f&artist=' +
                     s['artist'] + '&track=' + s['title'] + '&format=json')
    trackJson = r.json()
    print(trackJson)
    if "track" in trackJson:
        songTags = {"title": s["title"], "artist": s["artist"],
                    "album": s["album"], "genre": s["genre"], "fileLocation": s["fileLocation"], "lastFmData": trackJson}
    else:
        print("boo")
