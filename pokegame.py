'''
This is the main python file where the logic and practice for the fight simulator lives.

'''
from attack import Attack
from pokemon import Pokemon



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
drainpunch = Attack(75, "Fighting", 0)
extremespeed = Attack(80, "Normal", 0)
dragontail = Attack(60, "Dragon", 0)
outrage = Attack(120, "Dragon", 0)



bulbasaur = Pokemon([105, 48, 48, 63, 63, 45], 'grass', [gigadrain, quickattack, drainpunch, magicleaf, tackle, gigaimpact])
charmander = Pokemon([99, 51, 43, 58, 49, 63], 'fire', [firepunch, flamethrower, tackle, gigaimpact, assurance, dragontail])
squirtle = Pokemon([104, 47, 63, 49, 62, 43], 'water', [dive, quickattack, watergun, covet, icepunch])
pidgeot = Pokemon([143, 76, 72, 67, 67, 86], 'flying', [quickattack, hurricane, wingattack, aerialace, pound])
rattata = Pokemon([90, 54, 36, 27, 36, 69], 'normal', [quickattack, tackle, assurance, covet, extremespeed])
pikachu = Pokemon([95, 54, 31, 49, 40, 85], 'electric')
jigglypuff = Pokemon([175, 45, 22, 45, 27, 22], 'normal')
abra = Pokemon([85, 22, 18, 99, 54, 85], 'psychic')
snorlax = Pokemon([220, 103, 63, 63, 103, 31 ], 'normal')
dragonite = Pokemon([151, 125, 90, 94, 94, 76 ], 'dragon')
    
