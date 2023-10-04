"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    counter = 2
    while len(list) < number_of_primes:
        divisible_numbers = 0
        for i in range(counter):
            if counter % (i+1) == 0:
                divisible_numbers += 1
        if divisible_numbers == 2:
            list.append(counter)
        counter += 1
    print(list)
    return list

primes(20)