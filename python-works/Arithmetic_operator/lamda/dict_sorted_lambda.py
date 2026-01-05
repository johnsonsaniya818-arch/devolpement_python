
student_age={

    "Athul":25,

    "Madhav":22,

    "Vaishnavi":26,

    "Sarath":25,

    "Jeevan":20

}

sorted_age=sorted(student_age,key=lambda k:student_age.get(k))

print(sorted_age)