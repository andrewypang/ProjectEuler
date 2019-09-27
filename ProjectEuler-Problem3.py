# #The prime factors of 13195 are 5, 7, 13 and 29.

# #What is the largest prime factor of the number 600851475143 ?

# https://en.wikipedia.org/wiki/Primality_test

# Let N be a positive integer. If N is composite then N has a prime factor between 2 and floor(sqrt(N)).
# Thus, if N > 1 and N has no prime factors between 2 and floor(sqrt(N)) then N must be prime.

n = 600851475143
i = 2

while i * i < n:
    while n % i == 0: # if i is an even divisor of n then divide it
        n = n / i
    i = i + 1 # i++

print(n)