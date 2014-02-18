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

from lib.Agent import Agent
from lib.Grid import Grid
from scipy.stats import poisson
from lib.Plotter import Plotter


class Simulator(object):
    '''
    Choose number of agent, iteration of simulation. Now in early stages there are only static configuration.
    But from input user, choosing dimension of grid, boundary limit for agent, it can improve the goddess of simulation. 
    '''

    step = 0

    def __init__(self):
        pass

    def go(self):
        plotter = Plotter('outdir','sim', clean=False)
        grid = Grid(plotter)
        
        for num_of_agents in poisson.rvs(5, size=42):
            agents = [Agent.build() for i in xrange(num_of_agents)]
            #print agents
            print "\nStep {0}\n".format(self.step)
            grid.push(agents)
            grid.tick()
            self.step+=1
