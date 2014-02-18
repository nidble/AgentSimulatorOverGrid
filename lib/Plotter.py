'''
Created on 18/set/2013

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

import os
from matplotlib import pyplot
from shutil import rmtree

class Plotter(object):
    '''
    Plot and manage creation of file and directories
    '''

    _count = 0

    def __init__(self, output_dir, fname, clean):
        self.output_dir = output_dir
        self.fname = fname
        #if clean: self.clean()
        self.build_dirs()
        
    def build_dirs(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def clean(self):
        if os.path.exists(self.output_dir):
            rmtree(self.output_dir)
            pass
            
    def succ(self):
        fname = os.path.join(self.output_dir, self.fname)
        image = "{filename}_{cnt:03d}.png".format(filename=fname, cnt=self._count)
        self._count+=1
        return image
    
    def plot(self, *axes):
        rows, cols, axis_z = axes        
        #sq = markers.MarkerStyle('s')
        pyplot.scatter(rows, cols, c=axis_z, s=150, marker = 's')
        #pyplot.subplots_adjust(left=0.1, right=0.2, top=0.2, bottom=0.1)
        pyplot.savefig(self.succ())
        pyplot.clf()
            
        
        