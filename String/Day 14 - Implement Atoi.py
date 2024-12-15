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