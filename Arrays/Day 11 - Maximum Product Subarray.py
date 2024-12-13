class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        maxProd = float('-inf')

        leftToRight = 1
        rightToLeft = 1

        for i in range(n):
            if leftToRight == 0:
                leftToRight = 1
            if rightToLeft == 0:
                rightToLeft = 1

            leftToRight *= arr[i]

            j = n - i - 1
            rightToLeft *= arr[j]

            maxProd = max(leftToRight, rightToLeft, maxProd)

        return maxProd

arr = [-2, 6, -3, -10, 0, 2]
ob = Solution()