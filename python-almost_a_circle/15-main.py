#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":


    r2 = Rectangle(1, 2)
    Rectangle.save_to_file([r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
