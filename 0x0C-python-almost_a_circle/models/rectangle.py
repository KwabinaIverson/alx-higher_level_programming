#!/usr/bin/python3
"""Rectangle class that inherits from Base class

It has a private instance attributes for width, height, x and y.
I also has a public getters and setters methods for each of these attributes.
"""

from models.base import Base

class Rectangle(Base):
    """Definition of the Rectangle class"""
    
    __width = None
    __height = None
    __x = None
    __y = None
    
    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width
    
    @width.setter
    def width(self, new_width):
        """Setter fot the width attribute"""
        if new_width <= 0:
            raise ValueError("The width must be greater than 0")
        self.__width = new_width
        
    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height
    
    @height.setter
    def height(self, new_height):
        """Setter for the height attribute"""
        if new_height <= 0:
            raise ValueError("The height must be greater than 0")
        self.__height = new_height
        
    @property
    def x(self):
        """Getter for the x coordinate attribute"""
        return self.__x
    
    @x.setter
    def x(self, new_x):
        """Setter for the x coordinate attribute"""
        self.__x = new_x
        
    @property
    def y(self):
        """Getter for the y coordinate attribute"""
        return self.__y
    
    @y.setter
    def y(self, new_y):
        """Setter for the y coordinate attribute"""
        self.__y = new_y
    
    """
    Initializing of the Rectangle class
    
    Args:
        width (int): Width of the Rectangle
        height (int): Height of the Rectangle
        x (int): x value of the Rectangle
        y (int): y value of the Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
