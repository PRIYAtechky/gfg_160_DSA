"""
Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Examples:
Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals[][] = [[1, 3], [1, 3], [1, 3]]
Output: 2
Explanation: You need to remove two [1, 3] to make the rest of the intervals non-overlapping.

Input: intervals[][] = [[1, 2], [5, 10], [18, 35], [40, 45]]
Output: 0
Explanation: All ranges are already non overlapping.
"""

class Solution:
    def minRemoval(self, intervals):
        cnt = 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt += 1
            else:
                end = intervals[i][1]
        return cnt
