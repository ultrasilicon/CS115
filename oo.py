"""
Created on Nov 13 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw
"""


class Student(object):
    def __init__(self, first_name, last_name, sid, gpa):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sid = sid
        try:
            self.__gpa = float(gpa)
        except:
            raise TypeError('GPA must be a float')

    def __str__(self):
        return self.__first_name + ' ' + self.__last_name + ' (SID: ' + self.__sid + ', GPA: ' + str(self.__gpa) + ')'

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def first_name(self, last_name):
        self.__first_name = last_name

    @property
    def sid(self):
        return self.__sid

    @sid.setter
    def first_name(self, sid):
        self.__first_name = sid

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def first_name(self, gpa):
        self.__first_name = gpa



if __name__ == '__main__':
    s = Student('Jeremy', 'Doll', '55555555', '2.0')
    print(s.last_name)



