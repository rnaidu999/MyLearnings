#Input for file names
from_file= input ("Enter Destination File Name:")
to_file=input ("Enter Srource File Name:")

#open source file in read mode and read data from the source file
from_file=open(from_file,'r')
from_file_data=from_file.read()

# Open destination file in write mode and write data into to file
to_file=open(to_file,'r+')
to_file.write(from_file_data)

print (len(to_file.readlines()))
print (len(from_file.readlines()))

to_file.close()
from_file.close()


#print (f"Data in from File:{from_file_data}")
#print (f"Data in to file: {to_file_data}")
#print (to_file_len)
#print (from_file_len)
#to_file1=open(to_file,'r')
#to_file_len=to_file1.readlines()

#if from_file_len == to_file_len:

#    print (f"Data copied from Source file: Number of Lines {from_file_len}")
#else: print (f"Data not copied from Source file: Number of Lines {from_file_len}")
