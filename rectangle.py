"""
Created on Nov 21 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw
"""


from shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, length, width, name="rectangle"):
        super().__init__(x, y, name)
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def area(self):
        return self.__length * self.__width

    def __str__(self):
        return super().__str__() + ", length = " + str(self.__length) + ", width = " + str(self.__width) + ", area = " + str(self.area)


if __name__ == "__main__":
    ret = Rectangle(10, 10, 20, 30)
    print(ret)










































