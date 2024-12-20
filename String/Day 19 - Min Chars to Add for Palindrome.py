"""
Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.
Note: A palindrome string is a sequence of characters that reads the same forward and backward.

Examples:
Input: s = "abc"
Output: 2
Explanation: Add 'b' and 'c' at front of above string to make it palindrome : "cbabc"

Input: s = "aacecaaaa"
Output: 2
Explanation: Add 2 a's at front of above string to make it palindrome : "aaaacecaaaa"
"""

class Solution:
    def computeLPSArray(self, pat):
        n = len(pat)
        lps = [0] * n

        len_lps = 0
        i = 1

        while i < n:
            if pat[i] == pat[len_lps]:
                len_lps += 1
                lps[i] = len_lps
                i += 1
            else:
                if len_lps != 0:
                    len_lps = lps[len_lps - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def minChar(self, s):
        n = len(s)
        rev = s[::-1]  

        concat = s + "$" + rev
        lps = self.computeLPSArray(concat)

        return n - lps[-1]
