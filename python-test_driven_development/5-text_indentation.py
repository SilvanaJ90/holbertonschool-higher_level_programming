#!/usr/bin/python3
def text_indentation(text):
    for i in len(text):
        if type(text[i]) is not str:
            raise TypeError("text must be a string")
        if text[i] == '?' or text[i] == 'and' or text[i] == '.':
            print("{}".format(text[i]), end="\n")
    print()