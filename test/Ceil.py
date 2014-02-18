'''
Created on 16/set/2013

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
from mock import Mock, patch, MagicMock
import unittest

class TestCeil(unittest.TestCase):

    def test_get_mean_and_variance_of_waiting(self):
        fakeCeil = Ceil()
        item1 = Mock()
        item1.twait.return_value = 2
        item1.twait = 2
        item2 = Mock()
        item2.twait = 3
        item3 = Mock()
        item3.twait = 5
        fakeCeil.get_n_of_items = MagicMock(name='get_n_of_items')
        fakeCeil.get_switched_in_waiting = MagicMock(name='get_switched_in_waiting')
        fakeCeil.get_n_of_items.return_value = 3
        fakeCeil.get_switched_in_waiting.return_value = [item1,item2,item3]
                
        mean, variance = fakeCeil.get_mean_and_variance_of_waiting()
        
        self.assertAlmostEqual(3.33, mean, 2)
        self.assertAlmostEqual(1.555, variance, 2)

if __name__ == '__main__':
    unittest.main()

        