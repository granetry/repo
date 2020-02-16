# WHILE LOOPS

i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

am_i_true: True
while True:
    print("*")

# FOR LOOPS

for item in 'Python':
    print(item)

names = ['Mosh', 'John', 'Sarah']
for name in names:
    print(name)

list_of_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_range = list(range(1, 10 + 1, 2))
for value in list_of_range:
    print(value)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: ${total}")

# NESTED LOOPS

for x in range(4):
    for y in range(3):
        for z in range(3):
            print(f"({x}, {y}, {z})")

# Nested loops with strings
numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
