'''
Anik Patel
May 16th, 2018
R. Vincent, instructor
Final Project - PyGame game
'''

import random

class Player():
    '''Sets up a class for the player's character.
       This class also sets up the moves they can do during their turn'''
    def __init__(self, name, Id, atckph, atcksp, stdef, spd, pktype):
        '''Sets up playable character and its stats: attack, defense and speed'''
        self.health = 100
        self.heallimit = 5
        self.name = name
        self.id = Id
        self.atckph = atckph
        self.atcksp = atcksp
        self.defense = stdef
        self.speed = spd
        self.type = pktype


    def physical(self, other):
        '''An attack with physical contact'''
        phymoves = ('Slash','Crunch','Dragon Claw')
        usedmove = phymoves[self.id]

        temphealth = other.health

        #These moves have no type advantages against the characters available
        typeeff = 1

        #Random 10% chance of missing the attack
        accuracy = random.randrange(10)
        if accuracy != 0:
            accuracy = 1

        other.health -= int(((((22)*((self.atckph)/(other.defense))))+2)*((typeeff)*(accuracy)))

        if other.health <0:
            other.health = 0

    def special(self,other):
        '''A move without contact'''
        #Character ID will determine the move being used
        specmoves = ('Flamethrower','Surf','Energy Ball')
        usedmove = specmoves[self.id]

        temphealth = other.health

        #Gives a x2 damage multiplier if type is super effective and x1/2 damage mutiplier if type is not very effective (using Pokemon type effectiveness)
        if self.id == 0 and other.id == 2:
            typeeff = 2
        elif self.id == 1 and other.id == 0:
            typeeff = 2
        elif self.id == 2 and other.id == 1:
            typeeff = 2
        elif self.id == 2 and other.id == 0:
            typeeff = 0.5
        elif self.id == 0 and other.id == 1:
            typeeff = 0.5
        elif self.id == 1 and other.id == 2:
            typeeff = 0.5
        else:
            typeeff = 1

        #Random 10% chance of missing the attack
        accuracy = random.randrange(10)
        if accuracy != 0:
            accuracy = 1

        other.health -= int(((((22)*(self.atcksp/other.defense)))+2)*(typeeff*accuracy))

        if other.health <0:
            other.health = 0

    def heal(self):
        '''Restores half of the current health left'''
        healmove = ('Roost','Eat Berry','Synthesis')

        temphealth = self.health

        #Limits the total amount of time any character can heal to 5 times (just like healing moves in Pokemon)
        if self.heallimit > 0:
            self.heallimit -= 1
            self.health += self.health//2
        else:
            None

        if self.health > 100:
            self.health = 100

class Enemy():
    '''Sets up a class for the player's character.
       This class also sets up the moves they can do during their turn'''
    def __init__(self, name, Id, atckph, atcksp, stdef, spd, pktype):
        '''Sets up playable character and its stats: attack, defense and speed'''
        self.health = 100
        self.heallimit = 5
        self.name = name
        self.id = Id
        self.atckph = atckph
        self.atcksp = atcksp
        self.defense = stdef
        self.speed = spd
        self.type = pktype


    def physical(self, other):
        '''An attack with physical contact'''
        phymoves = ('Slash','Crunch','Dragon Claw')
        usedmove = phymoves[self.id]

        temphealth = other.health

        #These moves have no type advantages against the characters available
        typeeff = 1

        #Random 10% chance of missing the attack
        accuracy = random.randrange(10)
        if accuracy != 0:
            accuracy = 1

        other.health -= int(((((22)*((self.atckph)/(other.defense))))+2)*((typeeff)*(accuracy)))

        if other.health <0:
            other.health = 0

    def special(self,other):
        '''A move without contact'''
        #Character ID will determine the move being used
        specmoves = ('Flamethrower','Surf','Energy Ball')
        usedmove = specmoves[self.id]

        temphealth = other.health

        #Gives a x2 damage multiplier if type is super effective and x1/2 damage mutiplier if type is not very effective (using Pokemon type effectiveness)
        if self.id == 0 and other.id == 2:
            typeeff = 2
        elif self.id == 1 and other.id == 0:
            typeeff = 2
        elif self.id == 2 and other.id == 1:
            typeeff = 2
        elif self.id == 2 and other.id == 0:
            typeeff = 0.5
        elif self.id == 0 and other.id == 1:
            typeeff = 0.5
        elif self.id == 1 and other.id == 2:
            typeeff = 0.5
        else:
            typeeff = 1

        #Random 10% chance of missing the attack
        accuracy = random.randrange(10)
        if accuracy != 0:
            accuracy = 1

        other.health -= int(((((22)*(self.atcksp/other.defense)))+2)*(typeeff*accuracy))

        if other.health <0:
            other.health = 0

    def heal(self):
        '''Restores half of the current health left'''
        healmove = ('Roost','Eat Berry','Synthesis')

        temphealth = self.health

        #Limits the total amount of time any character can heal to 5 times (just like healing moves in Pokemon)
        if self.heallimit > 0:
            self.heallimit -= 1
            self.health += self.health//2
        else:
            None

        if self.health > 100:
            self.health = 100
