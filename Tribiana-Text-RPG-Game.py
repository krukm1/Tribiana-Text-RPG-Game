# -*- coding: utf-8 -*-
"""
Created on Monday May 12th, 2025.

@author: Mateusz
"""
"""
This is a fantasy game where you design your character and fight a monster based on stats generated from your choices.
"""
import random

class Character:
    #Initial character with basic stats and attributes
    def __init__(self, name, race=None, char_class=None):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.strength = 10
        self.agility = 10
        self.health = 100

    #Display character name, race, class, and stats
    def display_stats(self):
        print(f"\n{self.name}'s Stats:")
        if self.race and self.race != "None":
            print(f"  Race: {self.race}")
        if self.char_class and self.char_class != "None":
            print(f"  Class: {self.char_class}")
        print(f"  Strength: {self.strength}")
        print(f"  Agility: {self.agility}")
        print(f"  Health: {self.health}/{self.health}")
    
    #Calculate and return random attack damage based on strength or agility
    def attack_damage(self):
        base = 5
        if self.strength > self.agility:
            low = base + self.strength // 2
            high = base + self.strength
        else:
            low = base + self.agility // 4
            high = base + self.agility
        return random.randint(low, high)

def character_creation():
    while True:
        #Get character name
        name = input("\nWhat is your character's name? ")
        
        #Loop for valid race choice
        while True:
            print("\nChoose your race:")
            print("1. Human")
            print("2. Orc")
            print("3. Elf")
            race_input = input("Enter the number or name of your race: ").strip().lower()
        
            if race_input == "1" or race_input == "human":
                print("\nHuman! A wise choice. Humans are versatile and resilient, their kingdoms vast and their ambition unmatched, shaping the world with ingenuity and unyielding spirit.")
                race = "Human"
                break
            elif race_input == "2" or race_input == "orc":
                print("\nOrc! An excellent pick. Born of thunder and fire, orcs wield brute strength and a warrior’s heart, feared across the lands for their might and unbreakable honor.")
                race = "Orc"
                break
            elif race_input == "3" or race_input == "elf":
                print("\nElf! A splendid selection. Elves are beings of ancient magic and grace, their ageless beauty and attunement to nature making them guardians of the mystical and eternal.")
                race = "Elf"
                break
            else:
                print("\nInvalid choice, please choose one of the available options.")
                
        #Loop for valid class choice
        while True:
            print("\nChoose your class:")
            print("1. Barbarian")
            print("2. Rogue")
            print("3. Knight")
            class_input = input("Enter the number or name of your class: ").strip().lower()
        
            if class_input == "1" or class_input == "barbarian":
                print("\nBarbarian! A fierce choice. The barbarian channels primal fury and raw strength, a storm of muscle and rage born from the wild frontiers of the world.")
                char_class = "Barbarian"
                break
            elif class_input == "2" or class_input == "rogue":
                print("\nRogue! A clever pick. Rogues move like shadows, striking from the dark with precision and cunning, masters of deception and silent blades.")
                char_class = "Rogue"
                break
            elif class_input == "3" or class_input == "knight":
                print("\nKnight! An honorable decision. The knight stands as a beacon of valor and discipline, clad in steel and bound by oath to defend the realm with unwavering courage.")
                char_class = "Knight"
                break
            else:
                print("\nERROR: Invalid choice, please choose one of the available options.")
                
        #Confirmation before final summary
        while True:
            print(f"\nName: {name}")
            print(f"Race: {race}")
            print(f"Class: {char_class}")
            confirm = input("\nAre you sure you want to keep these choices? (yes/no): ").strip().lower()
            
            if confirm == "yes":
                player = Character(name, race, char_class)
                
                #Apply race-based stat modifiers
                if race == "Human":
                    player.health += 25
                elif race == "Orc":
                    player.strength += 3
                elif race == "Elf":
                    player.agility += 3
                
                #Apply class-based stat modifiers
                if char_class == "Barbarian":
                    player.strength += 3
                    player.agility -= 2
                elif char_class == "Rogue":
                    player.agility += 3
                    player.strength -= 2
                elif char_class == "Knight":
                    player.health += 30
                    
                return player
            elif confirm == "no":
                print("\nLet's start over!")
                break
            else:
                print("\nERROR: Invalid entry. Please enter 'yes' or 'no'.")
    
def choose_monster():
    monsters = [
        Character("Goblin", "Goblin", "Warrior"),
        Character("Skeleton", "Undead", "Soldier"),
        Character("Troll", "Troll", "Brute"),
        Character("Zombie", "Undead", "Shambler"),
        Character("Werewolf", "Beast", "Hunter")
    ]
    
    for monster in monsters:
        #Give monster random stats to keep things interesting
        monster.strength += random.randint(1, 4)
        monster.agility += random.randint(1, 4)
        monster.health += random.randint(10, 25)

    print("\nChoose a monster to fight:")
    for i, monster in enumerate(monsters, 1):
        print(f"{i}. {monster.name}")

    while True:
        choice = input("Enter the number or name of the monster you want to fight: ").strip().lower()
        if choice.isdigit() and 1 <= int(choice) <= len(monsters):
            return monsters[int(choice) - 1]
        elif any(monster.name.lower() == choice for monster in monsters):
            return next(monster for monster in monsters if monster.name.lower() == choice)
        else:
            print("Invalid choice. Please enter a valid number or name of a monster.")
        
        
def battle(player, monster):
    print(f"\nPrepare for battle: {player.name} the {player.race} {player.char_class} vs {monster.name}!")
    
    while player.health > 0 and monster.health > 0:
        #Player's turn
        dmg = player.attack_damage()
        monster.health -= dmg
        print(f"\n{player.name} attacks {monster.name} for {dmg} damage! ({monster.health} HP left)")
        if monster.health <= 0:
            print(f"\nYou have defeated the {monster.name}! Congratulations, YOU WIN!")
            return

        #Monster's turn
        dmg = monster.attack_damage()
        player.health -= dmg
        print(f"{monster.name} attacks {player.name} for {dmg} damage! ({player.health} HP left)")
        if player.health <= 0:
            print(f"\nYou have been defeated by the {monster.name}... Better luck next time. GAME OVER!")
            return

def main():
    #Welcome message
    print("Welcome to world of Tribiana! This is a land where forgotten kingdoms and mythical creatures collide. Your destiny is yet unwritten, but every choice you make will shape the path ahead. Will you rise as a hero of legend, or fall into the shadows and have your name forgotten?\n\nForge your identity, challenge the monsters that lurk in the dark, and discover what lies beyond the horizon. Your adventure begins now. Choose wisely, for the world of Tribiana holds more than meets the eye.")
    player = character_creation()
    
    #Welcome message with player info
    print(f"\nWelcome, {player.name} the {player.race} {player.char_class}! Your journey in Tribiana begins now.")

    #Monster selection
    monster = choose_monster()
    print(f"\nYou have chosen to fight: {monster.name}!")
    
    #Display player stats
    player.display_stats()
    
    #Display monster stats
    monster.display_stats()
    
    #Prompt for battle
    while True:
        ready = input("\nAre you ready to battle? (yes/no): ").strip().lower()
        if ready == "yes":
            battle(player, monster)
            break
        elif ready == "no":
            print("\nYou flee into the forest, vowing to return stronger... or maybe switching career paths and becoming a baker.")
            break
        else:
            print("\nInvalid input. Please type 'yes' or 'no'.")
    
    # Allow the user to type "exit" to end the program
    while True:
        command = input("\nType 'exit' to end the program or 'restart' to play again: ").strip().lower()
        if command == "exit":
            print("\nThank you for playing Tribiana! Goodbye!")
            break
        elif command == "restart":
            main()  # Restart the game
            break
        else:
            print("\nInvalid input. Please type 'exit' or 'restart'.")

main()