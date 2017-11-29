from sys import argv

script, filename=argv

openfile=open(filename,'w')
openfile.truncate()

table_number = int (input("\tEnter number to generate the table:"))

#write table in the notepad

for i in range (1,11):
    openfile.write(f"{table_number} * {i} = {table_number * i}\n")

#Closing file
openfile.close()

#Open file in read mode

#filename1=input ("Enter file name:")

openfile=open(filename,'r')
print (openfile.read())

#print (rowcount)
rowcount= len(openfile.readlines())
print (rowcount)
#Print table on console

#for j in range (1,rowcount):
#    print (j)
#    print (openfile.readlines(j))
rowcount=1
print (rowcount)
print (openfile.read())

#print (rowcount)
