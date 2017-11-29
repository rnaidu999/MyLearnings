from sys import argv
script, filename = argv

openfile_place=open(filename)
#print (openfile_place)
print (openfile_place.read())

#Enter file name
filename1=input("Enter File Name >>")
openfile_names=open(filename1)
readfile= openfile_names.read()
# Printing names
print (f"File Data Printed:\n",readfile)
