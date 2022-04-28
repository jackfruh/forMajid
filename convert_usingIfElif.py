from pathlib import Path

def main():
    #welcome to our main function, we will do our main work here.

    #get the directory this script is working in
    workingdirectory = Path.cwd()

    #this directory will hold our input files:
    InputFilesDirectory = 'InputFiles'

    #here we define an empty array:
    newfilelist = []

    #here we get a list of files from the inputfiles directory
    #and go through this list and examine each filename for signs that it needs special processing.
    for file in workingdirectory.glob(InputFilesDirectory + '/*.txt'):
        ThisFileNeedsAllTranslations = True
        parts = file.stem.split("_")
        for part in parts:
            if part == "ToRu":
                ThisFileNeedsAllTranslations = False
                convertToRussian(file)

            if part == "ToCs":
                ThisFileNeedsAllTranslations = False
                convertToCzech(file)
            
            if part == "ToDe":
                ThisFileNeedsAllTranslations = False
                convertToGerman(file)
            

            if part == "ToNl":
                ThisFileNeedsAllTranslations = False
                convertToDutch(file)
            
            
            elif part == "ToEs":
                convertToSpanish(file)
                ThisFileNeedsAllTranslations = False
                
        if ThisFileNeedsAllTranslations:
            convertToAllLanguages(file)


#end main function

def convertToRussian(file):
    print("converting " + file.stem + " to Russian")
    #conversion logic here
    #create file.stem.mp3 in output directory

 def convertToCzech(file):
    print("converting " + file.stem + " to Czech")
    #conversion logic here
    #create file.stem.mp3 in output directory


def convertToGerman(file):
    print("converting " + file.stem + " to German")
    #conversion logic here
    #create file.stem.mp3 in output directory

def convertToDutch(file):
    print("converting " + file.stem + " to Dutch")
    #conversion logic here
    #create file.stem.mp3 in output directory
 
def convertToSpanish(file):
    print("converting " + file.stem + " to Spanish")
    #conversion logic here
    #create file.stem.mp3 in output directory

def convertToAllLanguages(file):
    print("well look here, we have a file that needs to be converted to ALL languages!")
    convertToRussian(file)
    convertToCzech(file)
    convertToGerman(file)
    convertToDutch(file)
    convertToSpanish(file)

main() #begin program by calling main function