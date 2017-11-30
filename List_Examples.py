
list_item=[12,323,232,'CRR','FFS323',233.33,45,34,"dwewe",3434]
List_item1=[]
List_item2=[6,5,4,3,2,1]
List_item3=['aew','zdsd','ree','cddfd','botr']

print (list_item)
#get the Fisrt value from the List
print (list_item[0])

#Display Empty String
print (List_item1,"\n")

#add all List items
print (list_item + List_item2 + List_item3, "\n")

print (list_item * 2,"\n")

print (list_item[0] * 2,"\n")

print (list_item)

#Add item to the end of the list
list_item.append("sateesh")
print(list_item)

#Insert Item at the given position
list_item.insert(2,"Naidu")
print(list_item)

#Modify an element by using the index of the element
list_item[2]="Soujanya"
print (list_item)

#Remove an item from the list
list_item.remove("sateesh")
print (list_item)
#Cust 1st 3 items from the list
print ('Cut first three items')
print (list_item[:3])

#Cut first two items from the List_item
print ('Cust 4th two items')
print (list_item[4:5])

#Creates Copy of original list_item
print(list_item[:])

#Reove the item from the list
list_item.pop(6)
print (list_item)

#Return the index in the list of the first item whose value
print (list_item[0])

#Return the number of times 'a specific value (Soujanya)' appear in the list
print ("Count of the list")
print(list_item.count("Soujanya"))

#Sort the items of the list in place
List_item3.sort(key=None, reverse=False)
print(List_item3)
List_item2.sort(key=None, reverse=False)
print(List_item2)

#Reverse the list
list_item.reverse()
print (list_item)

#Return a shallow copy of the list
list_item.copy()
print (list_item)

#Search the Lists and find Elements
print(list_item.index('Soujanya'))

#Lists are Mutable
list_item[0]=1212
print (list_item)

#Remvoe all the items from the list
list_item.clear()
print (list_item)

#Find the largest and the smallest item in a list
print(max(List_item2))

#Find the Smallest and the smallest item in a list
print(min(List_item2))

#Nested lists in Python
listx = [["Hello", "World"], [0, 1, 2, 3, 4, 5]]
print (listx)
print(listx[1][4])
print(listx[0][1])
listx.append(["Name","City"])
print (listx)
listy=listx
print(listy)
print (listy[0][1],listy[1][0],listy[2][0])

#Using Lists as Stacks
color_list=["Red", "Blue", "Green", "Black"]
color_list.append("White")
color_list.append("Yellow")
print (color_list)
color_list.pop()
print(color_list)
color_list.pop()
print(color_list)
color_list.pop()
print(color_list)
