class Solution:
    def toLowerCase(self, s):
        result = ""

        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z':
                result += chr(ord(s[i]) + 32)
            else:
                result += s[i]

        return result