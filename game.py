"""
Granny/Hello Neighbor Game By VIDHI SONI
MY GAME:
HELLO GRANNY GAME!!!!!!!!!
STORYLINE:
You are stuck in a house with 10 rooms. There is 1 key in each room except the one you started in.
GOAL:
You need to find 5 keys without the granny catching you.
ROOMS:
There will be 6 rooms inside and 3 rooms outside
INSIDE:
-pantry(filled with old cans and food)-find the can that is fake with the key inside
-science room(filled with math and science)-find a key by solving a math or science problem
-library(filled with books)-there are three books on the table, find the one that is fake
-attic(filled with old boxes and antiques)-you have to look at the back of a photo and find the combo for a lock
-kitchen(filled with potions and recipies)- there is a recipe and you have to find exaclty what to put into the potion to make the key
-trophy room(a bunch of old trophies of granny's cooking)-have to order them by height unlocks the safe, which has the key
OUTSIDE:
-gazebo(you have to chill with granny's family)-you have a choice of what to say and you have to say the right things to get te key
-yard(a bunch of animals chase you in a maze)-there is a maze like harry potter with a bunch of animals in the way that u have to fight and a key in the middle
-greenhouse(a bunch of old, tangly, dangerous plants)-water them correctly and one spits out the key
"""


#INTRODUCTION/SETTING UP THE GAME


#This part introduces the player to the game so they know what is happening
print("\n\nHELLO GRANNY BY VIDHI SONI")
print("You find yourself in a dark, damp room and you feel tired.\nYou are not in your house!\nYou need to find your way home.")
print("You find a note right beside you.\nIt says . . .")
print("Welcome to my home, dear child. You won t be leaving anytime soon... unless you can play my game.\nHidden across these grounds are 9 rooms, each holding a key.")
print("Find 5 of them to unlock the front door and escape.\nBut be warned: I am always watching, and I don t like uninvited guests.")

#This code make granny go in different places every time you play using random
import random
rooms = ["Pantry", "Science Room", "Library", "Attic", "Kitchen", "Trophy Room", "Gazebo", "Yard", "Greenhouse"]
granny_location = random.choice(rooms)
print("Granny is in the ", granny_location)

#This part just makes sure you are not cheating and you don't have any of the keys yet
has_key1=False
has_key2=False
has_key3=False
has_key4=False
has_key5=False
has_key6=False
has_key7=False
has_key8=False
has_key9=False

#This part is just starting to count the count_keys
count_keys=0

#This part asks where you want to go first
u_go=input("Where do you want to go first(pantry, science room, library, attic, kitchen, trophy room, gazebo, yard or greenhouse) = ").lower().strip()


#PANTRY


def enter_pantry():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key1, u_go
#You probably shouldn't go into the room if granny is there, right?
    if granny_location.lower() == "pantry":
        print("\nOh no, granny is in the pantry! RUN!")
        return
#If you already went into the pantry, what was the point of going in it again?
    if has_key1:
        print("You already searched the pantry and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Introduction to the pantry
    print("\n\nTo the pantry we go!")
    print("In the pantry you find a ton of old, cluttered food that is expired.\nYou see your first clue. . .\nFind the fake can and your key will be inside.")
#The challlenge of the pantry
    while not has_key1:
        print("On the first shelf you find 5 cans of soup")
        print("The first one says Totally Not Expired Soup That We Have Reused")
        print("The second one says Lovelly Tomato Soup")
        print("The third one says Granny s Key Soup")
        print("The fourth one says Freshely Baked Beans")
        print("The fifth one says Old Rusty Pinapples")
    
        pantry_choice = input("Which can would you like to open?(1-5) ")
#The correct answer
        if pantry_choice == "3":
            print("Great Job! You found the key!")
            count_keys = count_keys + 1
            print(count_keys, "key(s)")
            has_key1 = True
#The wrong answers
        elif pantry_choice in ["1", "2", "4", "5"]:
            print("\nYou open the can and you smell the rotten smell of burnt spinach.")
            print("Ewww. There is nothing in this can except expired food, try another one!\n")
#The invaild answers
        else:
            print("\nInvaild input, please try again.\n")


#SCIENCE ROOM


def enter_science_room():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.    
    global count_keys, has_key2, u_go
#You probably shouldn't go into the room if granny is there, right?
    if granny_location.lower() == "science room":
        print("\nOh no, granny is in the science room! RUN!")
        return
#If you already went into the science room, what was the point of going in it again?
    if has_key2:
        print("You already searched the science room and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Introduction to the science room
    print("\n\nTo the science room we go!")
    print("In the science room you find a ton of unfinished math and science problems. You find another clue.\nIt says . . . Solve this math problem without a calculator")
#The eqation of the science room
    while not has_key2:
        science_room_math = input("\nHere it is . . . 6÷ 2(1+2) = ").strip()
#The correct answer
        if science_room_math == "9":
            print("Great job! You got it!")
            count_keys=count_keys+1
            print(count_keys, "key(s)")
            has_key2=True
#The wrong/invalid answers
        else:
            print("\nYou got it wrong or you put in an invailid input. If you got it wrong, try and use PEMDAS.")


#LIBRARY


def enter_library():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key3, u_go
#You probably shouldn't go into the room if granny is there, right?
    if granny_location.lower() == "library":
        print("\nOh no, granny is in the library! RUN!")
        return
#If you already went into the library, what was the point of going in it again?
    if has_key3:
        print("You already solved the library riddle and got the key!")
        print("Where to next?")
        return
#Introduction to the library
    print("\n\nTo the library we go!")
    print("In the library you find a note that says . . . \nWelcome to the library. You won t need to find anything here, I have a riddle for you.\n")
#The riddle of the library
    while not has_key3:
        library_riddle = input("What happens once in a minute, twice in a moment and never in a thousand years? ").lower().strip()
#The correct answer
        if library_riddle == "m" or library_riddle == "the letter m" or library_riddle == "letter m":
            print("You got it! Great job! You found that spelling was key!")
            count_keys = count_keys + 1
            print(count_keys, "key(s)")
            has_key3 = True
#The wrong/invaild answers
        else:
            print("\nYou got it wrong or you put in an invalid input. If you got it wrong, focus on the spelling.\n")


#ATTIC


def enter_attic():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key4, u_go
#You probably shouldn't go into the room if granny is there, right?
    if granny_location.lower() == "attic":
        print("\nOh no, granny is in the attic! RUN!")
        return
#If you already went into the attic, what was the point of going in it again?
    if has_key4:
        print("You already solved the attic riddle and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Introduction to the attic
    print("\n\nTo the attic we go!")
    print("In the attic you see an old picture of granny and her family. You also see a safe and it has another note on it! It says . . .")
    print("Hello again, to find the attic s key, you must find the combination of this safe.\n")
#The challlenge of the attic
    while not has_key4:
        attic_choice = input("Enter 1 to look at the picture closer\nEnter 2 to look at the safe closer: ").strip()
#The correct answer #1
        if attic_choice == "1":
            print("\nOn the back of the picture you see a code: 37-58-92. Maybe it is the combination for the safe!")
            correct_attic_choice = input("Enter the correct combination = ").strip()
#The correct Answer #2
            if correct_attic_choice == "37-58-92":
                print("Great Job! The safe unlocked and you got a key!")
                count_keys = count_keys + 1
                print(count_keys, "key(s)")
                has_key4 = True
#The wrong answers
            else:
                print("That combination didn t work! Try again.\n")
#The curious answer
        elif attic_choice == "2":
            print("\nYou look at the safe and try some combinations, but they don t work. Maybe you should look at the picture first!\n")
#The invaild answers
        else:
            print("Invalid input, please enter 1 or 2.\n")


#KITCHEN


def enter_kitchen():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key5, u_go
#You probably shouldn't go into the room if granny is there, right?
    if granny_location.lower() == "kitchen":
        print("\nOh no, granny is in the kitchen! RUN!")
        return
#If you already went into the kitchen, what was the point of going in it again?
    if has_key5:
        print("You already solved the kitchen riddle and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Introduction to the kitchen
    print("\n\nTo the kitchen we go!")
    print("You look around the kitchen and it is a big mess.\nYou start making a bigger mess to find a note and you find one on the table.")
    print("\nIt says . . . Use this recipe to make a potion for the key. Start by taking out some chocolate chips.")
    print("(I usually save these for my grandchildren but . . .) \nThen melt them in a pot on the stove.\nThen take out some strawberries, wash them and")
    print("Eat ONE with the chocolate. Then you will find something heavy in your pocket and find it is the key.\n")
#The kitchen recipe
    while not has_key5:
        kitchen_input = input("Enter the correct order of numbers of the things you have to do.\n7=Eat one strawberry with the chocolate. \n4=Find strawberries and wash them.\n9=Melt the chocolate chips. \n1=Take out some chocolate chips. ")
#The correct answer
        if kitchen_input == "1947":
            print("Great Job, you found the key!")
            count_keys = count_keys + 1
            print(count_keys, "key(s)")
            has_key5 = True
#The wrong/invaild answers
        else:
            print("\nIf you are here you entered an invaild input or you have gotten it wrong.\nIf you have gotten it wrong, please try to enter a four-digit number with no spaces or commas.\n")


#TROPHY ROOM


def enter_trophy_room():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key6, u_go   
#You probably shouldn't go into the room if granny is there, right? 
    if granny_location.lower() == "trophy room":
        print("\nOh no, granny is in the trophy room! RUN!")
        return
#If you already went into the trophy room, what was the point of going in it again?
    if has_key6:
        print("You already solved the trophy room riddle and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Trophy room introduction
    print("\n\nTo the trophy room we go!")
    print("In the trophy room you find a ton of trophies of granny's cooking.")
    print("You see a note next to three of them.")
    print("These three trophies are very special. I want you to put them in a specific order.\n")
    print("1. 23 in tall and is the most special to me.")
    print("2. 20 in and is not very special to me but i still like it.")
    print("3. 17 in tall and I hate it.")
#Trophy room challenge
    while not has_key6:
        trophy_room_order = input("What order do you have to put it in? ").strip()
#The correct answer
        if trophy_room_order == "321":
            print("Great job! How did you know? You got another key!")
            count_keys = count_keys + 1
            print(count_keys, "key(s)")
            has_key6 = True
#The wrong/invaild answers
        else:
            print("\nYou either got it wrong or you put in an invaild answer.")
            print("Make sure there are no spaces or commas.")
            print("Try to do it from shortest to tallest\n")


#GAZEBO


def enter_gazebo():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key7, u_go   
#You probably shouldn't go into the room if granny is there, right? 
    if granny_location.lower() == "gazebo":
        print("\nOh no, granny is in the gazebo! RUN!")
        return
#If you already went into the gazebo, what was the point of going in it again?
    if has_key7:
        print("You already solved the gazebo challenge and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Gazebo introduction
    print("\n\nTo the gazebo we go!")
    print("In the gazebo you find granny's family sitting around a table with three cups of tea. \nThe man says, hello child, One of these tea cups has a key at the bottom.\nChoose wisely!")
#Gazebo challenge
    while not has_key7:
        print("1. The Fancy Golden Teacup\n2. The Cracked Red Teacup\n3. The Ugly Blue Teacup")
        gazebo_choice = input("Which can would you like to open?(1-3) ")
#The correct answer
        if gazebo_choice == "1":
            print("Great Job! You found the key!")
            count_keys = count_keys + 1
            print(count_keys, "key(s)")
            has_key7 = True
#The wrong answers
        elif gazebo_choice == "2":
            print("\nYou look into the cup, there is nothing except broken old pieces of the teacup\nTry another cup!\n")
        elif gazebo_choice=="3":
            print("\nYou take a sip of the 'tea' but it was super sour lemon juice! \nNo key, try another one!\n")
#The invaild answers
        else:
            print("\nInvaild input, please try again.\n")


#YARD


def enter_yard():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key8, u_go   
#You probably shouldn't go into the room if granny is there, right? 
    if granny_location.lower() == "yard":
        print("\nOh no, granny is in the yard! RUN!")
        return
#If you already went into the yard, what was the point of going in it again?
    if has_key8:
        print("You already solved the yard maze and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Yard introduction
    print("\n\nTo the yard we go!")
    print("In the yard you see a gigantic maze that you cannot see over it is dark and scary inside. \nThe key is inside though. You have to find it.\n")
#The yard maze
    while not has_key8:
        yard_maze=int(input("The first fork you come across has signs.\n1. The wolf's cave\n2. The Golden Dream Road \nThe second intersection had\n1.Skeleton Highway\n2. Banana Road \nThe third crossroad had \n1. Candy Corner\n2. Zobbie Street \n\nEnter the correct order that you will go = "))
#The correct answer
        if yard_maze==221:
            print("Great Job! You got a key!")
            count_keys = count_keys + 1
            print(count_keys, "key(s)")
            has_key8 = True
#The wrong/invaild answers
        else:
            print("\nInvaild answer or it is wrong. Please try again. \nThink happiness.\n")


#GREENHOUSE


def enter_greenhouse():
#This global part tells the computer that it should use these varibales from all over the code, not just this part.
    global count_keys, has_key9, u_go
#You probably shouldn't go into the room if granny is there, right?
    if granny_location.lower() == "greenhouse":
        print("\nOh no, granny is in the greenhouse! RUN!")
        return
#If you already went into the greenhouse, what was the point of going in it again?
    if has_key9:
        print("You already solved the greenhouse riddle and got the key!")
        u_go = input("Where to next? ").lower().strip()
        return
#Introduction to the greenhouse
    print("\n\nTo the greenhouse we go!\nIn the greenhouse you see a ton of old, dangerous plants that are tied up with each other.\nYou see some instructions on the side. You read them . . .")
    print("\nFirst, water the soft, fuzzy green plant.\nThen pull out the weeds by the 2nd and 3rd plants.\nThe water the third plant.\nLastly, water the second plant.")
#The greenhouse instuctions
    while not has_key9:
        greenhouse_input = input("\n2=Water the third plant.\n4=Water the soft, fuzzy green plant.\n6=Water the second plant.\n8=Pull the weeds by the second and third plant.\nEnter the correct order of things you have to do = ")
#The correct answer
        if greenhouse_input == "4826":
            print("Great Job, the second plant spit out the key!")
            count_keys = count_keys + 1
            print(count_keys, "key(s)")
            has_key9 = True
#The wrong/invaild answers
        else:
            print("\nIf you are here you entered an invaild input or you have gotten it wrong.\nIf you have gotten it wrong, please try to enter a four-digit number with no spaces or commas.")


#MAIN GAME LOOP


#While you have less than 5 keys, you can go anywhere!
while count_keys < 5:
    if u_go == "pantry":
        enter_pantry()
    elif u_go == "science room" or u_go=="science":
        enter_science_room()
    elif u_go == "library" or u_go == "library room":
        enter_library()
    elif u_go == "attic":
        enter_attic()
    elif u_go == "kitchen":
        enter_kitchen()
    elif u_go == "trophy room" or u_go=="trophy":
        enter_trophy_room()
    elif u_go == "gazebo":
        enter_gazebo()
    elif u_go == "yard":
        enter_yard()
    elif u_go == "greenhouse":
        enter_greenhouse()
    else:
        print("Invalid input, please try again.")
#If you have less than 5 keys, you can go to other rooms
    if count_keys < 5:
        u_go = input("\nWhere to next? ").lower().strip()
#If not, you won the game!
    else:
        print("\nCONGRATULATIONS! You found 5 keys.\nYou immediately pun in all the keys into the front door and run straight out to your house!\n You are HOME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")



