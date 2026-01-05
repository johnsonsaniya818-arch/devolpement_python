# for i in range(1,4):

#     for j in range(1,4):

#         print(f"{i}+{j}={i+j}",end=" ")

#     print()

# for i in range(1,5):

#     for j in range(1,5):

#         if i==1 or i==4 or j==1 or j==4:

#             print("R",end=" ")

#         else:

#             print("S",end=" ")
#     print()

n = 4

for i in range(n):
    for j in range(n):
        if j <= i:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()



        