#Write a Python class to convert an integer to a roman numeral
class py_solution:
        def int_to_Roman(self, num):
            val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
                ]
            syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
                ]
            i=0
            roman_num=''
            while num > 0:
                for _ in range(num // val[i]):
                    roman_num+=syb[i]
                    num-=val[i]
                i=i+1
            return roman_num
print (py_solution().int_to_Roman(400))

#Write a Python class to convert a roman numeral to an integer.
print ("**************Write a Python class to convert a roman numeral to an integer*************")
class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))

#Write a Python class to find validity of a string of parentheses,
# '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}"
#are valid but "[)", "({[)]" and "{{{" are invalid.
print ("******************************************************")
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))

#Write a Python class to get all possible unique subsets from a set of distinct integers.
class py_solution(object):
    def sub_sets(self, sset):
        return self.subsetsRecur([],sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))

#Write a Python class to find a pair of elements (indices of the two numbers) from a
#given array whose sum equals a specific target number. - Go to the editor
#Input: numbers= [10,20,10,40,50,60,70], target=50
#Output: 3, 4

#My Version
class py_sum_num:
    def find_num(self,list_1,target):
        for num in range(len(list_1)):
            if int((list_1[num] + list_1[num+1]))==target:
                return (num,num+1)

print ("index1=%d, index=%d" % py_sum_num().find_num((10,20,10,40,50,60,70),50))
#Actual Excerise
print("************************")
class py_solution:
   def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            print (i, num)
            if target - num in lookup:
                return (lookup[target - num] + 1, i + 1)
            lookup[num] = i
            print (lookup)
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))

#Write a Python class to find the three elements that sum to zero from a set of n real numbers. - Go to the editor
#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#Output : [[-10, 2, 8], [-7, -3, 10]]
print ("********************************")
class printsum_3:
    def add_3_num(self,numlist):
        neg=[]
        pos=[]
        for val in numlist:
            if val < 0:
                neg.append(val)
            else:
                pos.append(val)
        for n in range(len(pos)):
            nn=1
            for nn in range (len(pos)):
                #print (pos[n],pos[nn])
                if ((pos[n] + pos[nn]) + neg[nn-1]) == 0:
                    print (pos[n], pos[nn],neg[nn-1])

                if ((neg[n] + neg[nn]) + pos[n]) == 0:
                    print (neg[n], neg[nn],pos[n])
printsum_3().add_3_num([-25, -10, -7, -3, 2, 4, 8, 10])

#Write a Python class to implement pow(x, n).
print ("********************************")
class prower_of_num:
    def power_num(self,num,power):
        if type(num) != int or type(power) != int:
            return "Please enter only Numbers"
        elif num==0 or num==1 or power==1:
            return num
        else:
            return num ** power

print (prower_of_num().power_num(4,4))

#Write a Python class to reverse a string word by word. - Go to the editor
#Input string : 'hello .py'
#Expected Output : '.py hello'

#Using Direct Method
class string_reverse:
#    def __init__(self,str14):

    def string_rev(self,str14):
        str15=''.join(reversed(str14))
        return str15

print (string_reverse().string_rev('hellp.py'))

print ("**********Reverse the List manually************")
#Reverse the List manually
class string_reverse_manual:
#    def __init__(self,str14):
    def string_rev_manual(self,str14):
        str15=[]
        str16=''
        for value in str14:
            str15.append(value)
        str15.reverse()
        str16=str(str15)
        return str(str16)

print (string_reverse_manual().string_rev_manual('hello.py'))

print ("**********Reverse by decresing for loop manually************")
#Reverse by decresing for loop manually
class string_reverse_manual:
#    def __init__(self,str14):
    def string_rev_manual(self,str14):
        str16=''
        for value in range(len(str14),0,-1):
            str16+=str((str14[value-1]))
        return str16

print (string_reverse_manual().string_rev_manual('hello .py'))

#Write a Python class which has two methods get_String and print_String.
#get_String accept a string from the user and print_String print the string in upper case.

class get_str_print_str:
    def __init__(self):
        self.strma=' '
    def get_str(self):
        self.strma=input("Enter String :")
    def print_str(self):
        print (self.strma.upper())

str_obj=get_str_print_str()
str_obj.get_str()
str_obj.print_str()
