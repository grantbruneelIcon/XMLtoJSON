from pathlib import Path
import xml.etree.ElementTree as ElementTree

# From the user, ask for File Location until an Existing file is given
def getXMLfilesInput():
    while True:
        location = Path(input("File Location: "))
        if location.exists():
            print("File Found")
            return getXMLfiles(location)
        elif not location.exists():
            print("No File Exists, please try again")

def getXMLfiles(location):
    if location.is_dir():
        for file in location.iterdir():
            print(file.resolve())
    
    else:
        print(location.resolve())
    return "funzies"
    

def main():
    print(getXMLfilesInput())
    print("\nDone")

main()