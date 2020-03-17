import random

# Generate a list of random numbers and print it
list_random = [random.randint(1,100) for x in range (0,100)]
print(list_random)

# save numbers divisible by 3 to a new list and print it
list_by_3 =[x for x in list_random if x % 3 == 0]
print(list_by_3)

# Get length of each list
list_random_len = len(list_random)
list_by_3_len = len(list_by_3)

# Get difference
list_difference = list_random_len - list_by_3_len
print(list_difference)

# Put it all together, a few times

# Generate an empty list
differences = []

# Do 3 loops
for i in range(0, 3):
    # Generate list with 100 random numbers from 0 to 100
    list_random = [random.randint(1, 100) for x in range(0, 100)]

    # Build list with numbers divisible by 3
    list_by_3 = [x for x in list_random if x % 3 == 0]

    # Save the length of each list
    list_random_len = len(list_random)
    list_by_3_len = len(list_by_3)

    # Get difference between list sizes and print
    list_difference = list_random_len - list_by_3_len

    # Push difference into a list
    differences.append(list_difference)

# Loop completed, print differences list
print(differences)

# Calculate the mean of the list
diff_mean = sum(differences) / len(differences)

print(f'The mean of the differences is {diff_mean}')