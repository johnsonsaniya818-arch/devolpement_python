
numbers=[2,4,5,7,9,8,7,6,9]


n1={}

for num in numbers:

    is_prime=True


    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break
    
    if is_prime==True:
      
      if num not in n1:

        n1[num]=1

      else:

        n1[num]+=1

print(n1)

