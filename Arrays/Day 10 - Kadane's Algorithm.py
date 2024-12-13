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
