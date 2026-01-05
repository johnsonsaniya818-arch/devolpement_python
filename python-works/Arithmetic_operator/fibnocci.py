class Fibnocci:

    def solution(self,limit):

        p=0

        c=1

        print(p,end=" ")

        print(c,end=" ")

        for i in range(1,limit-1):

            n=p+c

            print(n,end=" ")

            p=c

            c=n

fib_insatce=Fibnocci()
fib_insatce.solution(10)



            
