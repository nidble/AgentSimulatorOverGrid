'''
Created on 09/set/2013

@author: abertulla

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from random import randrange, randint, choice, random

class Agent(object):
    '''
    Agent are responsible to change their status, to choose direction and propose shifting to the grid
    '''
    
    MAX_WAITING_TIME = 7
    
    MAX_SPEED = 15
    
    _direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
            
    def __init__(self):
        self.sleep = 0
        self.switching_walking = True
        self.switching_waiting = False
      
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x      
      
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y
        
    @property
    def dimension(self):
        return self._dimension
    
    @dimension.setter
    def dimension(self, dim):
        self._dimension = dim
    
    def init_dimension(self, to=7):
        self.dimension = randrange(1, to, 2)
        return self
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = value
        return self
    
    def init_speed(self):
        self.speed = randint(1, self.MAX_SPEED)
        return self
    
    @property
    def twait(self):
        return self._twait
    
    @twait.setter
    def twait(self, value):
        self._twait = value
        return self
    
    def init_twait(self):
        self.twait = randint(0, self.MAX_WAITING_TIME)
        return self

    @property
    def pstop(self):
        return self._pstop
    
    @pstop.setter
    def pstop(self, value):
        self._pstop = value
        return self
    
    def init_pstop(self):
        self.pstop = random()
        return self
    
    @staticmethod
    def build():
        a = Agent()
        a.init_dimension().init_speed().init_twait().init_pstop()
        return a
                
    def compute_direction(self):
        self.current_direction = choice(self._direction)
        
    def get_direction(self):
        return self.current_direction

    def col_shift(self):
        return self.get_direction()[0]*self.speed
    
    def row_shift(self):
        return self.get_direction()[1]*self.speed

    def current_position(self):
        for col in xrange(0, self.dimension):
            for row in xrange(0, self.dimension):    
                yield (self.y+col, self.x+row)
                
    def would_to_walking(self):
        #print "salto il turno, sleep: {0}".format(self.sleep)
        self.switching_waiting = False
        if self.is_sleeping():
            self.sleep -= 1
            if self.sleep is 0: self.switching_walking = True
            return False
        self.switching_walking = False
        temp = random()
        #if self.pstop < temp: print "temp: {0} > pstop {1} ?".format(temp, self.pstop)
        if self.pstop < temp:
            self.sleep = self._twait
            self.switching_waiting = True
            if self._twait is 0: self.switching_walking = True
            return False
        return True
    
    def is_sleeping(self):
        return self.sleep > 0
    
    def to_position(self):
        self.compute_direction()
        col_shift, row_shift = self.col_shift(), self.row_shift()
        for col in xrange(0, self.dimension):
            for row in xrange(0, self.dimension):
                yield (self.y+col + col_shift, self.x+row + row_shift)
                
    def update_x_y(self):
        self.x, self.y = self.x + self.row_shift(), self.y + self.col_shift() 
        
    def is_switching_waiting(self):
        return self.switching_waiting
    
    def is_switching_walking(self):
        return self.switching_walking
        
#     def my_idx(self,grid):
#         return grid.keys()[grid.values().index(self)]