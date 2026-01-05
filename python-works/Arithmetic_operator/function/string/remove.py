
def common(n1,n2):

    n3=max(n1,n2)

    greatest=0

    for i in range(1,n3+1):

        if n1%i==0 and n2%i==0:

            greatest=i

    return greatest

print(common(6,12))

        

    