
def gcd(n1,n2):

    if(n1<n2):

        small=n1
   
    else:

        small=n2

    for i in range(1,small+1):

        if(n1%i==0 and n2%i==0):

            gcd=i
    
    return gcd

print(gcd(5,10))

print(gcd(8,4))

    