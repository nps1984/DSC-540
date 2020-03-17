from itertools import permutations, dropwhile
import math

# See help documentation
help(permutations)
help(dropwhile)

tup = (0,1,2)
print(type(dropwhile(lambda x: x <= 0, tup)))

tup = (1,0,2)
print(type(dropwhile(lambda x: x <= 0, tup)))

# Will print permutations object
print(permutations(range(3)))

print('Print the actual permutations:')
for num in permutations(range(3)):
    print(num)
    # Use assert to ensure we have tuple
    assert isinstance(num, tuple)

print('Print permutations (as list) that do not start with 0')
for num in permutations(range(3)):
    # Remove permutations that start with a 0
    print(list(dropwhile(lambda x : x <= 0, num)))


def convert_to_number(stack):
    number = 0

    # iterate over stack
    for i in range(0, len(stack)):
        # example [1,0,2]
        # (2 * 10^0) = 2
        # (0 * 10^1) = 0
        # (1 * 10^2) = 100
        # 2 + 0 + 100 = 102
        number += (stack.pop() * (math.pow(10, i)))
    return number


# Loop over range
print('Printing permutations (as list) before converting to number:')
for num in permutations(range(3)):
    # use dropwhile to remove tuples that start with 0
    number_stack = list(dropwhile(lambda x: x <= 0, num))

    print(number_stack)

    # Pass stack to function
    print(f'Converted to number: {convert_to_number(number_stack)}')

