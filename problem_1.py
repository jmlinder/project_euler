# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# First we initialize our total; we will be adding to this in the function
total = 0

# Testing the initial case of all multiples of 3 and 5 under 10
for i in range(10):

    # Case 0
    if i == 0:
        print(f'{i} is 0!')

    # if i is a multiple of 3
    elif i % 3 == 0:
        print(
            f'{i} is a multiple of 3; adding {i} to the total value of {total} gives us a total of ')
        total = total + i
        print(f'{total}')

    # if i si a multiple of 5
    elif i % 5 == 0:
        print(
            f'{i} is a multiple of 5; adding {i} to the total value of {total} gives us a total of ')
        total = total + i
        print(f'{total}')

    # if neither of the above
    else:
        print(f'{i} is not a multiple of 3 or 5.')
        continue


# Wrapping this code in a function and cleaning up some syntax
def sum_three_and_five_multiples(n):
    '''
    Returns the sum of all numbers 0 < n that are multiples of 3 or 5.
    '''
    tot = 0

    # Testing the initial case of all multiples of 3 and 5 under 10
    for i in range(n):

        # Case 0
        if i == 0:
            continue

        # if i is a multiple of 3
        elif i % 3 == 0:
            tot = tot + i

        # if i si a multiple of 5
        elif i % 5 == 0:
            tot = tot + i

        # if neither of the above
        else:
            continue
    print(
        f'The total of all numbers below {n} that are multiples of 3 and 5 are {tot}')


# Testing for consistency
print(sum_three_and_five_multiples.__doc__)

sum_three_and_five_multiples(10)  # 23

sum_three_and_five_multiples(1000)  # 233168
