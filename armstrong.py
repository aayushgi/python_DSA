n=int(input("enter the number here"))
num=n
nod=len(str(n))
total=0
while n>0:
    last_digit=n%10
    total=total+(last_digit**nod)
    n=n//10
if num==total:
    print("armstrong number")
else:
    print("not a armstrong")