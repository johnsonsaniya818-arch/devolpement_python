def sum_of_digit(number):

    if number==0:

        return 0
    
    return number%10+sum_of_digit(number//10)

print(sum_of_digit(25))

