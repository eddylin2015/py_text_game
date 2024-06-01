import time
import sys
import os

from Biolib import * 
os.system('cls')

ShowWords('Caution !!!',0.1)
print("")
print("")
time.sleep(1)
print("     / \          ")
print("    / ! \       ")
print("   /_ _ _\     ")
print("")
time.sleep(1) #time for the words to occur
ShowParagraph(
"""New disease.... X you made...
""")
# showWord allow the word to type slowly; 
# showparagraph is that eACH SENTENCE SLOW;Y
'''
'''
time.sleep(1)
os.system('cls')#clean the scene
printc("",10)
CountDown(3)

os.system('cls')


ShowParagraph(
"""Welcome to ET lab...
You are helping scientist to xxxxx
""")
time.sleep(1)
Username=(input("Username: "))

print(f'Hello,{Username} xxxx')
CountDown(3)
os.system('cls')
Start=input('Are you ready to start? (Yes/No)')
if Start==('No'):
    os.system('cls')
    ShowWords("The patient die...")
    exit()
else:
    os.system('cls')
    ShowParagraph("""Rules:
                  xxxxxxxx
                  """)
    os.system('cls')
    ShowParagraph("""Please choose your character:
1. White Blood Cell:Granulocyte (Attack power:10 Protect:9 HP:100 EXP:0 level:0)
2. White Blood Cell:Monocyte (Attack power:9 Protect:10 HP:100 exp:0 level:0)
3. White Blood Cell:Lymphcyte (Attack power:9 Protect:9 HP:150 exp:0 level:0)
                  """)
 
character_choice=9
while(not character_choice in ["1","2","3"]):
    character_choice=(input("select character 1/2/3:"))      

if character_choice == "1":
    character = Character("Granulocyte", 10, 9, 100)
elif character_choice == "2":
    character = Character("Monocyte", 9, 10, 100)
elif character_choice == "3":
    character = Character("Lymphcyte", 9, 9, 150)
else:
    print("Invalid character choice. Exiting the game.")
    exit()    
character.info()
enemies = [
    Enemy("Pythonigen", 8, 5, 30),
    Enemy("Mathogen", 10, 8, 50),
    Enemy("Studiogen", 12, 7, 70)
]


CountDown(3)
battle(character, enemies)