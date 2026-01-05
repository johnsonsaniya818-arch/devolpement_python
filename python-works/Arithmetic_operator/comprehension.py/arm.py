
numbers=[150,151,153,148,153,16341,1700,16341,153]
# W.A.P to display recursive Armstrong numbers.

n2={}

for num in numbers:

    temp=num

    s=len(str(num))

    sum=0

    while(temp>0):

        n1=temp%10

        sum+=n1**s

        temp//=10

    if(sum==num):

        if num not in n2:

            n2[num]=1

        else:

            n2[num]+=1

print(n2)


