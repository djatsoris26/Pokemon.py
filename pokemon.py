import time
import numpy as np
import sys

# Special slow typing thingie

def delay_print(s):
    # this is gonna be for printing one character at a time
    # Like the original Red, Blue, and Yellow did :P
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Creating the class of the pokemon btw this is so fucking annoying
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # saving variables as attributes or as michael reeves likes to say "That's a lot of buzz words. You don't care about buzz words."
        self.name = name
        self.types = types
        self.moves = moves 
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # the amount of health a pokemon has ;-;


    def fight(self, Pokemon2):
        # This is the piece of code that allows the pokemon to fight (I think)

        # Printing the fight info stuff, also my computer sucks and it doesn't like using vscode
        print(f"A wild {Pokemon2.name} Appeared!") # I honestly don't know if I spelt appeared right
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 50*2)
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 25*2+10)

        time.sleep(2)

        # this part of the code is where the type advantages are.
        # If you don't know what type advantages are, blastoise is water type, charizard is fire type, blastoise has the advantage bc ya know,water puts out fire.
        # in pokemon, theres a bajillion types. In this, there's going to be 3
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # if both pokemon are same type
                if Pokemon2.types == k:
                    string_1_attack = 'Its not very effective...'
                    string_2_attack = 'Its not very effective...'

                # this next bit of code will be if Pokemon2's move is type is super effective. 
                # oh yeah, did I mention that all moves are the same type as the pokemon?
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /- 2
                    string_1_attack = 'Its not very effective...'
                    string_2_attack = 'Its super effective!'

                # This will be if Pokemon 2 isn't very effective. I'm going to have an aneurysm
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = 'Its super effective!'
                    string_2_attack = 'Its not very effective...'


        # Now it's finally time for the goddamn fighting what took so fucking long jesus christ
        # Continue if the pokemon still are alive
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # This is where its gonna say the health of the pokemon
            print(f" {self.name}\t\tHLTH\t{self.health}")
            print(f" {Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move'))
            delay_print(f"{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # This is how we're going to determine the damage. Kill me
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back the bars plus a little defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="


            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Checking to see if the pokemon died- I MEAN FAINTED
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break
            
            # It's pokemon2s turn now

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move'))
            delay_print(f"{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # This is how we're going to determine the damage. Kill me
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back the bars plus a little defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="


            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Checking to see if the pokemon died- I MEAN FAINTED
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(5000)
        delay_print(f"Opponent paid you ${money}.")






if __name__ == '__main__':
    # Let's finally create pokemon. Fucking Finally
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Brave Bird', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Rage', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK': 10, 'DEFENSE': 10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK': 8,'DEFENSE': 12})

    Charmander = Pokemon('Charamander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubble', 'Tackle', 'Headbutt', 'Surf',],{'ATTACK':3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bublasaur', 'Grass', ['Vine Wip', 'Tackle', 'Take Down', 'Razor Leaf'], {'ATTACK':2, 'DEFENSE':4})
    
    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Spin'], {'ATTACK':6, 'DEFENSE': 5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun' 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE': 5})
    Ivysaur = Pokemon('Ivysaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Mega Drain', 'Take Down'], {'ATTACK':4, 'DEFENSE':6})
