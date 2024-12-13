"""
Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
"""

class Solution:
    def maxSubArraySum(self, arr):
        max_sum = arr[0]
        curr_sum = 0

        for num in arr:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

def main():
    arr = [1, 2, 3, -2, 5]
    ob = Solution() 
    
if __name__ == "__main__":
    main()
