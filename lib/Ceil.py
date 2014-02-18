'''
Created on 11/set/2013

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

class Ceil(object):
    '''
    It compute all information about the items that live inside. Ceil also manage other staff introspecting
    their items and speaking with grid.
    '''
    
    def __init__(self):
        self._items = []
        
    def get_n_of_items(self):
        return len(self._items)
        
    def get_switched_in_waiting(self):
        for item in self.get_items():
            if item.is_switching_waiting(): yield item
         
    def add_item(self, item):
        self._items.append(item)
     
    def del_item(self, item):
        self._items.remove(item)
        
    def get_items(self):
        return self._items
    
    def count_switched_waiting(self):
        '''
        @type item: Agent
        '''
        num_of_switched_waiting = 0
        for item in self.get_items():
            if item.is_switching_waiting():
                num_of_switched_waiting += 1
        return num_of_switched_waiting
    
    def count_switched_walking(self):
        '''
        @type item: Agent
        '''
        num_of_switched_walking = 0
        for item in self.get_items():
            if item.is_switching_walking():
                num_of_switched_walking += 1
        return num_of_switched_walking
                
    def get_mean_and_variance_of_waiting(self):
        n_items = 0
        waiting_time = 0
        for item in self.get_switched_in_waiting():
            waiting_time += item.twait
            #print "waiting_time: {0}".format(waiting_time)
            n_items += 1
        if not n_items:
            return 'n.d.', 'n.d.'
        mean = waiting_time / float(n_items)
        variance = sum(map(lambda v: (v.twait - mean)**2, self.get_switched_in_waiting())) / float(n_items)
        return mean, variance
    
    def stats(self):
        #return {'num_switched_walking': self.count_switched_walking(), 'num_switched_waiting': self.count_switched_waiting(), ''
        return (self.count_switched_walking(), self.count_switched_waiting(), self.get_mean_and_variance_of_waiting())
 
