
sttendance=[

    {"name":"abin","attendance_count":28,"count":1},
    {"name":"aadhil","attendance_count":20,"count":2},
    {"name":"adhnan","attendance_count":20,"count":2},
    {"name":"arya","attendance_count":25,"count":5},
    {"name":"clairin","attendance_count":25,"count":4},
    {"name":"joji","attendance_count":26,"count":7},
    {"name":"libin","attendance_count":28,"count":7},
    {"name":"lijo","attendance_count":21,"count":2},
    {"name":"shajeer","attendance_count":27,"count":2},
    {"name":"shafi","attendance_count":28,"count":7},
    {"name":"resin","attendance_count":24,"count":3},
    {"name":"lakshmi","attendance_count":16,"count":6},
    {"name":"thammana","attendance_count":25,"count":1},
    {"name":"VARSHANA","attendance_count":8,"count":0},

]

sort_a=sorted(sttendance,key=lambda a:a.get("attendance_count"),reverse=True) 

# #print(sort_a)

name_a=[{st.get("name"):st.get("attendance_count")}for st in sort_a]

print(name_a)

# max_a=max(sttendance,key=lambda k:k.get("count"))

# # print(max_a)


# sort_h=sorted(sttendance,key=lambda k:k.get("count"))

# print(sort_h)

# sorted_a=sorted(sttendance,key=lambda k:k.get("attendance_count"))

# print(sorted_a)
