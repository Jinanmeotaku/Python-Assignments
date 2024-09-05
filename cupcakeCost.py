#A cupcake costs A dollars and B cents. Determine how many dollars and cents should one pay for N cupcakes. 
# A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

def cupcakeCost():
    A = int(input("Enter the cost of a cupcake in dollars:"))
    B = int(input("Enter the cost of a cupcake in cents:"))
    N = int(input("Enter the number of cupcakes:"))

    dollar = (A * N)
    cents = (B/100) * N
    total = dollar + cents

    print("total cost: ", int(total), "dollars", int((total - int(total)) * 100), "cents")

cupcakeCost()