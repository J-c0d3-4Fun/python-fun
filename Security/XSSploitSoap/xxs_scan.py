import csv
import json
import os


def read_file(a):

    # Grab absolute path
    ospath = os.path.abspath(a)
    print("Trying to open:", ospath) # Debug
    with open(ospath,"r") as file:
        fileList = file.readlines()
        print(f"debugging fileList: {fileList}") # Debug
        if len(fileList) == 0:
            return "list is empty!" 
        else:
            for i in fileList:
            # Checks for if the file is empty
                print(i.strip( ))


r = read_file("/Users/jbrown/python-fun/Security/XSSploitSoap/test.txt")
print(r)