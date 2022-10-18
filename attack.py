class Attack:
    """The class with Attack information

    Attributes:

        name (str): Name of the attack
        damage (int): Damage of the attack
        tipo (str): Type of the attack
        pores (int): pores = 0 if attack is physical or pores = 1 if it is special  
    """
    def __init__(self, name: str, damage : int , tipo : str , pores : int):
        self.name = name
        self.damage = damage
        self.tipo = tipo
        self.pores = pores

