from pathlib import Path
import xml.etree.ElementTree as ET
import json
import platform

# From the user, ask for File Location until an Existing file is given
def getXMLfilesInput():
    print("Type \"Quit\" to end the program")
    while True:
        user_input = input("XML File Location: ")
        location = Path(user_input)
        try:
            found = location.exists()
        except:
            found = False
        if found:
            if (getXMLfiles(location)):
                return True
            else:
                print("\nError, no xml file found, try again or type \"Quit\" to exit\n")
        if user_input.lower() == "quit":
            return False
        elif not found:
            print("\nNo File Exists, please try again \n")

def getXMLfiles(location, saveLocation=None):
    if saveLocation==None:
        saveLocation = getValidSave()
    if location.is_dir():
        xmlFound = False
        for file in location.iterdir():
            if getXMLfiles(file, saveLocation):
                xmlFound = True
        return xmlFound

    else:
        location = str(location.resolve())
        if  not location.endswith("xml"):
            return False
        else: # XML file is found here it is converted to a JSON file
            return convert(location, saveLocation)
            

def convert(file, saveLocation):
    tree = ET.parse(file)
    testsuits = tree.getroot()
    if saveLocation == False:
        return False
    saveFile = Path(file).name
    saveFile = saveFile.replace("xml", "json")
    saveLocation = saveLocation + saveFile
    jsonfile = open(saveLocation, "w")
    diction = testsuits.attrib
    addChild(diction, testsuits)
    json.dump(diction, jsonfile)
    jsonfile.close()
    return True

def addChild(dict, element):
    try:
        tag = list(element)[0].tag
        dict[tag] = []
        for child in list(element):
            dict[tag].append(child.attrib)
            length = len(dict[tag])
            addChild(dict[tag][length - 1], child)
    except:
        pass
    
    
def getValidSave():
    if platform.system == "Windows":
        slash = "\\"
    else:
        slash = "/"
    print("\nType \"Quit\" to enter a XML file or \"Quit\" again to end the program\n")
    while True:
        location = input("Folder in which to save JSON files: ")
        try:
            attempt = Path(location)
            if attempt.is_dir():
                return str(attempt.absolute()) + slash
            if location.lower() == "quit":
                return False
            else:
                print("\nLocation does not exist, Please try again")
        except:
            print("\nInvalid file Path, please try agian. If you are trying to save to a new directory, please quit, create the directory, and try again\n")

        
                


def main():
    if getXMLfilesInput():
        print("\nFile successfully saved")
    else: 
        print("Program was quit")

main()