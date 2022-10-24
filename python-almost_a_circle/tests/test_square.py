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
        s = Square(1)
        self.assertEqual(s.width, 1)


    """ Test of Square(1, 2) exists """
    def test_square_w(self):
        s = Square(1, 2)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.x, 2)


    """ Test of Square(1, 2, 3) exists """
    def test_square_y(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    """ Test of Square("1") exists """
    def test_square_e(self):
        with self.assertRaises(TypeError):
            s = Square("1")


    """ Test of Square(1, "2") exists """
    def test_square_error(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    """ Test of Square(1, 2, "3") exists """
    def test_square_errorR(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    """ Test of Square(1, 2, 3, 4) exists """

    """ Test of Square(-1) exists """

    """ Test of Square(1, -2) exists """

    """ Test of Square(1, 2, -3) exists """
    
    """ Test of Square(0) exists """



if __name__ == '__main__':
    unittest.main()