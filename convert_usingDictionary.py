from pathlib import Path

def main():
    workingdirectory = Path.cwd()

    #here we define an empty array:
    newfilelist = []

    #languages is a python dictionary
    #left value is the abbreviation we have in our filesnames
    #right value is the function name in our code that handles that language
    languages = {
        'ToRu' : 'convertToRussian',
        'ToCs' : 'convertToCzech',
        'ToDe' : 'convertToGerman',
        'ToNl' : 'convertToDutch',
        'ToEs' : 'convertToSpanish'
    }

    #here we get a list of files from the inputfiles directory
    #and go through this list and examine each filename for signs that it needs special processing.
    for filename in workingdirectory.glob('InputFiles/*.txt'):
        
        #for each file we have, we don't yet know if we'll need all translations
        #so we will set this true for the file once here
        #and down below, if it becomes unnecessary, we will set it false below
        ThisFileNeedsAllTranslations = True

        #break the filename into it's pieces ie Catalog_ToRu becomes 2 pieces Catalog + ToRu
        parts = filename.stem.split("_")

        for part in parts:
            
            # here we compare the part we have 
            # (for example 'Catalog' or 'Ru" to our languages dictionary we defined above)
            # to what is in the dictionary
            if part in languages:
                # - if it's found (ie ToRu)
                # we use the globals() functon of python to call the function listed in the dictionary
                # ex: if 'part' = 'ToRu' then [languages[part]] will be set to the string 'convertToRussia' and the globals function will call the convertToRussia
                globals()[languages[part]](filename)

                #since we called a specific language, we assume this file doesn't need all translations:
                ThisFileNeedsAllTranslations = False
          
        if ThisFileNeedsAllTranslations:
            convertToLanguages(filename, languages)


#end main function

#Conversion functions
#could these be reduced to a single function with the language passed in?
#perhapse the langage codes used by the translator could be the abbreviated codes used in the file names?
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

def convertToLanguages(file,languages):
    print("well look here, we have a file that needs to be converted to ALL languages!")
    for languagefunction in languages.values():
        globals()[languagefunction](file)




main() #begin program by calling main function