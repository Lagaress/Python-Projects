# Import libraries
from PIL import Image # To show the image
import pathlib # Scroll through the files
import random # Generate the random number
import os # Do system instructions

# Function to get the script execution directory
def returnCurrentDirectory(): 
    return os.getcwd()

# Function to obtain the numbers of .jpg files (advice) in the argument directory
def numberOfFiles(actualDirectory):
    # Get the number of files in the same directory as the script
    fileCounter = 0

    for path in pathlib.Path(actualDirectory).iterdir(): # Scroll all files
        fileExtension = os.path.splitext(path)[1]
        if (fileExtension == '.jpg'): # Check if the extension verifies that is a .jpg file
            fileCounter += 1 

    return fileCounter 

# Function to create a file if it does not exists
def createFile():
    if ( os.path.exists("directoryRoute.txt") ): # If it exists
        f = open("directoryRoute.txt") # Only open it
    else: # If not
        f = open("directoryRoute.txt" , "w+") # Create
        writeFile(f , returnCurrentDirectory()) # And write the default directory as firt line
    return f 

# Function to write in a file for the directoryRoute
def writeFile(file , routeToWrite):
    with open (file.name , 'w') as fileToWrite:
        fileToWrite.write(routeToWrite)

# Main function to select a random advice
def findRandomAdvice(actualDirectory): 
    fileCounter = numberOfFiles(actualDirectory)

    # Get a random number between 1 and fileCounter 
    randomNumber = random.randint(1 , fileCounter)

    # We go through all the files stopping the loop in the randomNumber
    stopLoop = True 

    for path in pathlib.Path(actualDirectory).iterdir(): # Scroll all files
        if (stopLoop): # If the flag is true
            fileExtension = os.path.splitext(path)[1] # Extract the extension
            if (fileExtension == '.jpg'): # Verifies if is a .jpg file
                randomNumber -= 1  # Subtract 1
                if (randomNumber == 0): # When the counter is 0 implies that we're in the random advice
                    stopLoop = False # Stop all the comprobations
                    randomAdvice = path # Take the path of the random advice
    
    advice = Image.open(randomAdvice).show() # Open the Image with the viewer
