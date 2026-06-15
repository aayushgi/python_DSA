#count the number of digit in an interger eg= 5345 have 4 digit
n=int(input("enter the number here:"))
num=n
count=0
while(num>0):
    num=num//10
    count +=1
print("number of digits:",count)


"""
time complexity for the code is
tc=0(logb10(N))

here the N is the number of itteration that we done
TC=0(logb10(10))

space complexity=0(1)
"""