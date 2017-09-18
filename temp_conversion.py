def to_fahrenheit(celsius):
    """Return the input Celsius degrees in Fahrenheit."""
    return 9 / 5 * celsius +32


def to_celsius(fahrenheit):
    """Return the input Fahrenheit degrees in Celsius."""
    return 5 / 9 * (fahrenheit - 32)
#
# c = float(input('Enter degrees in Celsius: '))
# f = to_fahrenheit(c)

# You can print multiple items in one statement. If you put a comma after each item, it prints a space and then goes to print the next item.

currentUnit = input('Choose °C or °F (c/f)').capitalize()

assert currentUnit == 'C' or currentUnit == 'F'

if currentUnit == 'C':
    data = float(input('Enter degrees in Celsius: '))
    print('%.2f' % (to_fahrenheit(data)))
    print()
else:
    data = float(input('Enter degrees in Fahrenheit: '))
    print('%.2f' % (to_celsius(data)))
    print()





# print('%.2f' % (c))