# -*- coding: utf-8 -*-

'''
    Dungeons and Fighters 

    Task: This file contains the Tile class that represents an empty tile on the room floor.
          The list in the Room class actually stores Tile objects. 
          It also contains a subclass of Tile called Wall that represents an impenetrable wall. 
          It is a Model file as it contains no behaviour, only blueprints for some simple objects that might populate the room.
    
    tile.py

    Created by Seungkyu Kim on Apr 30, 2016
    Copyright 2016 Seungky Kim. All rights reserved.

'''


class Tile:
    '''Anything that takes up one square tile on the map.
    The default tile is empty space.'''

    def __init__(self, vis=False):
        '''(Tile, bool, bool) -> NoneType
        Construct a new tile. If penetrate is True,
        the tile can be stepped on by the Hero.
        self.visible is set to True once the Hero
        has uncovered that tile.'''

        self.visible = vis

    def symbol(self):
        '''(Tile) -> str
        Return the map representation symbol for Tile.'''

        return " "


class Wall(Tile):
    '''A subclass of Tile that represents an impassable wall.'''

    def __init__(self):
        '''(Wall) -> NoneType
        Construct an impenetrable Tile'''

        Tile.__init__(self)

    def symbol(self):
        '''(Wall) -> str
        Return the map representation symbol for Wall: X.'''

        #return "\u2588"
        return "X"


class Item(Tile):
    '''A subclass of Tile that represents an impassable item.'''

    def __init__(self, name, hp, strength, radius, x_cord, y_cord):
        '''(item) -> NoneType
        Construct an impenetrable Item'''

        Tile.__init__(self)
        self.name = name
        self.hp = hp
        self.strength = strength
        self.radius = radius
        self.x_cord = x_cord
        self.y_cord = y_cord

    def symbol(self):
        '''(Item) -> str
        Return the map representation symbol for Item: I.'''

        #return "\u2588"
        return "I"


class Monster(Tile):
    '''A subclass of Tile that represents an impassable Monster.'''

    def __init__(self, name, hp, strength, x_cord, y_cord):
        '''(Monster) -> NoneType
        Construct an impenetrable Monster'''

        Tile.__init__(self)
        self.name = name
        self.hp = hp
        self.strength = strength
        self.x_cord = x_cord
        self.y_cord = y_cord

    def symbol(self):
        '''(Monster) -> str
        Return the map representation symbol for Monster: M.'''

        #return "\u2588"
        return "M"


class Door(Tile):
    '''A subclass of Tile that represents an impassable Door.'''

    def __init__(self):
        '''(Door) -> NoneType
        Construct an impenetrable Door'''

        Tile.__init__(self)

    def symbol(self):
        '''(Door) -> str
        Return the map representation symbol for Door: /.'''

        #return "\u2588"
        return "/"
