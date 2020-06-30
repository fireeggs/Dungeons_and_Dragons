# -*- coding: utf-8 -*-

'''
    Dungeons and Fighters 

    Task: This file contains the Hero class that stores all pertinent information about the game's hero,including hit points, strength and items. 
          It is a Model file. You will notice that Hero inherits from Tile. 
          That is because our hero will be one of the things that could occupy a tile in a room.
    
    hero.py

    Created by Seungkyu Kim on Apr 30, 2016
    Copyright 2016 Seungky Kim. All rights reserved.

'''


from tile import *


class Hero(Tile):
    '''A class representing the hero venturing into the dungeon.
    Heroes have the following attributes: a name, a list of items,
    hit points, strength, gold, and a viewing radius. Heroes
    inherit the visible boolean from Tile.'''

    def __init__(self):
        '''(Hero) -> NoneType
        Create a new hero with name name,
        an empty list of items and bonuses to
        hp, strength, gold and radius as specified
        in bonuses'''

        self.bonuses = (0, 0, 0)
        self.items = []
        self.hp = 10 + self.bonuses[0]
        self.strength = 3 + self.bonuses[1]
        self.radius = 1 + self.bonuses[2]
        Tile.__init__(self, True)

    def symbol(self):
        '''(Hero) -> str
        Return the map representation symbol of Hero: O.'''

        #return "\u263b"
        return "O"

    def __str__(self):
        '''(Item) -> str
        Return the Hero's name.'''

        return "{}\nHP:{:2d} STR:{:2d} RAD:{:2d}\n".format(
                    self.name, self.hp, self.strength, self.radius)

    def take(self, item):
        '''ADD SIGNATURE HERE
        Add item to hero's items
        and update their stats as a result.'''

        # IMPLEMENT TAKE METHOD HERE
        self.items.append(item.name)
        self.hp += item.hp
        self.strength += item.strength
        self.radius += item.radius

    def fight(self, baddie):
        '''ADD SIGNATURE HERE -> str
        Fight baddie and return the outcome of the
        battle in string format.'''

        # Baddie strikes first
        # Until one opponent is dead
            # attacker deals damage equal to their strength
            # attacker and defender alternate
        situation = True
        while situation:
            self.hp -= baddie.strength
            if self.hp <= 0:
                situation = False
            baddie.hp -= self.strength
            if baddie.hp <= self.strength:
                situation = False
        if self.hp < 0:
            return "Killed by %s" % baddie.name
        return "Defeated %s" % baddie.name


class Rogue(Hero):
    '''A new hero, Rogue, inherited from its parent class, Hero.'''

    def __init__(self):
        '''(Rogue) -> NoneType
        Initialize settings of a new hero, Rogue,
        with inherited settings from parent class, Hero.'''

        Hero.__init__(self)
        self.name = "Rogue"
        self.items = []
        self.hp = 10 + self.bonuses[0]
        self.strength = 2 + self.bonuses[1]
        self.radius = 2 + self.bonuses[2]


class Barbarian(Hero):
    '''A new hero, Barbarian, inherited from its parent class, Hero.'''

    def __init__(self):
        '''(Barbarian) -> NoneType
        Initialize settings of a new hero, Barbarian,
        with inherited settings from parent class, Hero.'''

        Hero.__init__(self)
        self.name = "Barbarian"
        self.items = []
        self.hp = 12 + self.bonuses[0]
        self.strength = 3 + self.bonuses[1]
        self.radius = 1 + self.bonuses[2]


class Mage(Hero):
    '''A new hero, Mage, inherited from its parent class, Hero.'''

    def __init__(self):
        '''(Mage) -> NoneType
        Initialize settings of a new hero, Mage,
        with inherited settings from parent class, Hero.'''

        Hero.__init__(self)
        self.name = "Mage"
        self.items = []
        self.hp = 8 + self.bonuses[0]
        self.strength = 2 + self.bonuses[1]
        self.radius = 3 + self.bonuses[2]
