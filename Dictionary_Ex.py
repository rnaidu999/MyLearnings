# Creating Empty Disctionary
my_dist=dict()
print (my_dist)

#Create Distionary with values
my_dist1={'name':"Sateesh","age":32,"height":32}
print(my_dist1)

#Get value by key in Python dictionary
print (my_dist1.get('name'))
print (my_dist1['age'])
print(my_dist1.get('height'))
print(my_dist1.get('name'),my_dist1['age'],my_dist1.get('height'))

#Add key/value to a dictionary in Python
Colors_dist={1:"red",2:'green',3:'blue',4:'black'}
print(Colors_dist)
Colors_dist.update({5:'yellow'})
print(Colors_dist)
Colors_dist[6]="blue"
print(Colors_dist)
print (Colors_dist.items())
Colors_dist[1]="white"
print(Colors_dist)
print (Colors_dist.items())

#Iterate over Python dictionaries using for loops
for key,valye in Colors_dist.items():
    print (key,"Clor Code:",Colors_dist[key])

#Remove a key from a Python dictionary
my_numbers = {'c':1,'d':2,'a':3,'c':4,'f':5,'e':6,'b':7}
print(my_numbers)
if 'a' in my_numbers:
    del my_numbers['a']
    print (my_numbers)

#Sort a Python dictionary by key
print(sorted(my_numbers))

#Find the maximum and minimum value of a Python dictionary
key_max=max(my_numbers.keys())
key_min=min(my_numbers.keys())
print("Maximum Number :", my_numbers[key_max])
print("Minimum Number :", my_numbers[key_min])

#Concatenate two Python dictionaries into a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4={}
for e in (dic1,dic2,dic3):
    dic4.update(e)
    print (dic4)

#Test whether a Python dictionary contains a specific key
fruits = {}
fruits["apple"] = 1
fruits["mango"] = 2
fruits["banana"] = 4

if 'mango' in fruits:
    print ("Has Mangos")
else:
    print ("Mangos are not there")

if 'banana' in fruits:
    print ("Banana is there")
else:
    print("No Banana")

#Find the length of a Python dictionary
print (len(my_numbers))
