def factorial(number):

    if number==0:

        return 1
    
    return number*factorial(number-1)

print(factorial(5))

"""
factorial(5)

5*factorial(5-1)=5*24=120
4*factorial(4-1)=4*6=24
3*factorial(3-1)=3*2=6
2*factorial(2-1)2*1=2
1*factorial(1-1)=1*1=1 
factorial(0) =1 

"""



