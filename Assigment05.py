# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Coco,2.11.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

file = open(objFile,"w")            # Open a new file because no file exists.
dicRow = {"Task":"Taxes","Priority":"High"}         # Create a dictionary to start with
lstTable = [dicRow]         # Put the dictionary into lstTable
for dicRow in lstTable:
    file.write(dicRow["Task"]+","+dicRow["Priority"]+"\n")          # Save the dictionary to File
file.close()            # Close the file


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Task"+"\t"+"Priority")           # Print Header
        f = open(objFile, "r")          # Open the file in read mode
        for dicRow in lstTable:
            print(dicRow["Task"],",", dicRow["Priority"])           # Loop thru lstTable and print the Values
            f.close()           # Close the file
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        newRow = {}         # A variable for a new dictionary
        newRow["Task"] = input("Please enter a Task: ")         # Prompt user to enter a new task
        newRow["Priority"] = input("Please enter a Priority: ")         # Prompt user to enter a priority
        lstTable.append(newRow)         # Add the new row (dictionary) to the list
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        lstTable.pop()      # remove the last item
        print("The new item has been removed.")     # Notify user new item was removed
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        f = open(objFile, "w")      # Open the file in write mode
        for i in lstTable:      # loop through lstTable
            f.write(i["Task"]+","+i["Priority"]+"\n")   # get the values for Task and Priority and write to file
        f.close()       # close the file
        print("Data saved to File!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program.


input("\n\nPress the enter key to exit.")       # Option 5 breaks the loop and allows the user to exit.