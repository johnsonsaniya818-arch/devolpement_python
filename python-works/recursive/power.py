def numbers(number):

    if number==0:

        return 1
    
    return number%10*numbers(number//10)

print(numbers(32))