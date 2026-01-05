# def numbers(number):

#     if number==0:

#         return
    
#     print(number)

#     return numbers(number-1)

# numbers(15)

# def sum_1(number):


#     if number==1:

#         return 0
    
#     return number+sum_1(number-1)


# print(sum_1(10))


# def factorial(number):

#     if number==0:

#         return 1
    
#     return number*factorial(number-1)

# print(factorial(5))


def fibnocci(number):

    if number==0:

        return 0
    
    if number==1:

        return 1
    
    return fibnocci(number-1)+fibnocci(number-1)

print(fibnocci(10))



