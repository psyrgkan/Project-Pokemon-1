"""This is the main python file where the logic and practice for the fight simulator lives.
"""
from attack import Attack
from pokemon import Pokemon
import pokeinfo
import random
import copy


def get_effectiveness(att: Attack, pkm_def: Pokemon):
    """This calculates the effectiveness of a given move on a defending pokemon
    
    Args:
        att (Attack): The Attack that is being used
        pkm_def (Pokemon): The Pokemon that is defending the attack

    Returns:
        int: 0 if not effective, 0.5 is not very effective, 1 if normal, 2 if super
    """
    att_indx = pokeinfo.pkm_tipos.index(att.tipo)
    def_indx = pokeinfo.pkm_tipos.index(pkm_def.tipo)
    effect = pokeinfo.ef_arr[att_indx][def_indx]

    if effect == 2:
        print(att.name + " is super effective against " + pkm_def.name +"!")
    if effect == 1/2:
        print(att.name + " is not very effective against " + pkm_def.name)
    if effect == 0:
        print(att.name + " does not have an effect on " + pkm_def.name)

    return effect


def calculate_dmg(att: Attack, pkm_att: Pokemon, pkm_def: Pokemon):
    """Calculates the damage of a given attacking move from an attacking pokemon
    to the respective defending pokemon based on Gen I damage formula

    Args:
        att (Attack): The Attack that is being used
        pkm_att (Pokemon): The Pokemon that is attacking
        pkm_def (Pokemon): The Pokemon that is defending

    Returns:
        int: Returns the damage to be inflicted
    """
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


def single_attack(pkm_att: Pokemon, pkm_def: Pokemon, att: Attack):
    """This function is used to perform a single attack

    Args:
        pkm_att (Pokemon): The Pokemon that is attacking
        pkm_def (Pokemon): The Pokemon that is defending
        att (Attack): The Attack that is being used
    """
    print("\n"+pkm_att.name + " hit " + pkm_def.name + " with " + att.name)
    dmg0 = calculate_dmg(att, pkm_att, pkm_def)
    pkm_def.hp -= dmg0
    return


def attacking_round(pkm_first: Pokemon, pkm_second: Pokemon, att_first: Attack, att_second: Attack):
    """This function is used to perform a round of 2 attacks

    Args:
        pkm_first (Pokemon): The Pokemon that attacks first
        pkm_second (Pokemon): The Pokemon that attacks second
        att_first (Attack): The Attack that is being used first
        att_second (Attack): The Attack that is being used second
    """
    single_attack(pkm_first, pkm_second, att_first)
    if pkm_second.hp <= 0:
        return
    single_attack(pkm_second, pkm_first, att_second)
    return


if __name__ == '__main__': 
    print([i.name for i in pokeinfo.available_pkm])

    pkm0 = None
    pkm1 = None

    # Ask players to choose PokeMon
    while pkm0 == None:
        pkm0name = input("Player 1, enter a valid fighter: ").lower()

        for i in pokeinfo.available_pkm:
            if pkm0name == i.name.lower():
                pkm0 = copy.deepcopy(i)
                break

    while pkm1 == None:
        pkm1name = input("Player 2, enter a valid fighter: ").lower()

        for i in pokeinfo.available_pkm:
            if pkm1name == i.name.lower():
                pkm1 = copy.deepcopy(i)
                break

    # Choose 4 random moves for each PokeMon given their available moves
    pkm0.moveset = [pkm0.allmoves.pop(random.randrange(len(pkm0.allmoves))) for i in range(4)]
    pkm1.moveset = [pkm1.allmoves.pop(random.randrange(len(pkm1.allmoves))) for i in range(4)]

    print("\n"+pkm0.name + " has the following moves:")
    print([(i.name, i.tipo, i.damage) for i in pkm0.moveset])

    print(pkm1.name + " has the following moves:")
    print([(i.name, i.tipo, i.damage) for i in pkm1.moveset])

    # Fight start
    while pkm0.hp > 0 and pkm1.hp > 0:

        att0 = None
        att1 = None

        # Ask for attacks
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

        # Fastest PokeMon attacks first
        if pkm0.stats[5] > pkm1.stats[5]:
            attacking_round(pkm0, pkm1, att0, att1)
        else:
            attacking_round(pkm1, pkm0, att1, att0)

        # Check if alive and print info accordingly
        if pkm0.hp >0 and pkm1.hp > 0:
            print("\n"+pkm0.name + " has remaining HP: " + str(pkm0.hp) + "/" +str(pkm0.stats[0]))
            print(pkm1.name + " has remaining HP: " + str(pkm1.hp)+ "/" +str(pkm1.stats[0]))
            print("_________________________________________________")
            print("\n"+pkm0.name + " has the following moves:")
            print([(i.name, i.tipo, i.damage) for i in pkm0.moveset])
            print(pkm1.name + " has the following moves:")
            print([(i.name, i.tipo, i.damage) for i in pkm1.moveset])

    # If PokeMon is dead announce winner
    if pkm0.hp < 0:
        print("\n"+pkm0.name + " has fainted!")
        print("Winner is " + pkm1.name + "!")
    else:
        print("\n"+pkm1.name + " has fainted!")
        print("Winner is " + pkm0.name + "!")