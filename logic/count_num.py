#count the number of digit in an interger eg= 5345 have 4 digit
n=int(input("enter the number here:"))
num=n
count=0
while(num>0):
    num=num//10
    count +=1
print("number of digits:",count)