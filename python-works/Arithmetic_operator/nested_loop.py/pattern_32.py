
for r in range(1,4):

    for sp in range(4,r,-1):

        print(" ",end=" ")

    for c in range(1,r+1):

        print(" *",end=" ")
   
    print()

for r in range(1,4):

    for sp in range(1,r+1):

        print(" ",end=" ")

        for c in range(4,r-1,-1):

            print(" *",end=" ")
        
        print()