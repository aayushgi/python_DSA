"""
Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
"""


#solution


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num=x
        result=0
        while num>0:
            last_digit=num%10
            result=(result*10)+last_digit
            num=num//10
        if x==result:
            return True
        else:
            return False
        
