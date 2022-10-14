'''
This is the main python file where the logic and practice for the fight simulator lives.

'''
from attack import Attack
from pokemon import Pokemon



thunderpunch = Attack(75, "Electric" , 0)
quickattack = Attack(40, "Normal" , 0)
megakick = Attack(120, "Normal" , 0)
dive = Attack(80, "Water" , 0) 
watergun = Attack(40, "Water" , 1)
magicleaf = Attack(60, "Grass" , 1)
gigadrain = Attack(75, "Grass" , 1)
firepunch = Attack(75, "Fire" , 0)
flamethrower = Attack(90, "Fire" , 1)
hurricane = Attack(110, "Flying" , 1)
wingattack = Attack(60, "Flying" , 0)
aerialace = Attack(60, "Flying" , 0)
tackle = Attack(40, "Normal" , 0)
assurance = Attack(60, "Dark", 0)
covet = Attack(60, "Normal", 0)
gigaimpact = Attack(150, "Normal", 0)
lick = Attack(30, "Ghost", 0)
disarmingvoice = Attack(40, "Fairy", 1)
pound = Attack(40, "Normal", 0)
icepunch = Attack(75, "Ice", 0)
drainpunch = Attack(75, "Fighting", 0)
extremespeed = Attack(80, "Normal", 0)
dragontail = Attack(60, "Dragon", 0)
outrage = Attack(120, "Dragon", 0)



bulbasaur = Pokemon([105, 48, 48, 63, 63, 45], 'grass')
charmander = Pokemon([99, 51, 43, 58, 49, 63], 'fire')
squirtle = Pokemon([104, 47, 63, 49, 62, 43], 'water')
pidgeot = Pokemon([143, 76, 72, 67, 67, 86], 'flying')
rattata = Pokemon([90, 54, 36, 27, 36, 69], 'normal')
pikachu = Pokemon([95, 54, 31, 49, 40, 85], 'electric')
jigglypuff = Pokemon([175, 45, 22, 45, 27, 22], 'normal')
abra = Pokemon([85, 22, 18, 99, 54, 85], 'psychic')
snorlax = Pokemon([220, 103, 63, 63, 103, 31 ], 'normal')
dragonite = Pokemon([151, 125, 90, 94, 94, 76 ], 'dragon')
    
