
year=int(input("enter a year"))

if(year%100==0 and year%400==0)or (year%100!=0 and year%4==0):#year%100==0 to know the year is century or not if it century it will check with 400 and not century should divisible with 4

    print("year is leap year")

else:

    print("year is not leap year")

