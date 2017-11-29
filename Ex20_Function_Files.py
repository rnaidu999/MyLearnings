from sys import argv
script, filename=argv

#Read line number
def file_read (filename):
    print("File Data\n",filename.read())

def rewind(filename):
    filename.seek(0)

#Read data line by line from file and print line number alond with data

def readline(linen,filename):
    for linen in range(linenumber):
        print(linen,filename.readline())
        line=linen + 1

CurrentFile=open(filename,'r')

#Reading each line from the file without passing linenumber count
def readlines(filename,count):
    line=filename.readline()
    if line:
        print (f"Line {count}:\t{line}")
        count = (count + 1)
        return readlines(filename,count)


#Funcation calling
file_read(CurrentFile)
rewind(CurrentFile)
linenumber=10
print ("Reading File by each Line\n")
readline(linenumber, CurrentFile)
count=0
rewind(CurrentFile)
readlines(CurrentFile,count)
