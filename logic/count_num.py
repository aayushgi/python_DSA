#count the number 
num=int(input("enter the number here: "))
n=num
count=0
while n>0:
    count +=1
    n=n//10
print("total number of digit",count)   