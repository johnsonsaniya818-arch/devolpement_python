lst=[10,20,40,90]

evens=[num%2==0 for num in lst]

print(all(evens))

lst1=[10,41,52,11]

odds=list(map(lambda n:n%2!=0,lst1))

print(all(odds))