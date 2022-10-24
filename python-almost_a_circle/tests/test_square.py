#!/usr/bin/python3
""" Test Square """


from cgitb import reset
import unittest
import io
from contextlib import redirect_stdout
import json

from models.base import Base

from models.square import Square


class TestSquare(unittest.TestCase):
    
    
    """ Test of Square(1) exists """
    def test_square(self):
        r = Square(1)
        self.assertEqual(r.width, 1)


if __name__ == '__main__':
    unittest.main()