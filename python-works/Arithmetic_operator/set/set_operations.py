
set_a={10,20,30,30,40,50}

set_b={10,60,70,80,20}

union_set=set_a.union(set_b)

print(union_set)

intersection_set=set_a.intersection(set_b)

print(intersection_set)

digfference_set=set_b.difference(set_a)

print(digfference_set)

set_c={10,30,50,90}

set_d={10,90,30}


print(set_c.issuperset(set_d))

print(set_d.issuperset(set_c))