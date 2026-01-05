
#chks object is pointing to same memory location or not

manu_favt_colors=["green","red"]

deepu_favt_colors=["green","red"]

print(manu_favt_colors is deepu_favt_colors)

print(manu_favt_colors==deepu_favt_colors)# == is represented wheather the values are same

manu_favt_movie="kgf"

deepu_favt_movie="kgf"

print(manu_favt_movie is deepu_favt_movie)#small string is considered as same memory location by the python

rahul_game=["cricket","football"]

danya_game=rahul_game

print(rahul_game==danya_game)#the == is to know the values are same in both vraiables/objects

print(rahul_game is danya_game)#the is operator is checking both memories are same here is same beacuse rahul_game is assignes to danya_game

