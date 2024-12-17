"""
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
[ Note: The input strings may contain leading zeros but the output string should not have any leading zeros. ]

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100

Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110
  """

class Solution:
    def trimLeadingZeros(self, s):
        firstOne = s.find('1')
        return s[firstOne:] if firstOne != -1 else "0"

    def addBinary(self, s1, s2):
        s1 = self.trimLeadingZeros(s1)
        s2 = self.trimLeadingZeros(s2)
        
        n = len(s1)
        m = len(s2)
        
        if n < m:
            s1, s2 = s2, s1
            n, m = m, n
        carry = 0
        result = []
        j = m - 1  

        for i in range(n - 1, -1, -1):
            bit1 = int(s1[i])
            bitSum = bit1 + carry

            if j >= 0:
                bit2 = int(s2[j])
                bitSum += bit2
                j -= 1

            result.append(str(bitSum % 2)) 
            carry = bitSum // 2           

        if carry > 0:
            result.append('1')

        return ''.join(result[::-1])
