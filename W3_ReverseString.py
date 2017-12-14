lname = input("Enter Last Name: ")
fname = input ("Enter First Name: ")
print (lname, fname)
print (len(lname), len(fname))
n=0
list1=[]
while n <= len(lname)-1:
    print(lname[n])
    list1.append(lname[n])
    n+=1
print (list1)
list1.reverse()
print (list1)
