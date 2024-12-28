"""
Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:
Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.

Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
"""

class Solution:
    def countAndMerge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        res = 0
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                res += (n1 - i)
            k += 1
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        return res
    def countInv(self, arr, l, r):
        res = 0
        if l < r:
            m = (r + l) // 2
            res += self.countInv(arr, l, m)
            res += self.countInv(arr, m + 1, r)
            res += self.countAndMerge(arr, l, m, r)
        return res
    def inversionCount(self, arr):
        return self.countInv(arr, 0, len(arr) - 1)
