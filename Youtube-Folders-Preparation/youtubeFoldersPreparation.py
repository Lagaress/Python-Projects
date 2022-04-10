# Script to create the directories necessaries to edit a video by Jesus Lagares

# Import the necesaries libraries
import os # To execute system orders
import sys # To access to command line argumments
import shutil # To move the files

# Check if the user provide a name like first argumment
if len(sys.argv) > 1:
    # Start the program
    current_directoy = os.getcwd() # Get the current directory 
    carpeta_raiz = os.path.join(current_directoy , sys.argv[1] ) # The first parameter must be an str
    directory_list = [ 'Images' , 'Movs' , 'Music' , 'Sound' , 'Project' , 'Source' , 'Spam' , 'Stock' ]
    txt_list = [ 'Title' , 'Description' , 'Cards' , 'Keywords' ]
    source_folder = os.path.join(carpeta_raiz , "Source" ) # Path to the Source Folder

    # Check if the root folder exits
    if os.path.isdir( carpeta_raiz ): 
        print("La carpeta "+sys.argv[1]+" ya existe")

    else: 
        os.mkdir(carpeta_raiz) # Create the root directoy

    for directory in directory_list: # Go all over the directory_list
        subcarpeta = os.path.join(carpeta_raiz , directory) # Name all the subfolders
        # Check if the subfolder exists
        if os.path.isdir( subcarpeta ): 
            print("La carpeta "+directory+" ya existe")
        else: 
            os.mkdir(subcarpeta) # Create the subfolders

    # Moving the .mp4 files passing like argumments to the 'Source' folder
    for argument in range ( 2 , len(sys.argv) ):
        source_file_path = os.path.abspath(sys.argv[argument]) # Obtain the path of 
        final_file_path = str (source_folder)+"\\"+str(sys.argv[argument])
        shutil.move ( source_file_path , final_file_path)

    # Create all the .txt files necessaries for the Projec 
    for txt in txt_list: 
        file_name = os.path.join(carpeta_raiz , str(txt)+".txt") # Name all the subfolders
        # Handling with the creation of the file
        try:
            open( file_name , "x" )
        except: 
            print("El archivo "+file_name+" ya está creado") 

else:
    print("Error. You must provide a name to the root folder")