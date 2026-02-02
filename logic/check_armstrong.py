#check the number is armstrong or not
num=int(input("enter the number you want to chack: "))
n=num
n_o_d=len(str(n))
total=0
while n>0:
    last_digit=n%10
    total=total+(last_digit**n_o_d)
    n=n//10
if total==num:
    print("number is armstrong")
else:
    print("number is not armstrong")