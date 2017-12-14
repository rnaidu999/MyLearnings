#Write a Python program to accept a filename from the user and print the extension of that.
filename=input("Enter File Name with Extension :")
f_exten=filename.split(".")
print("File extension",repr(f_exten[1]))

#Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print("%s %s" %(color_list[0],color_list[-1]))

#Write a Python program to display the examination schedule.
exam_st_date = (11, 12, 2014)
print ("The examination will start from :",exam_st_date[0],"/",exam_st_date[1],"/",exam_st_date[2])
print ("The examination will start from :%s / %s / %s"%exam_st_date)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
a=int(input("Enter Value: "))
n1=int("%i" % a)
n2=int("%i%i" % (a,a))
n3=int("%i%i%i" % (a,a,a))
print (n1,type(n1))
print (n2,type(n2))
print (n3,type(n3))
print (n1+n2+n3)
if type(n1)== int:
    print ("it is integer")

#Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print (abs.__doc__)

#Write a Python program to print the calendar of a given month and year
import calendar
y = int(input("Enter year: "))
m = int(input("Enter Month: "))
print(calendar.month(y,m))
