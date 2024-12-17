"""
Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:
1) Skip any leading whitespaces.
2) Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
3) Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
4) If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.

Examples:
Input: s = "-123"
Output: -123
Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer

Input: s = "  -"
Output: 0
Explanation: No digits are present, therefore the returned answer is 0.

Input: s = " 1231231231311133"
Output: 2147483647
Explanation: The converted number will be greater than 231 – 1, therefore print 231 – 1 = 2147483647.

Input: s = "-999999999999"
Output: -2147483648
Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.

Input: s = "  -0012gfg4"
Output: -12
Explanation: Nothing is read after -12 as a non-digit character ‘g’ was encountered.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        idx = 0

        # Ignore leading whitespaces
        while idx < len(s) and s[idx] == ' ':
            idx += 1

        # Store the sign of the number
        if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                sign = -1
            idx += 1

        # Construct the number digit by digit
        while idx < len(s) and '0' <= s[idx] <= '9':
            # Append current digit to the result
            res = 10 * res + (ord(s[idx]) - ord('0'))

            # Handling overflow/underflow cases
            if res > (2**31 - 1):
                return (2**31 - 1) if sign == 1 else -2**31

            idx += 1

        return res * sign
