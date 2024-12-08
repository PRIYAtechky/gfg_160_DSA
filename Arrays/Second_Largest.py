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
