#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div = []
    temp = 0
    for i in range(0, list_length):
        try:
            temp = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            temp = 0
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except IndexError:
            print("out of range")
            temp = 0
        finally:
            pass
            div.append(temp)
    return div
