
def min_two(n1,n2):

    minimum=n1 if n1<n2 else n2

    return minimum

#print(min_two(5,2))

def max_two(n1,n2):

    return n1 if n1>n2 else n2

#print(max_two(60,20))

#print(min_two(6,10))

def is_odd(n):

    return True if n%2!=0 else False

#print(is_odd(9))
    
#print(is_odd(10))

def last_digit_max(n1,n2):

    return n1 if n1%10>n2%10 else n2

#print(last_digit_max(22,51))

#print(last_digit_max(34,66))

def is_leap_year(year):

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        
        return True
    
    else:
        
        return False

#print(is_leap_year(1850))

#print(is_leap_year(2004))

def bmi(height_in_cm,weight_in_kg):
    
    height_in_m=height_in_cm/100

    return round(weight_in_kg/(height_in_m**2))

print(bmi(151,50))


