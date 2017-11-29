def start ():
    print ("\nYou are in a Hall:")
    print ("""You have two rooms
            1. Gold Treasure
            2. Cash Treasure\n""")

    print ("Which Room door do you want to open?")

    room_door=input("\nSelect the Room (1 or 2)>>  ")

    if room_door=="1":
        print ("You selected Gold Treasure, be careful this room is Secured by a wild Bear\n")
        bare_room()
    elif room_door== "2":
        print ("You have selected Cash Treasure, be careful this room is always scured by Devil\n")
        devil_room()
    else:
        dead (" ! Invalid Room Selection")

def dead(reason):
    print (f"\nGave is over: {reason}")

def devil_room():
    print ("\nYou have 3 options to Fight with Devil")
    print ("""Please select right option >>>>
            1. Sword
            2. Magical Stick
            3. Magical Axe\n """)
    weapon = input ('Select Wepon >>> ')
    if weapon is '1':
        dead ("Sowrd is not strong enough to fight with Devil\n")
    elif weapon is '2':
        dead ("Magical Axe is not strong enough to fist with Devil\n")
    elif weapon is '3':
        print ("Congratulations you have selected the right weapon and killed Devil\n")
        cash_treasure()
    else:
        dead ("Invalid Selection")

def bare_room():
    print ("""You have couple of options to move the Bare away from the room

            1. OpenDoor
            2. ShowSmallFire
            3. ShowBigFire""")

    print ("How are going to move the Bear?\n")
    bear_move=False

    choice=input("Select Right Option to move the Bear out >>  ")
    if choice == "1":
        dead ("Bare looks at you then slaps your face off.\n")
        exit(0)
    elif choice =="2" or bear_move:
        print ("Bear looks at you then slaps your face off.")
        dead ("! You are dead")
    elif choice == "3" and not bear_move:
        print ("Congratulations you move Bare of your way\n")
        gold_room()
    else:
        dead ("! You don't know how to move the Bear out of your way")

# gold_room to
def gold_treasure():
    print ("""One of these boxes has Gold Room Key, Please select the right Box

            2. Box1
            4. Box2
            8. Box3

            Note: Invalid Selection will terminate you from the Game\n""")

    key=input("Select the box >>> ")
    if key.isnumeric():
        if key == "2":
            dead (f"Sorry no key found in the selection Box :{key}")
        elif key == "4":
            dead (f"Sorry no key found in the selection Box: {key}")
        elif key == "8":
            print ("Congratulations! you found the key and Doop is open")
            gold_coins()
    else:
        print ("Invalid Selection, please select valid option (2, 4 or 8)")
        gold_room()


# 3.Box3 is the right selection to get the Door Key.
# 1.Box1 and 2.Box2 will end the gamv.
# Invalid selection apart from box, 1,2 or 3. It will loop until the right selection made.
def cash_treasure():
    print ("Plese select the right option to find the room Key\n")
    print ("""Select one the following boxes for password of the room
            1. Box1
            2. Box2
            3. Box3 \n""")
    cash_tre_key=input ("Select the Box >>> ")
    if cash_tre_key.isnumeric():
        if int(cash_tre_key) == 1:
            dead ("Sorry wrong choise no password in Box1\n")
        elif int(cash_tre_key) == 2:
            dead ("Sorry wrong choise no password in Box2\n")
        elif int(cash_tre_key) == 3:
            print ("\nCongratulations....you selected the right box\n")
            print ("Here is Password to open the Cash Treasure: [[CashTreasureIsYours]]\n")
            get_treasure()
        else:
            dead ("Sorry wrong choise you coundn't select the right box\n")
    else:
        print ("Invalid Selection, Please try again")
        cash_treasure()

# You need to enter Password  CashTreasureIsYours
def get_treasure():
    door_key=input("Enter Password >>> ")
    if door_key == "CashTreasureIsYours":
        print ("Contratulation $50 Million treasure is your's")
        exit(0)
    else:
        dead ("Access Denied.....\n")

def gold_coins():
    coins= input ("How Many gold coins do you want to grab >>>  ")
    if coins.isnumeric():
        if int(coins) in range(100,99999999999999999):
            print ("Congratulations You own the enough coins")
            exit()
        elif int(coins) in range (0,100):
            print ("You couldn't grab enough gold coins....)")
    else:
        print ("Invalid Selection (Alpha Numeric), Coins can be quantiy only in numbers")
        gold_coins()
#    if coins.isalnum():
#        print ("Invalid Selection (Alpha Numeric), Coins can be quantiy only in numbers")
#        gold_coins()
#    if coins.isalpha():
#        print ("Invalid Selection (Alpha), Coins can be quantiy only in Numbers")

start ()
