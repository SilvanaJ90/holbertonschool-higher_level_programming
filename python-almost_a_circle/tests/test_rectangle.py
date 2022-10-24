#!/usr/bin/python3
""" Test Rectangle """


import unittest
import io
from contextlib import redirect_stdout

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    
    """ Test of Rectangle(1, 2) exists """
    def test_rectangle(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)


    """ Test of Rectangle("1", 2) exists """
    def test_tectangle_string(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)


    """ Test of Rectangle(1, "2") exists """
    def test_tectangle_str_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    """ Test of Rectangle(1, 2, "3") exists """
    def test_tectangle_str_tree(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    """ Test of Rectangle(1, 2, 3, "4") exists """
    def test_tectangle_str_for(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    """ Test of Rectangle(1, 2, 3, 4, 5) exists """
    def test_tectangle_five(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEquals(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    """ Test of Rectangle(-1, 2) exists """
    def test_rectangle_neg(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)


    """ Test of Rectangle(1, -2) exists """
    def test_rectangle_neg_(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    """ Test of Rectangle(0, 2) exists """
    def test_rectangle_zero(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    """ Test of Rectangle(1, 0) exists """
    def test_rectangle_zero_h(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    """ Test of Rectangle(1, 2, -3) exists """
    def test_rectangle_neg_s(self):
            with self.assertRaises(ValueError):
                r = Rectangle(1, 2, -3)

    """ Test of Rectangle(1, 2, 3, -4) exists """
    def test_rectangle_neg_h(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    """ Test of area() exists  """
    def test_rectangle_area(self):
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

    """ Test of __str__() for Rectangle exists  """
    def test_rectangle_str(self):
        r  = str(Rectangle(4, 6, 2, 1, 12))
        result = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(r, result)

    """ Test of display() without y exists  """
    def test_rectangle_display(self):
        r  = Rectangle(4, 2)
        input_string = io.StringIO()
        result = "####\n####\n"
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(result, input_string.getvalue())


    """ Test of display() exists  """
    def test_rec_display(self):
        self.assertIsNotNone(Rectangle.display)



    """ Test of to_dictionary() in Rectangle exists  """

    """ Test of update() in Rectangle exists  """

    """ Test of update(89) in Rectangle exists  """

    """ Test of update(89, 1) in Rectangle exists  """

    """ Test of update(89, 1, 2) in Rectangle exists  """

    """ Test of update(89, 1, 2, 3) in Rectangle exists """

    """ Test of update(89, 1, 2, 3, 4) in Rectangle exists """

    """ Test of update(**{ 'id': 89 }) in Rectangle exists """

    """ Test of update(**{ 'id': 89, 'width': 1 }) in Rectangle exists """

    """ Test of update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists """

    """ Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists """

    """ Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists """

    """ Test of Rectangle.create(**{ 'id': 89 }) in Rectangle exists """

    """ Test of Rectangle.create(**{ 'id': 89, 'width': 1 }) in Rectangle exists """

    """ Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists """

    """ Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists """

    """ Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists """

    """ Test of Rectangle.save_to_file(None) in Rectangle exists """

    """ Test of Rectangle.save_to_file([]) in Rectangle exists """

    """ Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle exists """

    """ Test of Rectangle.load_from_file() when file doesn’t exist exists """

    """ Test of Rectangle.load_from_file() when file exists exists """

if __name__ == '__main__':
    unittest.main()