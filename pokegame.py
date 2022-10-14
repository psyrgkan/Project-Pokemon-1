'''
This is the main python file where the logic and practice for the fight simulator lives.

'''
from attack import Attack
from pokemon import Pokemon
import random


# Create Attacks and Pokemon

thunderpunch = Attack('Thunder Punch', 75, "Electric" , 0)
quickattack = Attack('Quick Attack', 40, "Normal" , 0)
megakick = Attack('Megakick', 120, "Normal" , 0)
dive = Attack('Dive', 80, "Water" , 0) 
watergun = Attack('Watergun', 40, "Water" , 1)
magicleaf = Attack('Magic Leaf', 60, "Grass" , 1)
gigadrain = Attack('Gigadrain', 75, "Grass" , 1)
firepunch = Attack('Fire Punch', 75, "Fire" , 0)
flamethrower = Attack('Flamethrower', 90, "Fire" , 1)
hurricane = Attack('Hurricane', 110, "Flying" , 1)
wingattack = Attack('Wingattack', 60, "Flying" , 0)
aerialace = Attack('Aerial Ace', 60, "Flying" , 0)
tackle = Attack('Tackle', 40, "Normal" , 0)
assurance = Attack('Assurance', 60, "Dark", 0)
covet = Attack('Covet', 60, "Normal", 0)
gigaimpact = Attack('Giga Impact', 150, "Normal", 0)
lick = Attack('Lick', 30, "Ghost", 0)
disarmingvoice = Attack('Disarming Voice', 40, "Fairy", 1)
pound = Attack('Pound', 40, "Normal", 0)
icepunch = Attack('Ice Punch', 75, "Ice", 0)
drainpunch = Attack("Drain puch", 75, "Fighting", 0)
extremespeed = Attack("Extreme speed", 80, "Normal", 0)
dragontail = Attack("Dragon tail", 60, "Dragon", 0)
outrage = Attack("Out rage" , 120, "Dragon", 0)

bulbasaur = Pokemon('Bulbasaur', [105, 48, 48, 63, 63, 45], 'grass', [gigadrain, quickattack, drainpunch, magicleaf, tackle, gigaimpact])
charmander = Pokemon('Charmander', [99, 51, 43, 58, 49, 63], 'fire', [firepunch, flamethrower, tackle, gigaimpact, assurance, dragontail])
squirtle = Pokemon('Squirtle', [104, 47, 63, 49, 62, 43], 'water', [dive, quickattack, watergun, covet, icepunch])
pidgeot = Pokemon('Pidgeot', [143, 76, 72, 67, 67, 86], 'flying', [quickattack, hurricane, wingattack, aerialace, pound])
rattata = Pokemon('Rattata', [90, 54, 36, 27, 36, 69], 'normal', [quickattack, tackle, assurance, covet, extremespeed])
pikachu = Pokemon('Pikachu', [95, 54, 31, 49, 40, 85], 'electric',[thunderpunch,quickattack,outrage,hurricane,megakick,magicleaf,disarmingvoice])
jigglypuff = Pokemon('Jigglypuff', [175, 45, 22, 45, 27, 22], 'normal',[tackle,assurance,flamethrower,quickattack,hurricane,tackle])
abra = Pokemon('Abra', [85, 22, 18, 99, 54, 85], 'psychic',[disarmingvoice,assurance,tackle,wingattack,quickattack,lick])
snorlax = Pokemon('Snorlax', [220, 103, 63, 63, 103, 31 ], 'normal', [pound,covet,tackle,megakick,gigaimpact,hurricane,outrage])
dragonite = Pokemon('Dragonite', [151, 125, 90, 94, 94, 76 ], 'dragon', [outrage,gigaimpact,pound,covet,dragontail,magicleaf])

pokelist = [bulbasaur, charmander, squirtle, pidgeot, rattata, pikachu, jigglypuff, abra, snorlax, dragonite]

# Main code logic

player_counter = 0

print([i.name for i in pokelist])

pkm0 = None
pkm1 = None

while pkm0 == None:
    pkm0name = input("Player 1, choose your fighter: ").lower()

    for i in pokelist:
        if pkm0name == i.name.lower():
            pkm0 = i
            break

while pkm1 == None:
    pkm1name = input("Player 2, choose your fighter: ").lower()

    for i in pokelist:
        if pkm1name == i.name.lower():
            pkm1 = i
            break

for i in range(4):
    rand_idx = random.randrange(len(pkm0.allmoves))
    pkm0.moveset.append(pkm0.allmoves.pop(rand_idx))

print(pkm0.name + " has the following moves:")
print([i.name for i in pkm0.moveset])
    

for i in range(4):
    rand_idx = random.randrange(len(pkm1.allmoves))
    pkm1.moveset.append(pkm1.allmoves.pop(rand_idx))

print(pkm1.name + " has the following moves:")
print([i.name for i in pkm1.moveset])