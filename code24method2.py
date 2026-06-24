#print all the factors of a number
num=int(input("enter the number here: "))
factor=[]
for i in range(1,(num//2)+1):
    if num%i==0:
        factor.append(i)
factor.append(num)
print(factor)
print("more optimal solution")