class Solution:
    def mostWordsFound(self, sentences):
        maximum = 0
        for sentence in sentences:
            words = sentence.split()
            if len(words) > maximum:
                maximum = len(words)
        return maximum