
psswrd=2002

otp_db=523

password=int(input("enter your password"))

if(password==psswrd):
    
    otp=int(input("enter your otp"))
   
    if(otp==otp_db):

        print("your otp is correct")
   
    else:

        print("your otp is incorrect")
else:

    print("incorrect password")