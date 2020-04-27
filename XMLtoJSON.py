from pathlib import Path
import xml.etree.ElementTree as ET

# From the user, ask for File Location until an Existing file is given
def getXMLfilesInput():
    print("Type \"Quit\" at to end the program")
    while True:
        user_input = input("File Location: ")
        location = Path(user_input)
        if location.exists():
            print("File Found")
            if (getXMLfiles(location)):
                return "Done"
            else:
                print("No XML file found at this location, try again or type \"Quit\" to exit")
        if user_input.lower() == "quit":
            return "Script Ended"
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
            print(location + " is not XML")
            return False
        else:
            print(location + " is XML")
            print(ET.parse(location))

            return True
    

def main():
    print(getXMLfilesInput())

main()