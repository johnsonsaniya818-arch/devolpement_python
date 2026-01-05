
loan_amount=int(input("enter your loan amount "))

annual_rate=int(input("enter your interest "))

time=int(input("enter your time in years" ))

rate=annual_rate/12*100

months=time*12

EMI = (loan_amount * rate * (1 + rate)**months) / ((1 + rate)**months - 1)

print(EMI,round(EMI,2))

