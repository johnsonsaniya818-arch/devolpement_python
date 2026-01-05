def product(number):

    if number==0:

        return 1
    
    return number%10*product(number//10)

print(product(25))

