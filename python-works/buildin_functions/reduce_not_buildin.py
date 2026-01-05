from functools import reduce

lst1=[50,20,100,120]

max_num=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst1)

print(max_num)

min_num=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst1)

print(min_num)

product=reduce(lambda n1,n2:n1*n2,lst1)

print(product)


