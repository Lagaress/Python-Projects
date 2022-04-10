# Import libraries
import PySimpleGUI as sg # To build the GUI
import logic as backend # 

# Choose the theme
sg.theme('Dark Grey 13') 

# Components of the layout
layout = [  [sg.Text('Do you want some advice?')],
            [sg.Button('Yes')],
            [sg.Button('Change Directory'), sg.Button('Close Chest')] ]

# Create the Windows
window = sg.Window('Advice Chest', layout , alpha_channel=.95 , element_justification='c', margins = (0 , 40) , size=(300 , 200))

# Call the function to create the file for persistence
databaseFile = backend.createFile()

# The default directory will be the first line of the file
newDirectory = databaseFile.readline()

# Process the events
while True: #  Run the program

    event, values = window.read() # Read all the window

    if event == 'Yes': # [Yes Button]

        # Control the no .jpg files on the directory (there's no advice on the chest)
        if (backend.numberOfFiles(newDirectory) <= 0):
            sg.popup("There's no advices in your chest.\nPlease change the Advice Chest directory", "Advice have to be .jpg" , title = "No advice inside the chest")

        else:
            # If no errors, execute the main
            backend.findRandomAdvice(newDirectory)

    elif event == 'Change Directory': # [Change Directory Button]
        newDirectorySelected = sg.popup_get_folder("In which directory is your Advice Chest?", title = "Changue Advice Chest Directory" , default_path = newDirectory) # The user selects a directory
        if ( newDirectorySelected is None ): # If press cancel we do nothing
            sg.popup("You do not change the Advice Chest directory" , title = "Selected Directory Not Changed")
        
        else: # If choose any directory
            sg.popup("Your Advice Chest is in:\n"+str(newDirectorySelected) , title = "Selected Directory Changed")
            backend.writeFile(databaseFile , newDirectorySelected) # Write on the file if a new directory if selected or not
            newDirectory = newDirectorySelected

    else : # if user closes window or clicks cancel

        break # Stop the program

# Finish the execution
databaseFile.close() # Close the file
window.close() # Close the window
