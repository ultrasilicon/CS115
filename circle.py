"""
Created on Nov 21 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw
"""


from shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius, name="circle"):
        super().__init__(x, y, name)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14159265358979 * self.__radius ** 2

    def __str__(self):
        return super().__str__() + ", radius = " + str(self.__radius) + ", area = %.3f" % self.area


if __name__ == "__main__":
    ret = Circle(10, 10, 30)
    print(ret)










































