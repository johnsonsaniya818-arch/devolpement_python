# class ClosesetNumberToZero:

#     def solution(self,arr):

#         closest_number=0




        


#         return closest_number
    
# clst_instance=ClosesetNumberToZero()

# clst_instance.solution([-2,-1,-6,1,2,5,8])


# closest_number=0

# arr=[2,-1,4,1,-6]

# for i in arr:

#     if closest_number+1==i:

#         a=i

#     if closest_number-1==i:

#         b=i

# if a and b:
   
#     print(a if a > b else b)

# elif a:
    
#     print(a)

# elif b:
    
#     print(b)



# number=[2,1,-1,5,-3]

# ab=[]

# for i in number:

#     ab.append(abs(i))

# print(min(ab))


class ClosestNumber:

    def solution(self,arr):

        closest=arr[0]

        for num in arr:

            if abs(num)<abs(closest):

                closest=num

        if closest<0 and abs(closest) in arr:

            return abs(closest)
        
        else:

            return closest
        

closest=ClosestNumber()

print(closest.solution([-1,2,3,1]))







