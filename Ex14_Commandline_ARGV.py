from sys import argv

script, username =argv
print (f"\nHi {username}, This is Sateesh Naidu")
print (f"May I ask you couple of more questions {username}?")

prompt= '>>'

height= input (prompt)
print (f"Name: {username} and Height: {height}")

weight= input (prompt)
print (f"Name: {username} and weight: {weight}")

print (f"""\tAll right you said your Name is {username}
            Your height is {height}
            Your Weight is {weight}\n""")

# variantion1
print (f"Hi {username}, How are you today?")
prompt = ">>>"

height= input(prompt + f"\tEnter your height {username} :")
weight = input(prompt + f"\tEnter you weight {username} :")

print (f"Mr.{username} Nice, Your Height: {height} and Weight: {weight} are in proporition\n")

#with Data types
# variantion1
print (f"\tHi {username}, How are you today?")
prompt1 = (f"\t{username} Height>>>")
prompt2 = (f"\t{username} Weight>>>")

height1= int(input(prompt1))
weight1 = int(input(prompt2))

print (f"Mr.{username} Nice, Your Height: {height1} and Weight: {weight1} are in proporition")
