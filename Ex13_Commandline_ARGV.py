#Import argv (Argument value) from sys library
from sys import argv

#read the WYSS section for how to run this.
#Passing the following value to the script from the command prompt
Script, First, Second, Third, value = argv

print ("The Script is called:", Script)
print ("The First Parameter:", First)
print ("The Second Paramemter:", Second)
print ("The Third Parameter:", Third)

for i in range(1, 10):
    print (f"{value} * {i} = {value *1}")
