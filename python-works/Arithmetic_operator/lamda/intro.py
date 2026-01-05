
# lambda:anyonymus function with single expression

square=lambda n: n**2

print(square(3))

add_numbers=lambda n1,n2:n1+n2

print(add_numbers(100,300))

odd_even=lambda n:"odd" if n%2!=0 else "even"

print(odd_even(9))

is_positive=lambda n:True if n>0 else False

print(is_positive(8))

is_negative=lambda n:True if n<0 else False

print(is_negative(5))

is_century_year=lambda year:True if year%100==0 else False

print(is_century_year(2000))