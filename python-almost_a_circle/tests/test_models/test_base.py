#!/usr/bin/python3
""" Test base """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ doc """
    
    """ Test of Base() for assigning automatically an ID """
    def test_base(self):
        b1 = Base()
        self.assertEquals(b1.id, 1)
    """ Test of Base() for assigning automatically an ID + 1 of the previous """

    """ Test of Base(89) saving the ID passed """
    def test_base_saving(self):
        b2 = Base(89)
        self.assertEquals(b2.id, 89)



if __name__ == '__main__':
    unittest.main()