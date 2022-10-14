'''
This is where the code for the attack class lives.
'''

class Attack:

    """ Class attacks take into account:

     damage: takes in int  

     the tipo: takes in a str

     pores: takes a int where pores = 0 if it's physical or pores = 1 if it's special  """


    def __init__(self, damage : int , tipo : str , pores : int):
        self.damage = damage
        self.tipo = tipo
        self.pores = pores

       
thdrblt = Attack(40, "Electric" , 1)




    





