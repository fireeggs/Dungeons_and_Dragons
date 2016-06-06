'''
    Dungeons and Fighters 

    Task: This file contains the Game class which is the main Controller of the game. 
          Game is responsible for loading map files and creating Room objects out of them, 
          for keeping track of which room the hero is currently in, 
          and for passing movement commands along to that room.
    
    Game.py

    Created by Seungkyu Kim on Apr 30, 2016
    Copyright © 2016 Seungky Kim. All rights reserved.

'''


from hero import *
from room import *
from screen import *

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
CENTRE = 4


class Game:
    '''The controller class that keeps track of the current room
    the hero is in, the screen it should display to, etc. '''

    def __init__(self, mapname, hero):
        '''(Game, str, Hero) -> NoneType
        Create a new Game given the name of an initial room
        to load and a Hero object. mapname excludes extension.'''

        self.current_room = self.load(mapname)
        self.hero = hero
        self.North = NORTH
        self.South = SOUTH
        self.East = EAST
        self.West = WEST
        # start hero in position 4 (center)
        # corresponding to Room.locations[4]

        self.current_room.add_hero(self.hero, CENTRE)

    def game_over(self):
        '''(Game) -> NoneType
        Return True iff hero's hit points are 0 or less.'''

        return self.hero.hp <= 0

    def load(self, mapname):
        '''(Game, str) -> Room
        Append .map to mapname and open corresponding file.
        Create a new Room with appropriately placed walls.
        Precondition: file is a valid map format file.'''

        if mapname == "None":
            return
        mapfile = open(mapname + ".map", "r")
        walls = []
        row = 0
        assert mapfile.readline() == "MAPSTART\n"
        currline = mapfile.readline()
        while currline != "MAPFINISH\n":
            for col in range(len(currline)):
                if currline[col] == 'X':
                    walls.append((row, col))
            currline = mapfile.readline()
            row += 1

        #create Room
        room = Room(self, walls)

        #begin populating with items
        assert mapfile.readline() == "ITEMS\n"
        currline = mapfile.readline()
        while currline != "MONSTERS\n":
            # ADD ITEM PARSING CODE HERE
            item_list = currline.strip().split(",")
            name = item_list[0]
            hp = int(item_list[1])
            strength = int(item_list[2])
            radius = int(item_list[3])
            x_cord = int(item_list[4])
            y_cord = int(item_list[5])
            item_obj = Item(name, hp, strength, radius, x_cord, y_cord)
            room.add(item_obj, x_cord, y_cord)
            room.i_list.append(item_obj)
            currline = mapfile.readline()
        currline = mapfile.readline()
        while currline != "ENDFILE":
            # ADD MONSTER PARSING CODE HERE
            monster_list = currline.strip().split(",")
            name = monster_list[0]
            hp = int(monster_list[1])
            strength = int(monster_list[2])
            x_cord = int(monster_list[3])
            y_cord = int(monster_list[4])
            monster_obj = Monster(name, hp, strength, x_cord, y_cord)
            room.add(monster_obj, x_cord, y_cord)
            room.m_list.append(monster_obj)
            currline = mapfile.readline()
        mapfile.close()

        # PROCESS .links FILES HERE

        mapfile = open(mapname + ".links", "r")
        currline = mapfile.readline().strip()
        if(currline != "None"):
            if(currline != "Done"):
                room.north = self.load(currline)
                room.north.south = room
            room.add(Door(), 0, 10)
        currline = mapfile.readline().strip()
        if(currline != "None"):
            if(currline != "Done"):
                room.south = self.load(currline)
                room.south.north = room
            room.add(Door(), 10, 10)
        currline = mapfile.readline().strip()
        if(currline != "None"):
            if(currline != "Done"):
                room.east = self.load(currline)
                room.east.west = room
            room.add(Door(), 5, 20)
        currline = mapfile.readline().strip()
        if(currline != "None"):
            if(currline != "Done"):
                room.west = self.load(currline)
                room.west.east = room
            room.add(Door(), 5, 0)
        mapfile.close()

        return room

    def move_hero(self, x, y):
        '''(Game, int, int)
        Send a move command from the GameScreen to the current room
        to move the hero x tiles to the right and y tiles down.'''

        self.current_room.move_hero(x, y)
