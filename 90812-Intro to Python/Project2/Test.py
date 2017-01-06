from P2A1_Xin_Zhiwei import readNoise, readSubsitutions, readPatch


def testFiltNoiseWords():
    with open("noise_words.txt", 'r') as noiseReader:
        with open("allNoiseWords.txt", 'w') as noiseWriter:
            for line in noiseReader.readlines():
                noiseWriter.write(line)
    noiseWords = readNoise("noise_words.txt")
    substitutions = readSubsitutions()
    patchList = readPatch("allNoiseWords.txt", noiseWords, substitutions)
    newPathList = readPatch("newPatch.txt", noiseWords, substitutions)
    assert (len(patchList) == 0)
    assert (len(newPathList) != 0)
    print("testFiltNoiseWords passed")


def testStandFile():
    with open("common_misspellings.csv", "r") as commonFile:
        # create
        with open("test_python_miss.txt", 'w') as testMisspellingsWriter:
            for line in commonFile.readlines():
                words = line.split(",")
                testMisspellingsWriter.write(words[0] + "\n")
    misSpellSet = set()
    with open("test_python_miss.txt", "r") as testMisspellingsReader:
        for line in testMisspellingsReader.readlines():
            misSpellSet.add(line.rstrip())

    # test to make sure the words in misSpellSet not in the result
    resultPatchList = readPatch("oldPatch.txt", readNoise("noise_words.txt"), readSubsitutions())
    resultPatchSet = set(resultPatchList)

    for word in resultPatchSet:
        assert (word not in misSpellSet)
    print("test substitution successfully ")


# The main function to run test.
def main():
    testFiltNoiseWords()
    testStandFile()


if __name__ == '__main__':
    main()
