def inputOutput():

    print("Enter a number:")     #outputting a string to the console and literal strings are surrounded by quotations
                                 # but we can enter a number without quotations as it is literal value

    #print(1+1)                  outputs the actual math operation result 
    #                            although the data type for the result is integer, it is outputted as a string

    #print("1" + "1")                outputs the concatenation of the two strings
    #                                and the data type for the result is string

    #print(1 + "1")                  outputs an error as we cannot concatenate a string with an integer
    #print(str(1) + "1")             outputs the concatenation of the two strings if we used an integer and a string
    #print(1 + int("1"))             outputs the sum of the two integers if we used an integer and a string
    #print(int("1") + int("1"))      outputs the sum of the two integers if we used two strings
    #print(1, "1")                   outputs the two values with a space between them
    #print(1, "1", sep="")           outputs the two values without a space between them
    #print(1, "1", sep="*")          outputs the two values with a * between them


#   user_input = input()         #inputting a value from the console and the data type for the input is string
#   print(user_input)
#   print(type(user_input))      #to check the type of the input

#   user_input = int(user_input)         type casting the input to integer
#   print(user_input)

inputOutput()




