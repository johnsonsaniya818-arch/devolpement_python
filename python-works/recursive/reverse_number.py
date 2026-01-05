def reverse_number(number):

    if number==0:

        return ""
    
    return str(number%10) + str(reverse_number(number//10))


print(reverse_number(123))



