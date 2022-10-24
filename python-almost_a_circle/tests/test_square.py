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
            s = Square(1, "2")

    """ Test of Square(1, 2, "3") exists """
    def test_square_errorR(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    """ Test of Square(1, 2, 3, 4) exists """
    def test_square_for(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    """ Test of Square(-1) exists """
    def test_Raise_error(self):
        with self.assertRaises(ValueError):
            s = Square(-1)

    """ Test of Square(1, -2) exists """
    def test_Square_Raise_Error(self):
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    """ Test of Square(1, 2, -3) exists """
    def test_square_error_r(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
    
    """ Test of Square(0) exists """
    def test_square_zero(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    """ Test of __str__() for Square exists """ 
    def test_square_str(self):
        s  = str(Square(1, 2, 3, 4))
        result = '[Square] (4) 2/3 - 1'
        self.assertEqual(s, result)

    """ Test of to_dictionary() in Square exists """
    def test_square_dictionary(self):
        r1 = Square(1, 2, 3, 4).to_dictionary()
        result = {'size': 1, 'x': 2, 'y': 3, 'id': 4}
        self.assertEqual(r1, result)

    """ Test of update(89) in Square exists """
    def test_square_upd_id(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

    """ Test of Square.create(**{ 'id': 89 }) in Square exists """
    def test_square_create(self):
        s1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.width, 1)

    """ Test of Square.save_to_file(None) in Square exists """
    def test_square_save_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())




if __name__ == '__main__':
    unittest.main()