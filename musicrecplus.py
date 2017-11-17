"""
Created on Nov 13 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw10
"""

from pathlib import Path

database = {}
myName = ""


def isPrivate(s):
    return s[-1] == '$'


def writeFile(path):
    my_file = Path(path)
    if my_file.is_file():
        file = open(my_file, "w+")
        writeRawData(file)
        file.close()
        return True
    file = open(my_file, "w+")
    file.close()
    return False


def writeRawData(file):
    for user in database:
        print(user)
        artists = ""
        for artist in sorted(database[user]):
            artists += artist + ","
        artists = artists[:-1]
        print("writen: ", artists)
        file.write(user + ":" + artists + "\n")


def parseRawData(dat):
    ret = {}
    for line in dat.read().splitlines():
        fullName, artists = line.split(':')
        artistList = artists.split(',')
        ret[fullName] = sorted(artistList)
        print(ret)
        print("parse------")
    return ret


def readFile(path):
    """read from musicrecolus.txt"""
    global database
    my_file = Path(path)
    if my_file.is_file():
        file = open(my_file, "r")
        database = parseRawData(file)
        file.close()
        return True
    file = open(my_file, "w+")
    file.close()
    return False


def checkName():
    global myName
    while myName == "":
        myName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if myName not in database:
        database[myName] = []
        print("changed database:")
        print(database)
        return False
    return True


def setPreferences():
    global myName, database
    newArtist = []
    while True:
        artist = input("Enter an artist that you like (Enter to finish):")
        if artist != "":
            newArtist.append(artist)
            print("new artists: ", newArtist)
        else:
            break
    if myName != "":

        database[myName] = sorted(list(set(newArtist)))


def printMenu():
    print("""Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit""")

def printUsersWithMostLikes():
    ret = []
    maxNum = 0
    for key in database:
        if not isPrivate(key):
            numOfArtists = len(database[key])
            print("iterating: ", key, numOfArtists)
            if numOfArtists >= maxNum:
                if numOfArtists > maxNum:
                    ret.clear()
                ret.append(key)
                maxNum = numOfArtists

    if maxNum == 0:
        print("Sorry, no user found")
    else:
        for usr in sorted(ret):
            print(usr)


def isSimilar(usr, other):
    i = 0
    for artist in usr:
        if artist in other:
            i +=1
    if i >= 2 and i != len(usr) and i != len(other):
        return True
    else:
        return False


def printRecommendations():
    artists = []
    recArtists = []
    for usr in database:
        if isSimilar(database[myName], database[usr]) and not isPrivate(usr):
            artists += database[usr]
    for x in artists:
        if x not in database[myName]:
            recArtists.append(x)
    if recArtists != []:
        for artist in sorted(list(set(recArtists))):
            print(artist)
    else:
        print("No recommendations available at this time")


def getMostPopularArtist():
    global database
    allPreferences = []
    for usr in database:
        allPreferences += database[usr]
    allPreferences = sorted(allPreferences)

    artistRanking = {} # name : likes
    currentArtist = ""
    for artist in allPreferences:
        if artist != currentArtist:
            currentArtist = artist
            artistRanking[artist] = 0
        artistRanking[artist] = artistRanking[artist] + 1
    print(artistRanking)

    hotList = []
    likes = 0
    for artist in artistRanking:
        print(hotList)
        if artistRanking[artist] > likes:
            hotList = [artist]
            likes = artistRanking[artist]
        elif artistRanking[artist] == likes:
            hotList.append(artist)
    print((likes, hotList))
    return (likes, hotList)


            




if __name__ == '__main__':
    readFile("musicrecplus.txt")
    if(not checkName()):
        setPreferences()

    while True:
        printMenu()
        c = input()
        if c == 'e':
            setPreferences()
        elif c == 'q':
            break
        elif c == 'm':
            printUsersWithMostLikes()
        elif c == 'd':
            print(database)
        elif c == 'r':
            printRecommendations()
        elif c == 'p':
            getMostPopularArtist()

    if(database != {}):
        writeFile("musicrecplus.txt")
