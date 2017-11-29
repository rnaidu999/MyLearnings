names=['Ram','Sam','Ramesh','Ganesh','Sundar','Mahesh']
age=[21,25,27,23,28,26]
weight=[62,68,61,65,71,72]
height=[5.11,5.10,6,6.1,5.8,5.9]

for i in names:
    print (f"Names of team members {i}")

for j in age:
    print (f"Age of the team members by Name order : {j}")

for k in weight:
    print (f"Weight of given team members by order in Name {k}")

for l in height:
    print (f"heights of given team members by order in Name {l}")


#Displaying data uwing while loop

i=0;name_a_w_h=[]
print ("\nDisplaying Data through While loop")
print ("=========================================================")
print ("\nName\t\tAge\t\tWeight\t\theight")
print ("=========================================================")

while i < len(names):
    n_a_w_h=(f"{names[i]}\t\t{age[i]}\t\t{weight[i]}\t\t{height[i]}")
    name_a_w_h.append(n_a_w_h)
    print (n_a_w_h)
    i=i+1
#print (len(name_a_w_h))

#Displaying data using for loop

print ("\nDisplaying Data through for loop")
print ("=========================================================")
print ("\nName\t\tAge\t\tWeight\t\tHeight")
print ("=========================================================")

for i in name_a_w_h:
    print (i)
