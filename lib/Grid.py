'''
Created on 10/set/2013

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

from lib.Ceil import Ceil
from random import choice

class Grid(object):
    '''
    Grid collect agents and is responsible to maintain or delete them. It talks with
    agent, moves them, collect data from/to ceils, and delegate them other things.
    '''
    agents = []
    n = 25
    m = 25

    def __init__(self, plotter=None):
        self.chess = {}
        for col in xrange(self.n):
            for row in xrange(self.m):
                self.chess[(col, row)] = Ceil()
        self.init_perimetral()
        self.plotter = plotter 
        
    def push(self, agents):
        self.agents.extend(agents)
        for agent in agents:
            self.set_start_point(agent)
        return self
        
    def tick(self):
        self.stats()
        self.plot()
        removed_agents = []
        for agent in self.agents:
            isKilled = False
            if not agent.would_to_walking():
                continue
            for i, j in agent.current_position():
                """
                   @self.chess[i, j]: Ceil
                """
                self.chess[i, j].del_item(agent)
                # print "item per ({0},{1}): {2}".format(i, j, self.chess[i, j].get_items())
            destination = []
            for nextCeil in agent.to_position():
                try:
                    #print "nextCeil: {0}".format(nextCeil)
                    self.chess[nextCeil]
                    destination.append(nextCeil)
                except KeyError as e:
                    #print "Cella {0} non valida per agente {1}".format(e, agent.dimension)
                    #aggiuno l'agente tra quelli da rimuove
                    removed_agents.append(agent)
                    isKilled = True
                    break
            if not isKilled: 
                self.move_agent_to(agent, destination)
                agent.update_x_y()                 
        map(lambda a: self.agents.remove(a), removed_agents)
        #print "totali: {0}".format(len(self.agents))
  
    def get_chess(self):
        return self.chess
    
    def init_perimetral(self):
        self._perimetral = [ceil for ceil in self.chess if (ceil[0]==0 and ceil[1] in xrange(self.m)) or (ceil[1]==0 and ceil[0] in xrange(self.n))]
    
    def get_perimetral(self):
        return self._perimetral
    
    def set_start_point(self, agent):
        col, row = choice(self._perimetral)
        # print "start: ({0}, {1}) ".format(col, row)   
        # print 'col: %d, row: %d, n: %d, m: %d, d: %d' % (col, row, self.n, self.m, agent.dimension)
        while col + agent.dimension > self.n:
            col = col - 1
        while row + agent.dimension > self.m:
            row = row - 1
            
        agent.x, agent.y = row, col
        for i in xrange(agent.dimension):
            for j in xrange(agent.dimension):
                #print self.chess[(col+i, row+j)]
                self.chess[(col+i, row+j)].add_item(agent)
    
    def plot(self):
        if self.plotter: 
            self.plotter.plot(*self.get_axes())
        else:
            self.default_plot()
                        
    def default_plot(self):
        stringa = ""
        for col in xrange(self.n):
            for row in xrange(self.m):
                # stringa += "({0:02d},{1:02d}):{2} ".format(col, row, self.chess[(col, row)].get_items())
                stringa += "{0} ".format(self.chess[(col, row)].get_n_of_items())
            stringa += "\n"
        print stringa
        
    def move_agent_to(self, agent, destination):
        for ceil in destination:
            self.chess[ceil].add_item(agent)

    def stats(self):
        for col in xrange(self.n):
            for row in xrange(self.m):
                walking, waiting, (mean, variance) = self.chess[(col, row)].stats()
                print "walking: {0} waiting: {1} mean: {2} variance {3}".format(walking, waiting, mean, variance)
                    
    def get_axes(self):
        rows, cols, axis_z = [], [], []        
        for col in xrange(self.n):
            for row in xrange(self.m):
                cols.append(col)
                rows.append(row)
                axis_z.append(self.chess[(col, row)].get_n_of_items())
        return (rows, cols, axis_z)
    