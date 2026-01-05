
def gcd_two(n1,n2):

    gcd=0

    small=min(n1,n2)

    for i in range(1,small+1):

        if n1%i==0 and n2%i==0:

            gcd=i

    return gcd

    

print(gcd_two(6,9))