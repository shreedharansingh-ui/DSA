class Solution(object):
    def canConstruct(self, ransomNote, magazine):
       
        char_count = {}
        
        for ch in magazine:
            char_count[ch] = char_count.get(ch, 0) + 1
        for ch in ransomNote:
            if ch not in char_count or char_count[ch] == 0:
                return False
            char_count[ch] -= 1
        return True