"""
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element.

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5. 
"""

class Solution:
    def getSecondLargest(self, arr):
        if not arr or len(arr) < 2:
            return -1  # Return -1 if there are fewer than 2 elements
        
        first = float('-inf')  # Largest element
        second = float('-inf')  # Second largest element
        
        for num in arr:
            if num > first:
                second = first  # Update second largest
                first = num  # Update largest
            elif num > second and num < first:
                second = num  # Update second largest if in between
        
        return second if second != float('-inf') else -1
