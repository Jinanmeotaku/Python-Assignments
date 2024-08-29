
def listOfPrimes(x):
    primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n/2) + 1):    #we use n ** 0.5 to reduce the number of iterations   
        if n % i == 0:
            return False
    else:
        return True
    
def main():
    x = int(input("Enter a number: "))
    print(listOfPrimes(x))

if __name__ == "__main__":
    main()