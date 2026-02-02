#check the number is palindrome or not
num=int(input("enter a number want to check palindrome: "))
n=num
result=0
while n>0:
    last_digit=n%10
    result=(result*10)+last_digit
    n=n//10
if num==result:
    print("number is palindrome")
else:
    print("number is not a palindrome")