'''
This is the main python file where the logic and practice for the fight simulator lives.

'''
from curses import def_prog_mode
from attack import Attack
from pokemon import Pokemon
import random
import copy
import numpy as np

# Type effectiveness chart/array
pkm_tipos = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

# A 2 Dimenstional Numpy Array Of Damage Multipliers For Attacking Pokemon:

ef_arr = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]])

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

bulbasaur = Pokemon('Bulbasaur', [105, 48, 48, 63, 63, 45], 'Grass', [gigadrain, quickattack, drainpunch, magicleaf, tackle, gigaimpact])
charmander = Pokemon('Charmander', [99, 51, 43, 58, 49, 63], 'Fire', [firepunch, flamethrower, tackle, gigaimpact, assurance, dragontail])
squirtle = Pokemon('Squirtle', [104, 47, 63, 49, 62, 43], 'Water', [dive, quickattack, watergun, covet, icepunch])
pidgeot = Pokemon('Pidgeot', [143, 76, 72, 67, 67, 86], 'Flying', [quickattack, hurricane, wingattack, aerialace, pound])
rattata = Pokemon('Rattata', [90, 54, 36, 27, 36, 69], 'Normal', [quickattack, tackle, assurance, covet, extremespeed])
pikachu = Pokemon('Pikachu', [95, 54, 31, 49, 40, 85], 'Electric',[thunderpunch,quickattack,outrage,hurricane,megakick,magicleaf,disarmingvoice])
jigglypuff = Pokemon('Jigglypuff', [175, 45, 22, 45, 27, 22], 'Normal',[tackle,assurance,flamethrower,quickattack,hurricane,tackle])
abra = Pokemon('Abra', [85, 22, 18, 99, 54, 85], 'Psychic',[disarmingvoice,assurance,tackle,wingattack,quickattack,lick])
snorlax = Pokemon('Snorlax', [220, 103, 63, 63, 103, 31 ], 'Normal', [pound,covet,tackle,megakick,gigaimpact,hurricane,outrage])
dragonite = Pokemon('Dragonite', [151, 125, 90, 94, 94, 76 ], 'Dragon', [outrage,gigaimpact,pound,covet,dragontail,magicleaf])

pokelist = [bulbasaur, charmander, squirtle, pidgeot, rattata, pikachu, jigglypuff, abra, snorlax, dragonite]

def get_effectiveness(att: Attack, pkm_def: Pokemon):
    att_indx = pkm_tipos.index(att.tipo)
    def_indx = pkm_tipos.index(pkm_def.tipo)
    effect = ef_arr[att_indx][def_indx]
    if effect == 2:
        print(att.name + " is super effective against " + pkm_def.name +"!")
    if effect == 1/2:
        print(att.name + " is not very effective against " + pkm_def.name)
    return effect

def calculate_dmg(att: Attack, pkm_att: Pokemon, pkm_def: Pokemon):
    dmg = ((2*50/5) + 2) * att.damage 

    if att.pores == 0:
        dmg = (dmg * pkm_att.stats[1] / pkm_def.stats[2])/50 + 2

    if att.pores == 1:
        dmg = (dmg * pkm_att.stats[3] /pkm_def.stats[4])/50 + 2

    if att.tipo.lower() == pkm_att.tipo.lower():
        dmg = dmg * 1.5

    dmg = dmg * get_effectiveness(att, pkm_def)
    dmg = dmg * random.randrange(217, 255) /255
    return int(dmg)

# Main code logic

if __name__ == '__main__': 
    print([i.name for i in pokelist])

    pkm0 = None
    pkm1 = None

    while pkm0 == None:
        pkm0name = input("Player 1, enter a valid fighter: ").lower()

        for i in pokelist:
            if pkm0name == i.name.lower():
                pkm0 = copy.deepcopy(i)
                break

    while pkm1 == None:
        pkm1name = input("Player 2, enter a valid fighter: ").lower()

        for i in pokelist:
            if pkm1name == i.name.lower():
                pkm1 = copy.deepcopy(i)
                break

    for i in range(4):
        rand_idx = random.randrange(len(pkm0.allmoves))
        pkm0.moveset.append(pkm0.allmoves.pop(rand_idx))

    print("\n"+pkm0.name + " has the following moves:")
    print([(i.name, i.damage) for i in pkm0.moveset])
        

    for i in range(4):
        rand_idx = random.randrange(len(pkm1.allmoves))
        pkm1.moveset.append(pkm1.allmoves.pop(rand_idx))

    print(pkm1.name + " has the following moves:")
    print([(i.name, i.damage) for i in pkm1.moveset])

    while pkm0.hp > 0 and pkm1.hp > 0:
        # player1 picks attack
        att0 = None
        att1 = None

        while att0 == None:
            att0name = input("\n"+"Player 1 pick a valid move: ").lower()

            for i in pkm0.moveset:
                if att0name == i.name.lower():
                    att0 = i
                    break

        while att1 == None:
            att1name = input("Player 2 pick a valid move: ").lower()

            for i in pkm1.moveset:
                if att1name == i.name.lower():
                    att1 = i
                    break

        if pkm0.stats[5] > pkm1.stats[5]:
            print("\n"+pkm0.name + " hit " + pkm1.name + " with " + att0.name)
            dmg0 = calculate_dmg(att0, pkm0, pkm1)
            pkm1.hp -= dmg0
            if pkm1.hp <= 0:
                break
            print(pkm1.name +  " hit " + pkm0.name + " with " + att1.name)
            dmg1 = calculate_dmg(att1, pkm1, pkm0)
            pkm0.hp -= dmg1

        else:
            print("\n"+ pkm1.name +  " hit " + pkm0.name + " with " + att1.name)
            dmg1 = calculate_dmg(att1, pkm1, pkm0)
            pkm0.hp -= dmg1
            if pkm0.hp <= 0:
                break
            print(pkm0.name + " hit " + pkm1.name + " with " + att0.name)
            dmg0 = calculate_dmg(att0, pkm0, pkm1)
            pkm1.hp -= dmg0

        if pkm0.hp >0 and pkm1.hp > 0:
            print("\n"+pkm0.name + " has remaining HP: " + str(pkm0.hp) + "/" +str(pkm0.stats[0]))
            print(pkm1.name + " has remaining HP: " + str(pkm1.hp)+ "/" +str(pkm1.stats[0]))
            print("_________________________________________________")
            print("\n"+pkm0.name + " has the following moves:")
            print([(i.name, i.tipo, i.damage) for i in pkm0.moveset])
            print(pkm1.name + " has the following moves:")
            print([(i.name, i.tipo, i.damage) for i in pkm1.moveset])


    if pkm0.hp < 0:
        print("\n"+pkm0.name + " has fainted!")
        print("Winner is " + pkm1.name + "!")
    else:
        print("\n"+pkm1.name + " has fainted!")
        print("Winner is " + pkm0.name + "!")
