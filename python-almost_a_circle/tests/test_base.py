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

    """ Test of Base.to_json_string(None) exists """
    def test_base_to_json_string_none(self):
        self.assertIsNotNone(Base.to_json_string)

    """ Test of Base() for assigning automatically an ID + 1 of the previous exists """

    """  Test of Base.to_json_string([]) exists """
    def test_base_to_json_strin_empty(self):
        test = Base.to_json_string(None)
        self.assertEqual(test, '[]')


    """ Test of Base.to_json_string([ { 'id': 12 }]) returning a string """

    """ Test of Base.from_json_string(None) """

    """ Test of Base.from_json_string("[]") """

    """ Test of Base.from_json_string('[{ "id": 89 }]') """

    """ Test of Base.from_json_string('[{ "id": 89 }]') returning a list """


if __name__ == '__main__':
    unittest.main()