'''
if it's hot
    It's a hot day
    Drink plenty of water
otherwise if it's cold
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day
'''

# BOOLIAN APPROACH
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day!")
print("Enjoy your day")

# EXAMPLE 2
price = 100000
good_credit = False

if good_credit:
    down = 0.1 * price
else:
    down = 0.2 * price
print(f"Down payment required: ${round(down)}")

# CONDITIONAL
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if x == y:
    print(f"x and y are the same length, {len(x)}")
else:
    print(f"x and y are not the same length: x = {len(x)} and y = {len(y)}.")
