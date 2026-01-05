class Fibnocci:

    def solution(self,limit):

        is_fib=False

        p=0

        c=1


        while(n<=limit):

            n=p+c

            p=c

            c=n

            if n==limit:

                is_fib=True

                break


        return is_fib
    

fib_instance=Fibnocci()

fib_instance.solution(10)