"""
Created on Nov 13 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw10
"""

from pathlib import Path

database = {}
myName = ""
firstOpen = True


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
        print(artists)
        file.write(user + ":" + artists)


def parseRawData(dat):
    ret = {}
    for line in dat.readlines():
        user = []
        fullName, artists = line.split(':')
        artistList = artists.split(',')
        # if any(c == '$' for c in fullName):
        #     fullName.replace('$', '')
        #     private = True
        # else:
        #     private = False
        ret[fullName] = [sorted(artistList)]
        print(ret)
        print("parse------")
    return ret


def readFile(path):
    """read from musicrecolus.txt"""
    my_file = Path(path)
    if my_file.is_file():
        file = open(my_file, "r")
        fileContent = parseRawData(file)
        file.close()
        return True
    file = open(my_file, "w+")
    file.close()
    return False


def setName():
    global myName
    myName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if myName not in database:
        database[myName] = []


def setPreferences():
    global myName, database
    while True:
        artist = input("Enter an artist that you like (Enter to finish):")
        if artist != "":
            database[myName].append(artist)
            print(database)
        else:
            break
    writeFile("musicrecplus.txt")


# def getRecommendation():


def printMenu():
    print("""Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit""")


if __name__ == '__main__':
    if(readFile("musicrecplus.txt")):
        firstOpen = False
        setName()

    else:
        setName()
        setPreferences()

    while True:
        printMenu()
        c = input()
        if c == 'e':
            setPreferences()
        elif c == 'q':
            break
    writeFile("musicrecplus.txt")
