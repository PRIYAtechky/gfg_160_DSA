"""
You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 
Note: The answer should be returned in an increasing format.

Examples:
Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.

Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: no candidate occur more than n/3 times.
"""

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        ele1, ele2 = -1, -1
        cnt1, cnt2 = 0, 0

        for ele in arr:
            if ele == ele1:
                cnt1 += 1
            elif ele == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = ele
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = ele
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for ele in arr:
            if ele == ele1:
                cnt1 += 1
            elif ele == ele2:
                cnt2 += 1

        res = []
        if cnt1 > n / 3:
            res.append(ele1)
        if cnt2 > n / 3:
            res.append(ele2)

        res.sort()
        return res
