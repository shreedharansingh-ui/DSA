class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for ch1 in jewels:
            for ch2 in stones:
                if ch1 == ch2:
                    count += 1
        return count  