class Character:
    'represents characters in the game'
    def __init__(self, name, lvl=1, health_pts=100, attack_level=10, defense_level=1, exp):
    #def __init__(self, name, price, taxable):
	'initialize character'
	self.name = name
	self.lvl = level
	self.hp = health_pts
	self.at = attack_level
	self.df = defense_level
	self.exp = exp

    def setlvl(self, new_level):
	'set health level '
	self.lvl = new_level


    def sethp(self, new_level):
	'set health point '
	self.hp = new_level

