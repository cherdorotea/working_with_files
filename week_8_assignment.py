import os

def main():
    directory = input("Enter the path to your file: ")
    filename = input("Enter filename (please include the file extension - ex: .txt): ")
    if os.path.isdir(directory): # this checks if the path is indeed in the directory
        writeFile = open(os.path.join(directory,filename),'w') # creating and opening the file to write
        name = input("What is your name? ")
        address = input("What is your address? ")
        phone_number = input("What is your phone number? ")
        writeFile.write(name+", "+address+", "+phone_number+'\n') # this is the user's input, separated by a comma
        writeFile.close() # the file will close after the writing is done
        
        print("File contents: ")
        readFile = open(os.path.join(directory,filename),'r') # reading the file for proof of storing
        for line in readFile:
            print(line) # if storing is successful, this should display the user's input
        readFile.close()
    else:
        print("Sorry. Path not located. Please rerun this module and try again.")
main()
