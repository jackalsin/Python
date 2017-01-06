import os
def printFiles(path):
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so print its path
        print(path)
    else:
        # recursive case: it's a folder
        for filename in os.listdir(path):
            printFiles(path + os.sep + filename)

# To test this, download and expand this zip file in the same directory
# as the Python file you are running:  sampleFiles.zip
# Note: if you see .DS_Store files in the sampleFiles folders, or in the
# output of your function (as often happens with Macs, in particular),
# download removeDsStore.py, place it in the same directory, and run it,
# and you should see your .DS_Store files removed.

printFiles("sampleFiles")

import os
def listFiles(path):
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so return singleton list with its path
        return [path]
    else:
        # recursive case: it's a folder, return list of all paths
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + os.sep + filename)
        return files

# To test this, download and expand this zip file in the same directory
# as the Python file you are running:  sampleFiles.zip

print(listFiles("sampleFiles"))