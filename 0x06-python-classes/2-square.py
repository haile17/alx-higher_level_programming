#!/usr/bin/python3

"""
defines a class Square
"""

class Square():
    """
    This square represent a class 
    """
    def __init__(self, size=0):
        """
        initializes the instance attributtes 
        Args:
            size (int): size of square, must be integer and greater than zero 
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

