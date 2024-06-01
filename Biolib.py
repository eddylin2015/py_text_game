import time
import sys
import os
os.system('cls')
def ShowWords(words,timespend=1):
    for countdown in range(len(words)):
        sys.stdout.write('%s' % words[countdown])
        sys.stdout.flush()
        time.sleep(timespend)

def ShowParagraph(paragraph,timespend=1):
    paragraph=paragraph.split("\n")
    for countdown in range(len(paragraph)):
        print(paragraph[countdown])
        time.sleep(timespend)        

def CountDown(num_seconds=3):
    for countdown in reversed(range(num_seconds + 1)):
        if countdown > 0:
            sys.stdout.write('%s...' % countdown)
            sys.stdout.flush()
            time.sleep(1)
        else:
            print ('Go!')        

def move(y, x):
    print("\033[%d;%dH" % (y, x))            

def  printc(str_, y=0, x=0):
    if(y==0 and x==0):
        print(str_,end="'")
    else:
        print("\033[%d;%dH%s" % (y,x,str_),end="")     
Tools=["Vaccine","Shield","Health Potion"]
class Enemy:
    def __init__(self, name, attack_power, protection, hp):
        self.name = name
        self.attack_power = attack_power
        self.protection = protection
        self.hp = hp

    def attack(self, character):
        damage = self.attack_power - character.protection
        if character.action==1:
            damage=self.attack_power
        if damage>0:
            character.hp -= damage
            print(f"{self.name} attacked {character.name} and dealt {damage} damage.")
        time.sleep(2)
        if character.hp <= 0:
            print(f"Oh no! {character.name} has been defeated!")        
    
    def info(self):
        print(f'{self.name:15}: HP - {self.hp:9}|Attack Power:{self.attack_power:4}|Protect:{self.protection:4}')

class Character:
    def __init__(self, name, attack_power, protection, max_hp):
        self.name = name
        self.attack_power = attack_power
        self.protection = protection
        self.max_hp = max_hp
        self.hp = max_hp
        self.exp = 0
        self.level = 0
        self.action = 0 

    def attack(self, enemy):
        damage = self.attack_power - enemy.protection
        if damage>0 :
            enemy.hp -= damage
            print(f"{self.name} attacked {enemy.name} and dealt {damage} damage.")
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
        self.exp+=1    
        if self.exp>=10:
            self.level+=1
            self.exp=0
            self.attack_power+=3
            self.protection+=3

    def defend(self):
        print(f"{self.name} defended the attack.")

    def use_tool(self, tool): #change
        if tool == Tools[0]:
            self.attack_power += 3
            print(f"{self.name} used a vaccine. Attack power increased by 3.")
        elif tool == Tools[1]:
            self.protection += 3
            print(f"{self.name} used a shield. Protection increased by 3.")
        elif tool == Tools[2]:
            self.hp += 30
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f"{self.name} used a health potion. HP restored by 30.")

    def level_up(self):
        self.level += 1
        self.attack_power += 2
        self.protection += 2
        self.max_hp += 50
        self.hp = self.max_hp
        print(f"Congratulations! {self.name} leveled up to level {self.level}.")

    def info(self): 
        print(f"\n{self.name:15}: HP - {self.hp:4}/{self.max_hp:4}|Attack power:{self.attack_power:4}|Protect:{self.protection:4}|EXP:{self.exp:4} Level:{self.level:4}")       
        #print(f"{self.name} Attack power:{self.attack_power} Protect:{self.protection} HP:{self.hp} exp:{self.exp} level:{self.level}")


def battle(character, enemies):
    for enemy in enemies:
        ShowWords(f"\nA {enemy.name} has appeared!",0.2)
        while character.hp > 0 and enemy.hp > 0:
            os.system('cls')
            character.info()
            enemy.info()
            action = input("Choose your action: (1) Attack, (2) Defend, (3) Use tool: ")
            if action == "1":
                character.attack(enemy)
                character.action=1
            elif action == "2":
                character.defend()
                character.action=2
            elif action == "3":
                character.action=3
                tool = input(f"Choose a tool: (1) {Tools[0]}, (2) {Tools[1]}, (3) {Tools[2]}: ")
                if tool == "1":
                    character.use_tool(Tools[0])
                elif tool == "2":
                    character.use_tool(Tools[1]) #change
                elif tool == "3":
                    character.use_tool(Tools[2])
                else:
                    print("Invalid tool choice. Skipping turn.")
                    continue
            else:
                print("Invalid action choice. Skipping turn.")
                continue

            if enemy.hp <= 0:
                character.exp += 10
                print(f"You defeated the {enemy.name} and gained 10 EXP.")
                if character.exp>=10:
                    character.level+=1
                    character.exp=0
                    character.attack_power+=3
                    character.protection+=3
                break

            enemy.attack(character)
            
        if character.hp <= 0:
            print("\nGame over! You have been defeated.")
            return

        if character.exp >= 50:
            character.level_up()

    ShowWords("\nCongratulations! You have defeated all pathogen and won the game.",0.2)       
    input() 