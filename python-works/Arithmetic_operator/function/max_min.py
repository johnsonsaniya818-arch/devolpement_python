def operation(*args,**kwargs):

   op=kwargs.get("keys")

   if op=="max":
      
      return max(args)
   
   else:
      
      return min(args)
   
print(operation(10,20,30,keys="max"))

print(operation(10,20,30,keys="min"))

