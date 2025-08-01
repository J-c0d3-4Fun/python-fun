import csv
import json
import os


def read_file(a):

    a.strip()
    ospath = os.path.expanduser(a)
    with open(ospath,"r") as file:
        fileList = []
        fileList.append(file)
        for i in fileList:
            if i == 0:
                return "list is empty!"
            # print(i.strip())
            test = list(map(str, i))
            return test
r = read_file("test.txt")
print(r)