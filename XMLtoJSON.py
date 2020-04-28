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
    testsuit = testsuits.getchildren()[0]
    jsonfile = open("sample.json", "w")
    jsonfile.write("{")
    jsonfile.writelines(json.dumps(testsuit.tag) + ":")
    jsonfile.writelines(json.dumps(testsuit.attrib))
    jsonfile.write("}")

    jsonfile.close()

def main():
    print(getXMLfilesInput())

print(convert("PASSED_ETPF44920_83_309_2020_03_24_16_10.xml"))