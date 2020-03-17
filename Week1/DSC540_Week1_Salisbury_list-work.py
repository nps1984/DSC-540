import random

# Create a list with 15 numbers between 1 and 100
a_list = [5,1,30,19,87,57,75,32,30,10,92,88,43,19,28]

# create an empty list which we will put our sorted list
sorted_list = []

# Iterate over list and put values into a sorted list
for i in sorted(a_list):
    sorted_list.append(i)

# Generate a list of random numbers
random_list = [random.randint(1,100) for x in range (0,15)]

# Extend our sorted list by our random list
sorted_list.extend(random_list)

# Print it out
print(f'The sorted listed with extended random values is: {sorted_list}')
