'''
CS 115, Inheritance Activity

Author: <your name here>
Pledge: <write pledge>
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RULES: You can use Canvas to download this file and upload your solution.
' You can use Eclipse to edit and run your program. You should NOT look at
' other programs in Eclipse, you should NOT use any other programs, and you
' should NOT use any notes or books.
' According to the Honor Code, you should report any student who appears
' to be violating these rules.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 7 (15 points)
' Implement missing sections of the Employee class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class Employee(object):
    def __init__(self, last_name, title, hours_per_week, hourly_rate):
        self.__last_name = last_name
        self.__title = title
        self.__hours_per_week = hours_per_week
        self.__hourly_rate = hourly_rate

    '''Write the constructor below. It should take in five arguments:
        - first_name (a string)
        - last_name (a string)
        - title (a string)
        - hours_per_week (an int)
        - hourly_rate (a float)
        All fields must be private. No error checking or type conversions
        are required.
         5 points'''

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    '''Write a property for hourly_rate. 3 points'''

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    '''Write a setter for hourly rate. 3 points'''

    def get_total_compensation(self):
        return self.__hourly_rate * self.__hours_per_week * 50

    '''Write a method called get_total_compensation.
       It returns the total amount of money an employee earns in a year.
       Assume that the employee works 50 weeks each year, with the remaining
       2 set aside for vacation.
       4 points'''

    def __str__(self):
        return 'Employee: %s %s\n  Title: %s\n  Hours per week: %d\n' \
               '  Hourly rate: $%.2f\n  Yearly compensation: $%.2f' % \
               (self.__first_name, self.__last_name, self.__title, \
                self.__hours_per_week, self.__hourly_rate, \
                self.get_total_compensation())


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (15 points)
' Implement missing sections of the Manager class. Manager should be a
' subclass of Employee.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class Manager(Employee):  # 2 points
    def __init__(self, last_name, title, hours_per_week, hourly_rate, bonus_percent):
        super().__init__(last_name, title, hours_per_week, hourly_rate)
        try:
            bonus = float(bonus_percent)
        except:
            raise TypeError("Bonus percent must be a float.")
        if bonus < 0:
            raise ValueError("Bonus percent cannot be negative.")
        self.__bonus_percent = bonus

    '''Write the constructor below. It should take in six arguments:
    - the first five are the same as in the Employee constructor
    - bonus_percent, a float >= 0. This attribute represents the percentage
      of the employee's yearly compensation that will be used to
      create the manager's annual bonus. MAKE SURE the argument is a float
      >= 0.  Otherwise, if it's not a float raise a TypeError stating,
      "Bonus percent must be a float." If it's a float but < 0, raise a
      ValueError stating, "Bonus percent cannot be negative."
      bonus_percent must be private.
    8 points'''

    def get_total_compensation(self):
        return self.get_total_compensation() * (1 + self.__bonus_percent / 100)

    '''Override the method get_total_compensation.
    It returns the total amount of money the manager earns in a year, i.e.
    basic employee compensation + bonus.
    To get full credit, you must call get_total_compensation in the superclass.
    Note: If a manager's yearly compensation is $100,000 and the bonus_percent
          is 10 (ten), the total compensation will be 110,000.
    5 points'''

