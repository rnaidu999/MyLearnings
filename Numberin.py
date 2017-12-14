def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))

def sum_three(a,b,c):
    sum1=a+b+c
    if a==b==c:
        sum1=sum1*3
    return sum1

print (sum_three(2,2,2))
print (sum_three(1,2,3))

#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
def is_string(st_name):
    if len(st_name) >= 2 and st_name[:2]=="IS":
        return st_name
    return "IS"+ st_name

print (is_string("Arry"))
print (is_string("IS Empty"))

#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
def even_odd(num):
    if num%2 == 0:
        print ("Event NUmber")
    else:
        print ("Odd number")

even_odd(5)

#Write a Python program to count the number 4 in a given list.
def count_num(num_list):
    count=0
    for num in num_list:
        if num == 4:
            count=count+1

    return count

print (count_num([1,2,3,4,4,4,5,6]))
print (count_num([4,2,3,4,4,4,5,6]))
print (count_num([1,2,3,2,2,2,5,6]))

#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
def return_str(val):
    if len(val) > 2:
        print (val[:2])
    else:
        print(val*5)


return_str("Satesh")
return_str("ST")

#Write a Python program to test whether a passed letter is a vowel or not.
def vowel(letr):
    if type(letr) == str:
        if letr in ['a','e','i','o','u','A','E','I','O','U']:
            print ("VOWEL")
        else:
            print ("Not VOWEL")
    else:
        print ("Enter only String")

vowel ("A")
vowel ("L")
vowel(4)

def isinlist(n):
    if n in [1, 5, 8, 3]:
        return True
    else:
        return False
print (isinlist(3))
print (isinlist(-1))

def isinlist(list_item, n):
    if n in list_item:
        return True
    else:
        return False
print (isinlist([1, 5, 8, 3],3))
print (isinlist([1, 5, 8, 3],-1))

def isinlist(list_item, n):
    for value in list_item:
        if n==value:
            return True
    return False

print (isinlist([1, 5, 8, 3],3))
print (isinlist([1, 5, 8, 3],-1))

#Write a Python program to create a histogram from a given list of integers.
#without Array
def histrogram(list1):
    for n in list1:
        outlist=''
        while n >= 1:
            outlist+='*'
            n-=1
        print (outlist)
histrogram([2,2,5,6,7,0])
#wih Array
def histrogram(list1):
    outlist=[]
    for n in list1:
        while n >= 1:
            outlist.append('*')
            n-=1
        print (outlist)
        outlist.clear()
histrogram([2,2,5,6,7,0])

#Write a Python program to concatenate all elements in a list into a string and return it.
def concate(list_item):
    str1=''
    for n in list_item:
        str1+=n
    return str1
print (concate(['w','e','r','t','y']))
print (concate(['3','4','7','9','10']))

#Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
def evennum(list_item):
    for n in list_item:
        if n != 237:
            if n%2 == 0:
                print (n)
        else:
            break

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
evennum(numbers)

#Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print (color_list_1.difference(color_list_2))

#Write a Python program to add two objects if both objects are an integer type


def addtwo(a,b):
    if not ((isinstance(a,int)) and (isinstance(b,int))):
        print ("Enter Integer value")
    else:
        print (a+b)

addtwo('cc',9)
