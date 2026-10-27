# Kth Smallest
# Difficulty: MediumAccuracy: 35.17%Submissions: 853K+Points: 4Average Time: 25m
# Given an integer array arr[] and an integer k, find and return the kth smallest element in the given array.

# Examples :

# Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
# Output: 5
# Explanation: 4th smallest element in the given array is 5.
# Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
# Explanation: 3rd smallest element in the given array is 7.
# Constraints:

# 1 ≤ arr.size(), arr[i] ≤ 105
# 1 ≤ k ≤ arr.size()


class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        if len(arr)==1:
            return 0
            
        arr.sort()
        return arr[k-1]
        #index will start form 0 so we are using(k-1)
