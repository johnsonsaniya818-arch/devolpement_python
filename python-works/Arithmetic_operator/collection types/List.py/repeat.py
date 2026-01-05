
arr=[5,10,5,12,12,31]

arr.sort()

new=[]

left=0

right=left+1

for num in range(len(arr)-1):

    if arr[right]-arr[left]==0 and num not in new:
        
        new.append(arr[left])

    left+=1

    right+=1

   

print(new)

