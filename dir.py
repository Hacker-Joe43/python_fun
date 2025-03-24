import os

PATH = "/"

filecount = 0
dircount = 0

for root, dirs,files,in os.walk(PATH):
    print("Looking in:",root)
    for directories in dirs:
        dircount += 1
    for files in files:
        filecount += 1

print("Number of files",filecount)
print("Number of Directories",dircount)
print("Total:",(dircount + filecount))