lst=["housefull","beautifull","peacefull","harmfull","thinkful","powerful"]

any_b=[w.endswith("full") for w in lst]

any_boolean=any(any_b)

#print(any_boolean)

lst1=["program","problem","perfect","apple"]

any_b_lst=[w.startswith("pro") for w in lst1]

#print(any(any_b_lst))

#prime number

num=7

print(not any(num%i==0 for i in range(2,num)))


