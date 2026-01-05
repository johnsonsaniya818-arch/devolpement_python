def sum_of_number(limit):

    if limit==1:

        return 1
    
    return limit+sum_of_number(limit-1)

print(sum_of_number(5))

# sum_of_n(5)

# 5+sum_of_number(5-1=4)

# 4+sum_of_number(4-1=3)

# 3+sum_of_number(3-1=2)

# 2+sum_of_number(2-1=1)

# sum_of_number(1)

