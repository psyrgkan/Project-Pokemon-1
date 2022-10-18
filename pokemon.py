from attack import Attack

class Pokemon:
    """The class with PokeMon information

    Attributes:

        name (str): Name of pokemon
        stats (list[int]): Stats[0] is HP, stats[1] is Attack, stats[2] is Defence,
            stats[3] is Special Attack, stats[4] is Special Defence and stats[5] is Speed
        tipo (str): Gives the type of the pokemon in str format ('water', 'fire', 'flying', etc.)
        attacks (list[Attack]): Gives the list of all possible attacks a pokemon can learn
    """
    def __init__(self, name: str, stats: list, tipo: str, attacks: list[Attack] = []):
        self.name = name
        self.stats = stats
        self.tipo = tipo
        self.hp = stats[0]
        self.allmoves = attacks
        self.moveset = []
