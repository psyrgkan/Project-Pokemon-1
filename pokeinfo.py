from attack import Attack
from pokemon import Pokemon

# Type effectiveness chart/array
pkm_tipos = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

# A 2 Dimenstional Array Of Damage Multipliers For Attacking Pokemon:
ef_arr = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],[1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
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
            [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]]

# Create Attacks 
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

# Create Pokemon
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

available_pkm = [bulbasaur, charmander, squirtle, pidgeot, rattata, pikachu, jigglypuff, abra, snorlax, dragonite]