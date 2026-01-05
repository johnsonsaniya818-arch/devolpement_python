
years=[2005,2004,2008,2010,2024,2028,2024,2005]
# W.A.P to display recessive leap years.

y1={}

for y in years:

    if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0):

        if(y not in y1 ):

            y1[y]=1

        else:

            y1[y]+=1

print(y1)



