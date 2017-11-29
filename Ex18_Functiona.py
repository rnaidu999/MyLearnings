# This functional is like as argv
def add_num(*vars):
    val1,val2,val3,val4=vars
    print (f"Addition of tow number: {val1+val2+val3+val4}\n")

#function with 3 parameters
def mul_num (val1, val2, val3):
    print (f"Multiplication of the give numbers: {val1*val2*val3}\n")

#function with 2 parameters
def sub_num (val1,val2):
    print (f"Substraction of the numbers: {val1-val2}\n")

#function with no parameters
def zero_para():
    print (f"I got Nothing")

add_num(4,5,5,5)
mul_num (2,4,3)
sub_num (8,18)
zero_para()
