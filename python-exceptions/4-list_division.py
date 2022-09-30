#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        for  in list_length[0]:
        resul = list_length(my_list_1) / list_length(my_list_2)
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        if my_list_2 == 0:
            return None
        else:
            print("Inside result: {}".format(resul))
            return resulf