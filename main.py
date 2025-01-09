#--------------------------------------------------------------------------------------------------------------#
# Author: Asmaa Khan
# Touchstone 1
# This project is meant to help me collect and organize new patient information for my job at a medical clinic
#--------------------------------------------------------------------------------------------------------------#

# Variable declarations for managing the for loop
getNextLine = False
field = ''

# Open a text file containing new patient information
with open("newPatient.txt", "r") as file:
    for line in file: # Loop through every line in the file
        if(getNextLine == True): # If the last line we read is data we need then collect it
            print(field + ": " + line)
            getNextLine = False
            field = ''
            
        # If the current line contains the name, phone, or reason for visit information 
        # then set our variables to collect in the next loop
        if(line.strip().lower() == 'name'):
            field = line.strip() # We need to strip() to remove extra spaces in the string
            getNextLine = True
        if(line.strip().lower() == 'phone'):
            field = line.strip()
            getNextLine = True
        if(line.strip().lower() == 'reason for visit'):
            field = line.strip()
            getNextLine = True
