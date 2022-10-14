'''
This is where the code for the attack class lives.
'''

class Attack:

    """ Class attacks take into account:

     name: str, the name of the attack

     damage: takes in int  

     tipo: takes in a str

     pores: takes a int where pores = 0 if it's physical or pores = 1 if it's special  """


    def __init__(self, name: str, damage : int , tipo : str , pores : int):
        self.name = name
        self.damage = damage
        self.tipo = tipo
        self.pores = pores

