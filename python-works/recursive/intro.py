#Recursion means a function calls itself repeatedly only base condition we have to stop the calling


def say_hi(limit):

    if limit==0:

        return
    
    print("haii")

    return say_hi(limit-1)

#say_hi(5)


def hello_world(limit):

    if limit==0:

        return
    
    print("Hello World")

    return hello_world(limit-1)

#hello_world(10)