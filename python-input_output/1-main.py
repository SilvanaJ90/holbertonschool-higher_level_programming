#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

filename = "o_file"
text = "Holberton School is so cool!\n"
nb_characters = write_file(filename, text)
print(nb_characters)