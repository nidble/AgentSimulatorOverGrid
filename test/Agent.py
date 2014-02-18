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

from lib.Agent import Agent
from mock import Mock, patch, MagicMock
import unittest

class TestAgent(unittest.TestCase):


    def test_would_to_walking_with_positive_twait(self):
        fakeAgent = Agent()
        
        #t(0)
        self.assertEqual(fakeAgent.switching_walking, True)
        self.assertEqual(fakeAgent.switching_waiting, False)
        fakeAgent.pstop = 1
        self.assertEqual(fakeAgent.would_to_walking(), True)
        
        #t(1)
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, False)
        
        fakeAgent.pstop = -1
        fakeAgent._twait = 2
        self.assertEqual(fakeAgent.would_to_walking(), False)
        
        #t(2) sleep = 2
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, True)
        
        self.assertEqual(fakeAgent.would_to_walking(), False)
                
        #t(3) sleep = 1
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, False)
        
        self.assertEqual(fakeAgent.would_to_walking(), False)
         
        #t(4) sleep = 0
        self.assertEqual(fakeAgent.switching_walking, True)
        self.assertEqual(fakeAgent.switching_waiting, False)
        fakeAgent.pstop = 1
        self.assertEqual(fakeAgent.would_to_walking(), True)
          
        #t(5) 
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, False)
        
        self.assertEqual(fakeAgent.would_to_walking(), True)


    def test_would_to_walking_with_zero_twait(self):
        fakeAgent = Agent()
        
        #t(0)
        self.assertEqual(fakeAgent.switching_walking, True)
        self.assertEqual(fakeAgent.switching_waiting, False)
        fakeAgent.pstop = 1
        self.assertEqual(fakeAgent.would_to_walking(), True)
        
        #t(1)
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, False)
        fakeAgent.pstop = -1
        fakeAgent._twait = 0
        self.assertEqual(fakeAgent.would_to_walking(), False)
        
        #t(2) sleep = 0
        self.assertEqual(fakeAgent.switching_walking, True)
        self.assertEqual(fakeAgent.switching_waiting, True)
        fakeAgent.pstop = 1
        self.assertEqual(fakeAgent.would_to_walking(), True)
                
        #t(3) sleep = 0
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, False)

        self.assertEqual(fakeAgent.would_to_walking(), True)
          
        #t(4)
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, False)
        fakeAgent.pstop = -1
        self.assertEqual(fakeAgent.would_to_walking(), False)
           
        #t(5) 
        self.assertEqual(fakeAgent.switching_walking, True)
        self.assertEqual(fakeAgent.switching_waiting, True)
        
        self.assertEqual(fakeAgent.would_to_walking(), False)
        
        #t(6) 
        self.assertEqual(fakeAgent.switching_walking, True)
        self.assertEqual(fakeAgent.switching_waiting, True)
        fakeAgent.pstop = 1
        self.assertEqual(fakeAgent.would_to_walking(), True)
        
        self.assertEqual(fakeAgent.switching_walking, False)
        self.assertEqual(fakeAgent.switching_waiting, False)
        

if __name__ == '__main__':
    unittest.main()

        