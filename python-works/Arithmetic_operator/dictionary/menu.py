
menu_items={"tea":10,
           "vada":15,
           "dosa":20,
           "poori":25,
           "chappathi":10,
           "biriyani":80}

# for k in menu_items.keys():

#     print(k)

# for k,v in menu_items.items():

#     print(k,v)

# for k,v in menu_items.items():

#     if(v<50):

#         print(k,v)

# item=menu_items.get("biriyani",0)

# print(item)

if "mandhi" in menu_items:

    menu_items["mandhi"]+=15

else:

    menu_items["mandhi"]=200


print(menu_items)



