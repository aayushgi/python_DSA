#print all the factros of a given number
num=int(input("enter a number here: "))
n=num
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)

print(factors)
