#!/usr/bin/python3

""" Class Square """


class Square:
    """ create Square size private"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print()

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


