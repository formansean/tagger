import pymongo
from bson import ObjectId
from credentials import mongoCredentials
from util import clearScreen


def insertRecords(dict, databaseName, collectionName):
    myclient = pymongo.MongoClient(mongoCredentials)
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    for k, v in dict.items():
        x = mycol.insert_one(v)


def getCollection(databaseName, collectionName):
    myclient = pymongo.MongoClient(mongoCredentials)
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    collectionDict = {}
    for x in mycol.find():
        songTags = {"title": x["title"], "artist": x["artist"],
                    "album": x["album"], "genre": x["genre"], "fileLocation": x["fileLocation"], "_id": x["_id"]}
        collectionDict[x["fileLocation"]] = songTags

    return collectionDict


def getSingleDocument(databaseName, collectionName, id):
    myclient = pymongo.MongoClient(mongoCredentials)
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    singleDocument = mycol.find_one({'_id': ObjectId(id)})
    return singleDocument


def deleteRecords(records, databaseName, collectionName):
    myclient = pymongo.MongoClient(mongoCredentials)
    mydb = myclient[databaseName]
    mycol = mydb[collectionName]
    for x in records:
        mycol.delete_one({'_id': ObjectId(x)})


""" def getSongIssues():
    myclient = pymongo.MongoClient(mongoCredentials)
    mydb = myclient["songsWithTags"]
    mycol = mydb["songs"]
    count = 0
    songsWithIssuesDict = {}
    for x in mycol.find():
        title = x["title"].strip().lower()
        artist = x["artist"].strip().lower()
        if title == "None" or title == "" or artist == "None" or artist == "":
            songTags = {"title": x["title"], "artist": x["artist"],
                        "album": x["album"], "genre": x["genre"], "fileLocation": x["fileLocation"]}
            songsWithIssuesDict[x["fileLocation"]] = songTags

            count = count + 1
    print(count)
    #insertRecords(songsWithIssuesDict, "songsWithIssues", "songs") """
