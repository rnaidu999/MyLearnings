Sting1="Sateesh Naidu"
print (len(Sting1))

# Write a Python program to count the number of characters (character frequency) in a string
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        print (keys)
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
    #If the string length is less than 2, return instead of the empty string
def str_dis(str):
    if len(str) > 2:
        print (str[:2]+str[-2:])
    elif len(str) == 2:
        print (str+str)
    elif len(str) == 1:
        print (" ")

str_dis("weruerrre")
str_dis("JJ")
str_dis("M")

#Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself
def str_def(str1):
    char=str1[0]
    str2=str1.replace(char,'$')
    print (str2)

str_def("googleg")

#Write a Python program to get a single string from two given strings, separated by
#a space and swap the first two characters of each string.
Str1='abc'
str2='xyz'
print (str2[0:2]+Str1[2:], Str1[0:2]+str2[2:])

#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given
#string already ends with 'ing' then add 'ly' instead.
#If the string length of the given string is less than 3, leave it unchanged
def str_repl(str1):
    if str1[-3:]=='ing':
        return str1[0:-3]+'ly'
    elif str1[-2:]=='ly':
        return str1[0:-2]+'ing'
    else:
        return str1
print(str_repl('jakdfading'))
print(str_repl('jakdfadly'))
print(str_repl('dd'))

#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
#if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

val='The lyrics is not that poor!'
val=val.replace('poor','good')
fstr=val.find('not')
print (val[0:fstr-1]+val[fstr+3:])

#Write a Python function that takes a list of words and returns the length of the longest one.
def strlen(str1,str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else:
        return "Two strings have euqal leanth"
print(strlen("this is sateesh","this "))

#scenario2
def strlen(*number):
    word_list=[]
    for n in number:
        word_list.append(len(n))
    return number[word_list.index(max(word_list))]
print(strlen("th","not","yes3243","iuoweurioeuwio"))

#Write a Python program to remove the nth index character from a nonempty string.
def str_remove_indexchar(str1,n):
    if str1 != "" and len(str1)!= n:
        list1=list(str1)
        list1.pop(n)
        str1=''.join(list1)
        return str1
    else:
        return "Empty String or Index is out of range"
print (str_remove_indexchar("abdcejhdmc",10))

#Scenario2
def str_remove_indexchar(str1,n):
    if str1 != "":
        return str1[0:n-1]+str1[n:]
    else:
        return "Empty String"
print (str_remove_indexchar("abddcdf",7))

#Write a Python program to change a given string to a new string where the first and last chars have been exchanged
def str_chang(str1):
    return str1[-1]+str1[0:-2]+str1[0]

print (str_chang("qkjjlkkljkklQ"))
print (str_chang("23456789"))

#Write a Python program to remove the characters which have odd index values of a given string.
def str_remove_odd(str1):
    str2=""
    for n in range(len(str1)):
        if n%2 == 0:
            str2=str2+(str1[n])
    return str2
print(str_remove_odd ("ThisisSateeshuereweewrew"))

#Write a Python program to count the occurrences of each word in a given sentence.
from collections import Counter
def std_duplicate_words(str2):
    word_list=[]
    word_list=str2.split(" ")
    c=Counter(word_list)
    print (c)
std_duplicate_words("this is sateesh sateesh naidu is naidu")

#Write a Python script that takes input from the user and displays that input back in upper and lower cases
def reverse_str(str2):
    str3=''.join(reversed(str2))
    return str3.upper(), str3.lower()

print(reverse_str("This is sateesh"))

#Write a Python program that accepts a comma separated sequence of words
        #as input and prints the unique words in sorted form (alphanumerically)

def str_sort(str):
    str2=str.split(",")
    str2.sort()

    str3=''.join(str2)
    return str2, str3

print (str_sort("zeebra,yellow,red,apple,cat,ball,van"))

#Write a Python function to insert a string in the middle of a string
def str_insert(str1,str2):
    mid=int(len(str1)/2)
    str3=str1.replace(str1[mid],str2)
    print (str3)
str_insert("sateeshsnaidu","dhanvi")

#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

def str_repeate(strng):
    if len(strng) < 2:
        return "String Length must be minimum 2"
    else:
        return (strng[-2:]*4)

print (str_repeate("sateesh"))
print (str_repeate("s"))
print (str_repeate("dh"))

#Write a Python function to get a string made of its first three characters of a specified string.
# If the length of the string is less than 3 then return the original string.
print("\nFunction to get a string made of its first three characters of a specified string")
def str_first3char(str1):
    if len(str1) <=3:
        return str1
    else:
        return str1[0:3]
print (str_first3char("sateesh"))
print (str_first3char("sat"))
print (str_first3char("da"))

#Write a Python program to get the last part of a string before a specified character.
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])

#Write a Python function to reverses a string if it's length is a multiple of 4.
def str_rev_len4(str11):
    if len(str11)%4==0:
        return (' '.join(reversed(str11)))
    else:
        return str11

print(str_rev_len4("Sat"))

#Write a Python function to convert a given string to all uppercase if it contains at least 2
#uppercase characters in the first 4 characters
print ("******************************************")
def str_rev_upper(str12):

    if len(str12) >= 4:
        count=0
        for n in str12[0:4]:
            print (n.isupper())
            if n.isupper()==True:
                count+=1
        if count >= 2:
            #str13=''.join(reversed(str12))
            return str12.upper()
        else:
            return str12
    else:
        return str12

print(str_rev_upper("SaT"))

#Write a Python program to sort a string lexicographically
print ("******************************************")
def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('zyxvudcba'))
print(lexicographi_sort('quickbrown'))

#Write a Python program to remove a newline in Python
str1='Python Exe rcises\n'
print(str1)
print(str1.rstrip())

#Write a Python program to check whether a string starts with specified characters.
string = "w3resource.com"
print (string.startswith("w3r"))

#Write a Python program to display formatted text (width=50) as output.
print("************************************************")
import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()

#Write a Python program to remove existing indentation from all of the lines in a given text.
print("**********************************************")
import textwrap
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation )
print()

#Write a Python program to add a prefix text to all of the lines in a string.
import textwrap
sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)
#wrapped += '\n\nSecond paragraph after a blank line.'
final_result = textwrap.indent(wrapped, '> ')
print()
print(final_result)
print()

#Write a Python program to set the indentation of the first line.
print ("**************************************************")
import textwrap
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()

#Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with sign: {:+.2f}".format(x));
print("Original Number: ", y)
print("Formatted Number with sign: {:+.2f}".format(y));
print()

# Write a Python program to print the following floating numbers with no decimal places.
print ("***********************************************")
x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x));
print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y));
print()

#Write a Python program to print the following integers with zeros on the left of specified width.
print ("********************************************")
x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
print()

#Write a Python program to print the following integers with '*' on the right of specified width.
print("*********************************************")
x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 6d}".format(y));
print()

# Write a Python program to display a number with a comma separator.
print ("*******************************************")
x = 3000000
y = 30000000
print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x));
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y));
print()

#Write a Python program to format a number with a percentage.
x = 0.25
y = -0.25
print("\nOriginal Number: ", x)
print("Formatted Number with percentage: "+"{:.2%}".format(x));
print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.2%}".format(y));
print()

#Write a Python program to display a number in left, right and center aligned of width 10.
x = 22
print("\nOriginal Number: ", x)
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x));
print()
