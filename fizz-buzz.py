# function to print fizz for multiples of 3, buzz for multiples of 5 
# and fizzbuzz for multiples of 3 and 5

def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

n = int(input("Enter the number: "))
#calling the function
fizz_buzz(n)
