
all_users={"sachin","dravid","laxman","gangully","sreenath","zaheer","dhoni","yuvi","kaif"}

sachin_friends={"dravid","laxman","ganguly"}

dhoni_friends={"dravid","laxman","druvid","kalif"}

suggesion_friends=all_users.difference(sachin_friends)

suggesion_friends.remove("sachin")

print(suggesion_friends)

mutual_friends=sachin_friends.intersection(dhoni_friends)

print(mutual_friends)
