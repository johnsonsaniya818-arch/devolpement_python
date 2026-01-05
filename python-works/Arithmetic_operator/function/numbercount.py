class NumberCount:

    def solution(*args,**kwargs):

        sol=kwargs.get("value")

        if sol==10:

            print(args.count(sol))

            


numbercount1=NumberCount()

numbercount1.solution(10,10,40,100,10,50,10,value=10)