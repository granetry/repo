'''
Everything we need to know about strings!
'''

# Use input() to set a name.
name = input('What is your name? ')
print('Hi ' + name)

## Printing strings ##

# Concat strings for print().
name = input('What is your name? ')
fav_color = input('Enter favorite color. ')
print(name + ' likes ' + fav_color)

# .format print()
weight = input('Enter weight: ')
convert = float(weight) * 0.45
print('Your weight in kg is {}.'.format(convert))

# formated string
first = 'Ryan'
last = 'Granet'
msg = f'{first} [{last}] is a coder'
print(msg)

# Change input string to integer or float
birth_year = input('Birth Year: ')
age = 2020 - int(birth_year)  # float() or bool() are other options
print(age)

# Indexing strings.
course = 'Python for Beginners'
print(course[1:-1])

# String METHODS (course.METHODS)
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course)
course.find('P')
course.title()
print(course.replace('Beginners', 'Absolute Beginners'))

# Boolian
'Python' in course
