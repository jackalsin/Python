# removeDsStore.py
import os
def removeDsStore(path):
    if (os.path.isdir(path) == False):
        if (path.endswith(".DS_Store")):
            print("removing:", path)
            os.remove(path)
    else:
        # recursive case: it's a folder
        for filename in os.listdir(path):
            removeDsStore(path + "/" + filename)

print("Removing .DS_Store files")
removeDsStore("sampleFiles")
print("Done")