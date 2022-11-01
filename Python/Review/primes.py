
def getPrimes():
    for i in range(7,n):
    # if any( i % m == 0 for m in range(2,10) ):
        if i % 2 == 0 or i % 3 == 0 or i % 4 == 0 or i % 5 == 0 or i % 6 == 0 or i % 7 == 0 or i % 8 == 0:
            continue
        else:
            primes.append(i)


















# Find all prime numbers between 1 and 50,000

# Find them using the modulo (%) function
# And division (/)

primes = [2,3,5,7]
n = 30

getPrimes()

print(primes)