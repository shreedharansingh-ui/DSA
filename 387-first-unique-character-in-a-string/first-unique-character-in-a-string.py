class Solution(object):
    def firstUniqChar(self, s):
        
        char_count = {}
        for ch in s:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i

        return -1