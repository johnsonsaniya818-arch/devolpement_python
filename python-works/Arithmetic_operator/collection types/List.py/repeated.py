
arr=[100,200,300,110,210,200,110,110,100]

new=[]

for num in arr:

    if(arr.count(num)>1 and num not in new):

        new.append(num)

print(new)