#!/usr/bin/python3
'''
@author Zhiwei Xin
@andrewID zxin
original creation date: September 14, 2016
last modification date: September 14, 2016 

This is the Prject 2 file, which is used to do text analysis
'''

import re


def main():
    noiseWords = readNoise("noise_words.txt")
    substitutions = readSubsitutions()
    oldPatchString = readPatch("oldPatch.txt", noiseWords, substitutions)
    newPatchString = readPatch("newPatch.txt", noiseWords, substitutions)
    print("Result of Activity 1: ")
    print(oldPatchString)
    print(newPatchString)
    oldUniquePatchList = removeDup(oldPatchString)
    newUniquePatchList = removeDup(newPatchString)
    print("Result of Activity 2: ")
    print(oldUniquePatchList)
    print(newUniquePatchList)


# remove the duplicate words in the string that split by space
def removeDup(patchString):
    items = patchString.split(" ")
    return list(set(items))


# read the file and use the noise words list to filter the noise words and substitute the misspellingwords to right
# words
def readPatch(fileName, noiseWords, substitutions):
    subFile = open(fileName, "r")
    resultList = list()

    for line in subFile.readlines():
        line.rstrip()
        words = re.findall(r'[\w]+', line.rstrip())
        for word in words:
            if word not in noiseWords:  # filter the noise words
                if word in substitutions:  # add substituted words
                    resultList.append(substitutions[word])
                else:
                    resultList.append(word)
    subFile.close()
    return " ".join(resultList)


# read the substations and return a directory: wrong to right
def readSubsitutions():
    subFile = open("common_misspellings.csv", "r")
    resultDir = {}
    # ignore the first line
    subFile.readline()
    for line in subFile.readlines():
        line.rstrip()
        words = line.rstrip().split(",")
        resultDir[words[0]] = words[1]
    subFile.close()
    return resultDir


# read noise word from the file named fileName, return a set of noise words.
# @param fileName the noise word file's name
# @return a set of noise words.
def readNoise(fileName):
    noiseFile = open(fileName, 'r')

    resultSet = set()

    for line in noiseFile.readlines():
        line.rstrip()
        for word in line.split("\\W+"):
            resultSet.add(word.rstrip())
    noiseFile.close()
    return resultSet


if __name__ == '__main__':
    main()
