# -*- coding: utf-8 -*-

'''
    Dungeons and Fighters 

    Task: This file contains the Room class that keeps a 2-D list of squares that correspond to the floor plan of the room the hero is in, 
          and resolves movement actions for our hero. It's a Model file that receives movement commands and updates itself accordingly. 
          Its main purpose is to determine the correct action when movement commands are sent to it according to the rules of the game.
    
    room.py

    Created by Seungkyu Kim on Apr 30, 2016
    Copyright 2016 Seungky Kim. All rights reserved.

'''


from tile import *
from math import floor, ceil
from game import *

ROWS = 11
COLS = 21


class Room:
    '''A class representing one of several interconnected
    Rooms that constitute the game.'''

    def __init__(self, game, walls):
        '''(Room, Game, list) -> NoneType
        Create a new Room that belongs to game game.
        Add walls at all coordinates specified as tuples (x, y) in walls.'''

        self.game = game
        self.rows = ROWS
        self.cols = COLS
        self.i_list = []
        self.m_list = []
        self.north = None
        self.south = None
        self.east = None
        self.west = None

        #populate the entire grid with empty tiles first
        self.grid = [[Tile() for q in list(range(self.cols))]
            for z in list(range(self.rows))]

        #add walls as specified by the map file
        for i, j in walls:
            self.grid[i][j] = Wall()
        self.status = ""

        #specify where hero should appear if he is coming from
        #each direction: 0 - north, 1 - south, 2 - east, 3 - west
        # 4 - center

        self.locations = [(self.rows - 2, ceil(self.cols // 2)),
                        (1, ceil(self.cols // 2)),
                        (ceil(self.rows // 2), 1),
                        (ceil(self.rows // 2), self.cols - 2),
                        (ceil(self.rows // 2), ceil(self.cols // 2))]

    def update_visibility(self):
        '''(Room) -> NoneType
        Update what the hero has uncovered given his new position.'''

        rad = 0
        self.helper_update_visibility(self.hero_x, self.hero_y, rad)

    def helper_update_visibility(self, x, y, rad):
        '''(Room, int, int) -> NoneType
        Help update_visibility method updating hero's uncovered position with
        given current location of hero's x_coordinate, x, and y_coordinate,
        y.'''

        if(self.in_grid(x, y) and rad <= self.game.hero.radius):
            self.grid[x][y].visible = True
            self.helper_update_visibility(x - 1, y, rad + 1)
            self.helper_update_visibility(x, y - 1, rad + 1)
            self.helper_update_visibility(x + 1, y, rad + 1)
            self.helper_update_visibility(x, y + 1, rad + 1)
            self.helper_update_visibility(x - 1, y + 1, rad + 1)
            self.helper_update_visibility(x + 1, y + 1, rad + 1)
            self.helper_update_visibility(x - 1, y - 1, rad + 1)
            self.helper_update_visibility(x + 1, y - 1, rad + 1)
        return

    def add_hero(self, hero, where):
        '''(Room, Hero, int) -> NoneType
        Add hero hero to the room, placing him
        as specified in self.locations[where].'''

        self.hero_x, self.hero_y = self.locations[where]
        self.hero = hero
        self.grid[self.hero_x][self.hero_y] = self.hero
        self.update_visibility()

    def add(self, obj, x, y):
        '''(Room, Tile, int, int) -> NoneType
        Add Tile object obj to the room at (x, y).'''

        self.grid[x][y] = obj

    def in_grid(self, x, y):
        '''(Room, int, int) -> bool
        Return True iff coordinates (x,y) fall within the room's grid.'''

        return x >= 0 and x < self.rows and y >= 0 and y < self.cols

    def move_hero(self, x, y):
        '''(Room, int, int) -> NoneType
        Move hero to new location +x and +y from current location.
        If the new location is impenetrable, do not update hero location.'''

        newx = self.hero_x + x
        newy = self.hero_y + y
        self.hero = self.game.hero
        if not self.in_grid(newx, newy) or type(self.grid[newx][newy]) == Wall:
            return

        # DOOR CODE GOES HERE
        elif(self.grid[newx][newy].symbol() == "/"):
            if (newx == 0 and newy == 10):
                self.game.current_room = self.north
                self.game.current_room.add_hero(self.hero, self.game.North)
            elif (newx == 10 and newy == 10):
                self.game.current_room = self.south
                self.game.current_room.add_hero(self.hero, self.game.South)
            elif (newx == 5 and newy == 20):
                self.game.current_room = self.east
                self.game.current_room.add_hero(self.hero, self.game.East)
            elif (newx == 5 and newy == 0):
                self.game.current_room = self.west
                self.game.current_room.add_hero(self.hero, self.game.West)
        else:
            self.resolve(newx, newy)
            self.update_visibility()

    def resolve(self, x, y):
        '''(Room, int, int) -> NoneType
        Resolve an encounter between a penetrable Tile and a hero.
        '''

        #Replace space hero left with a new blank Tile
        self.grid[self.hero_x][self.hero_y] = Tile(True)

        # ITEM AND MONSTER CODE GOES HERE
        self.status = ""
        if self.grid[x][y] in self.i_list:
            index = self.i_list.index(self.grid[x][y])
            self.hero.take(self.i_list[index])
            self.status = "Picked up %s" % self.i_list[index].name
        elif self.grid[x][y] in self.m_list:
            index = self.m_list.index(self.grid[x][y])
            self.status = self.hero.fight(self.m_list[index])
        #update hero location
        self.hero_x = x
        self.hero_y = y
        self.grid[x][y] = self.hero
