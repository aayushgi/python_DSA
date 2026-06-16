#check the number is palindrome or not
"""
palendrome number vo hote hai jinko kisi bhi side se padhne per vo same value return karte hai like 121,333
"""
n=int(input("enter the number here: "))
num=n
result=0
while(num>0):
    last_digit=num%10
    result=(result*10)+last_digit
    num=num//10

if(n==result):
    print("number iss palendrome") 
else:
    print("number is not a palendrome")

"""
TC=0(lodb10(N))
N=numer of itteration 10
SC=o(1)
"""