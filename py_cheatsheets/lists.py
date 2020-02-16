# List of names
import numpy as np
names = ['John', 'Bob', 'Ryan', 'Sarah', 'Mary']
print(names)

# Find items in a List
names[0]  # First indexed name
names[:]  # Starts at beginning and runs until end
names[2:]  # Starting at index 2 until end
names[:2]  # Starting at beginning and goes until 2nd index
names[-1]  # Last item in the List

# Changing the List
names[0] = 'Cat'  # Changes first index to 'Cat'
names.append('Jax')  # Adds 'Jax' into the end of the list
names.insert(0, 'Carl')  # Inserts 'Carl' into the 0th index. (Does NOT delete or replace a value)
names.remove('Carl')  # Remove 'Carl' from list
names.pop()  # Removes the last item from list
names.clear()  # Will clear the list
names.index('Ryan')  # Will return the index of the first occurance of this item
'Ryan' in names  # Find out if an item is in the list with /n/
print(names)

# Numerical Lists (Finding values and changing lists)
numbers = [1, 66, 8, 4, 45, 35, 51, 87, 1, 5, 8, 3, 32, 87, 4, 1, 57]

numbers.append(20)  # Appending to a list also works with numerical values
numbers.insert(0, 1337)  # Insert 1337 at the 0th index.
numbers.remove(8)  # Removes the first 8 in the list, only the first.
numbers.index(1337)  # Will return the index of the first occurance of this item
numbers.count(8)  # Count how many times an item occurs in a lists
numbers.sort()  # Sort numbers in ascending order
numbers.reverse()  # Reverse our list to descending order
numbers2 = numbers.copy()  # Will make a direct copy of the list as a new variable
print(numbers)
print(numbers2)

# Removing duplicate values from list
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)

# Quickly find unique items in a list. Not for saving unique values into a new list.
np.unique(numbers)

max(numbers)
max_number = numbers[0]  # Set max number as the first value in list
for values in numbers:  # run through values in list and update the max_number variable if it's greater than current
    if values > max_number:
        max_number = values
print(max_number)  # test the code

# Making an F
f_list = [5, 2, 5, 2, 2]  # Create structure of F with list
for value in f_list:
    output = ''  # Empty string variable to add structure to
    for count in range(value):
        output += 'x'  # Add as many 'x' as in list amount
    print(output)

# Making an L
# Basically making new lists of strings that will be of length 1 and 5.
l_list = [1, 1, 1, 1, 5]
for value in l_list:
    output = ''
    for count in range(value):
        output += '*'
    print(output)


'''2D lists'''
# List of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0]  # Return first list in matrix
matrix[0][0]  # Return first value of first list in matrix
matrix[0][0] = 20  # Change the first value of the first list
matrix[0] = [10, 20, 30]  # Change the first row in matrix

for row in matrix:  # will select the first row, then second, ...
    for item in row:  # will select each item in the row before moving to next row
        print(item)
