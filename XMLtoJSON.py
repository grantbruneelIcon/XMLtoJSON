from pathlib import Path
import xml.etree.ElementTree as ET
import json
import platform

# From the user, ask for File Location until an Existing file is given
def getXMLfilesInput():
    print("Type \"Quit\" to end the program")
    while True:
        user_input = input("File Location: ")
        location = Path(user_input)
        if location.exists():
            if (getXMLfiles(location)):
                return True
            else:
                print("\nError, no json file saved, try again or type \"Quit\" to exit\n")
        if user_input.lower() == "quit":
            return False
        elif not location.exists():
            print("\nNo File Exists, please try again \n")

def getXMLfiles(location):
    if location.is_dir():
        xmlFound = False
        for file in location.iterdir():
            if getXMLfiles(file):
                xmlFound = True
        return xmlFound

    else:
        location = str(location.resolve())
        if  not location.endswith("xml"):
            return False
        else: # XML file is found here it is converted to a JSON file
            return convert(location)
            

def convert(file):
    tree = ET.parse(file)
    testsuits = tree.getroot()
    saveLocation = getValidSave(file)
    if saveLocation == False:
        return False
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
    
    
def getValidSave(file):
    if platform.system == "Windows":
        slash = "\\"
    else:
        slash = "/"
    print("\nType \"Quit\" to enter a XML file or \"Quit\" again to end the program\n")
    while True:
        location = input("Save file <" + file + "> in directory : ")
        jsonfile = Path(file).name
        jsonfile = jsonfile.replace("xml", "json")
        attempt = Path(location)
        if attempt.is_dir():
            return str(attempt.absolute()) + slash + jsonfile
        if location.lower() == "quit":
            return False
        else:
            print("\nInvalid file Path, please try agian. If you are trying to save to a new directory, please quit, create the directory, and try again\n")

        
                


def main():
    if getXMLfilesInput():
        print("\nFile successfully saved")
    else: 
        print("Program was quit")

main()