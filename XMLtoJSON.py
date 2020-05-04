from pathlib import Path
import xml.etree.ElementTree as ET
import json

# From the user, ask for File Location until an Existing file is given
def getXMLfilesInput():
    print("Type \"Quit\" at to end the program")
    while True:
        user_input = input("File Location: ")
        location = Path(user_input)
        if location.exists():
            if (getXMLfiles(location)):
                return "Done"
            else:
                print("No XML file found at this location, try again or type \"Quit\" to exit")
        if user_input.lower() == "quit":
            return "Script quit"
        elif not location.exists():
            print("No File Exists, please try again")

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
    jsonfile = open(saveLocation, "w")
    diction = testsuits.attrib
    addChild(diction, testsuits)
    json.dump(diction, jsonfile)
    jsonfile.close()

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
    while True:
        location = input("Save file <" + file + "> as : ")
        if not location.endswith(".json"):
            print("JSON file must end with .json, please try again")
        try:
            open(location, "w")
            return location
        except:
            print("Invalid file Path, please try agian")
        


def main():
    print(getXMLfilesInput())

print(convert("PASSED_ETPF44920_83_309_2020_03_24_16_10.xml"))