# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


# A prime number is a number that is only divisible by one and itself.
# We need to make a function that will test all numbers up to n and divide it by n to determine which numbers are prime.


# This function will determine if the number is prime
def prime(x):
    if x <= 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# This will print a list nls of prime factors of number n
def highest_prime_fac(n):
    highest_prime = 0
    for i in range(1, n+1):
        if n % i != 0:
            continue
        else:
            if prime(i) == True:
                if i > highest_prime:
                    highest_prime = i
    print(highest_prime)


# Lets test this function against the example provided
# The prime factors of 13195 are 5, 7, 13 and 29.
# highest_prime_fac(13195) # 29

# What is the largest prime factor of the number 600851475143?

# TODO - function needs to be optimized.
highest_prime_fac(600851475143)
