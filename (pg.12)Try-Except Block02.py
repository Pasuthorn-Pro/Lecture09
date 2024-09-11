#Get the file name
filename = input("Enter a filename: ")
try:
    #Open file
    infile = open(filename, "r")
    #Read contents in file
    contents = infile.read
    #Display contents
    print(contents)
    #Close file
    infile.close
except IOError:
    print("An error occured trying to read")
    print("the file", filename)

print("End program")