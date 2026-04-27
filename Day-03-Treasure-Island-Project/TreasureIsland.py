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

first_choice = input('You are at a cross road. Where do you want to go? Type "Left" or "right". \n').lower()
if first_choice == "left":
    second_choice = input('You\'ve reached the seashore. There\'s an island not far away. Are you going to go there now? "Yes" or "no"? \n').lower()
    if second_choice == "yes":
        third_choice = input('You started walking deeper into the island. Three houses appeared before you. Which house do you prefer: "1", "2", or "3"? \n').lower()
        if third_choice == "1":
            print("A witch turned you into a frog. Game over.")
        elif third_choice == "2":
            print("You found the treasure. You have won.")
        elif third_choice == "3":
            print("You teleported to your home. Game over.")
        else:
            print("You had to choose from the given options. Game over.")

    else:
        print("Suddenly, fog descended and the island disappeared.")

else:
    print("You entered a dragon's lair, and the dragons ate you. Game over.")
