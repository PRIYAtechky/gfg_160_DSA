class Solution:
    
    def rotateArr(arr, d):
        n = len(arr)
        if n == 0:
            return
        d %= n

        Solution.reverse(arr, 0, d - 1)
        Solution.reverse(arr, d, n - 1)
        Solution.reverse(arr, 0, n - 1)

    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
