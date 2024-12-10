"""
Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements.
Do the mentioned change in the array in place.

Examples:
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
"""

class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < len(arr):
            arr[count] = 0
            count += 1
