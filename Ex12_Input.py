
# Customer information
name= input("Enter Customer Name:")
age= int(input ("Enter Custoemr Age:"))
height= input("Enter Customer Height:")

#Print Customer Information
print (f"User Name:{name}, Age: {age}, Height: {height}")

# Print table for the value provided by User
table= int(input ("Enter Number to generate Table: "))
for i in range (1, 11):
    print (f"{table}*{i} = {table * i}")

#Use f function to print the customer Information

# Customer information
name= input("\tEnter Customer Name:")
age= int(input (f"\tNice Name {name}, Enter Custoemr Age:"))
height= input(f"\tAre you {age},nice: Enter Customer Height:")

#Print Customer Information
print (f"User Name:{name}, Age: {age}, Height: {height}")
