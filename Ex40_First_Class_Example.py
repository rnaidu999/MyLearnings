class song(object):
    def __init__ (self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_baby = song (["Happy Birthday to you",
                     "I don't want to get used",
                     "So I will stop right here"])

happy_baby.sing_me_a_song()

class sing(object):
    num1=34
    num2=45
    def __init__(self, value1,value2):
        self.a=value1
        self.value2=value2

#accessing global variables in a method
    def add_two_num (self):
        print (self.num1 + self.num2)

#accessing the self Variables in a method
    def mult_two_num (self):
        print (self.a * self.value2)

#Method without using the parameters
    def name_print(self):
        print ("My Name is Sateesh Naidu")

#Defing variables witin a method
    def num_in_fun(self):
        value1=40
        value2=60
        return (value1 * value2)

#Method with 3 parameters
    def mul_of_3num(self, third):
        print(self.a * self.value2 * third)

#Method with it's own arguments
    def div_num(self,n1,n2):
        print (n1/n2)

add_two=sing(6,6)
add_two.add_two_num()
add_two.mult_two_num()
add_two.name_print()
add_two.num_in_fun()
add_two.mul_of_3num(5)
print (add_two.num_in_fun())
add_two.div_num(1000,4)
