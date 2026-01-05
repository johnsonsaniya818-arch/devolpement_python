
def common_divisors(n):

    for i in range(1,n+1):

        if n%i==0:

            print(i)
        
print(common_divisors(25))