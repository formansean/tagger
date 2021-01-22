from aidmatch import aidmatch
from databaseUtil import insertRecords, deleteRecords, getCollection
import time
from util import clearScreen


def aidScan():
    found = failed = count = 0
    toDelete = []
    successSongsDict = {}
    collectionDict = getCollection("songsWithIssues", "songs")
    for k, v in collectionDict.items():
        clearScreen()
        print("Scanning songs with tag issues via AcoustID....")
        print(str(count) + "/" + str(len(collectionDict)))
        print("found = " + str(found))
        print("failed = " + str(failed))
        try:
            aidInfo = aidmatch(v["fileLocation"])
            if aidInfo != "failed":
                print(str(aidInfo["title"]) + "----" + str(aidInfo["artist"]))
                songTags = {"title": aidInfo["title"], "artist": aidInfo["artist"],
                            "album": v["album"], "genre": v["genre"], "fileLocation": v["fileLocation"]}
                successSongsDict[v["fileLocation"]] = songTags
                toDelete.append(v["_id"])
                count = count + 1
                found = found + 1
            else:
                print("failed")
                count = count + 1
                failed = failed + 1
        except:
            pass

    insertRecords(successSongsDict, "songsWithTags", "songs")
    deleteRecords(toDelete, "songsWithIssues", "songs")
    #print("found = " + str(found))
    #print("failed = " + str(failed))
