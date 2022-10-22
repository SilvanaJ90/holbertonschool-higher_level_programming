#!/usr/bin/python3
""" test base """

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ doc """
    def test_base(self):
        b1 = Base()
        self.assertEquals(b1.id, 1)
        b2 = Base()
        self.assertEquals(b2.id, 2)
        b2 = Base(89)
        self.assertEquals(b2.id, 89)

if __name__ == '__main__':
    unittest.main()