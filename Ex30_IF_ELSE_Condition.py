people=20
cats=10
dogs=35

if people > cats:
    print(f"\nPeple:{people} are more than cats: {cats} in the world\n")
elif people < cats:
    print ("\nCats are:{} are more than people {} in the world".format(cats,people))
else:
    print ("Can't be decide")

if people > dogs:
    print ("\nPeople are {} are moare than dogs {} in the world".format(people,gods))
elif people < dogs:
    print (f"\nDogs:{dogs} are more than people: {people} in the world")
else:
    print ("Can't be decide")

people+=15

if people >= dogs:
    print (f"People:{people} are equal to dogs:{dogs}")
elif people == dogs:
    print ("People: {} are equal to dogs {}".format (dogs, people))
