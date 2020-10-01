import os

def main():
    directory = input("Enter the path to your file: ")
    filename = input("Enter filename (please include the file extension - ex: .txt): ")
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone_number = input("What is your phone number? ")
    if os.path.isdir(directory): # this checks if the path is indeed in the directory
        writeFile = open(os.path.join(directory,filename),'w') # creating and/or opening the file to write
        writeFile.write(name+", "+address+", "+phone_number+'\n') # this is the user's input, separated by comma
        writeFile.close() # the file will close after the writing is done
        
        print("File contents: ")
        readFile = open(os.path.join(directory,filename),'r') # reading the file for proof of storing
        for line in readFile:
            print(line) # if storing is successful, this should display the user's input
        readFile.close()
    else:
        if not os.path.exists(directory):
            os.makedirs(directory) # creates new file to the specified directory
            writeNewFile = open(os.path.join(directory,filename),'w') # writes to the new file in the specified directory
            writeNewFile.write(name+", "+address+", "+phone_number+'\n') # this is the user's input, separated by comma
            writeNewFile.close() # the file will close after the writing is done
        
        print("File contents: ")
        readNewFile = open(os.path.join(directory,filename),'r') # reading the file for proof of storing
        for line in readNewFile:
            print(line) # if storing is successful, this should display the user's input
        readNewFile.close() 
main()
