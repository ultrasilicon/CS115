"""
Created on Nov 20 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115
"""

from student import Student


class UndergradStudent(Student):
    def __init__(self, first_name, last_name, sid, gpa, meal_plan_balance):
        super().__init__(first_name, last_name, sid, gpa)
        self.__meal_plan_balance = meal_plan_balance

    def __str__(self):
        return super().__str__() + ", meal plan balance: $" + str(self.__meal_plan_balance)

    @property
    def meal_plan_balance(self):
        return self.__meal_plan_balance

    @meal_plan_balance.setter
    def meal_plan_balance(self, _meal_plan_balance):
        self.__meal_plan_balance = meal_plan_balance


if __name__ == "__main__":
    u1 = UndergradStudent("John", "Doe", "12345", 4.0, 1000)
    print(u1)









































