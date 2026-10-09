print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side = input("Choose a direction. left or right: \n").lower()



if side == "left":
    print("You find an stream flowing down.\n The waters are calm and you see the island where the treasure is across the stream.\n")
    print("What will you do?\n")
    move = input("Swim across the stream or wait it out? swim or wait: \n").lower()

    if move == "wait":
        print("Your patience pays and a raft floats by and you use it to cross.\n")
        print(
            "After crossing, you see a shack and enter it.\n In, there are three coloured doors. What do you do?\n")
        print("Choose wisely! Only one door leads to the treasure.\n")

        door = input("Which door do you choose. red, blue or yellow?  \n").lower()

        if door == "red":
            print("You get burned by magical fire! Game Over!!!\n")

        elif door == "blue":
            print("A dragon resides here. You woke it and it ate you! Game Over!!!\n")
        elif door == "yellow":
            print("Congratulations!! You win!")

        else:
            print("Now that is just a sad and loser way to go man. Game Over..")

    else:
        print("You get eaten by piranhas and die.\n Game Over!!!")
else:
    print("You fell in a hole and died. Game Over!!!")

