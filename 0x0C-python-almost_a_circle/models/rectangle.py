#!/usr/bin/python3
"""Defines the Reactangle class that inherits from Base"""


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Reactangle class

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of he new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identifier of the new Rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """"Set the height of the Rectangle"""
        if type(value) != int:
            raise TypeError('height must be integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Get the X coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the X coordinate of the Rectangle"""
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        """Get the y coordinate of the Rectangle"""
        return self.__y

    @x.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle"""
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

    def area(self):
        """calculate the area value of the value Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            print()

        [print() for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st represent be the id attribute
                - 2nd represent be the width attribute
                - 3rd represent the height attribute
                - 4th represent the x attribute
                - 5th represent the y attribute
            ** kwargs (dict): New key/value pairs of attributes.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 0:
                self.id = args[0]
            elif len(args) >= 1:
                self.__width = args[1]
            elif len(args) >= 2:
                self.__height = args[2]
            elif len(args) >= 3:
                self.__x = args[3]
            elif len(args) >= 4:
                self.__y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
            }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )
