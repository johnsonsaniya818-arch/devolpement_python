# def count_of_n(number):

#     if number==0:

#         return 0
    
#     return 1  +count_of_n(number//10)

# print(count_of_n(25))

# def sum_of_digit(number):

#     if number==0:

#         return 0
    
#     return number+sum_of_digit(number//10)

# print(sum_of_digit(25))

def reverse(number):

    if number==0:

        return ""
    
    return str(number%10)+str(reverse(number//10))

print(reverse(256))