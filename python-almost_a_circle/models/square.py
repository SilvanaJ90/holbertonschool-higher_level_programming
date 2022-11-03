#!/usr/bin/python3
"""
Class Square inhere Rectangle
"""


from models.rectangle import Base, Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter size"""
        return super().width

    @size.setter
    def size(self, size):
        """ setter size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ args - kwargs """
        if len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if len(kwargs) > 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.height = kwargs['size']
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ dictionary Square """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
