class Solution(object):
    def checkIfPangram(self, sentence):
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch not in sentence:
                return False
        return True