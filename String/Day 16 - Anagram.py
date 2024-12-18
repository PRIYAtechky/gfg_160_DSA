"""Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

Note: You can assume both the strings s1 & s2 are non-empty.

Examples :

Input: s1 = "geeks", s2 = "kseeg"
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.
Input: s1 = "allergy", s2 = "allergic"
Output: false
Explanation: Characters in both the strings are not same, so they are not anagrams.
Input: s1 = "g", s2 = "g"
Output: true
Explanation: Character in both the strings are same, so they are anagrams.
"""
class Solution:
    MAX_CHAR = 26

    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False  

        freq = [0] * self.MAX_CHAR
       
        for ch in s1.lower():
            freq[ord(ch) - ord('a')] += 1

        for ch in s2.lower(): 
            freq[ord(ch) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False
                
        return True
