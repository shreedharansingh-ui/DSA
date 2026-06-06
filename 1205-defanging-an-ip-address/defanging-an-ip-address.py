class Solution(object):
    def defangIPaddr(self, address):
        result = ''
        for i in range(len(address)):
            if address[i] == '.':
                result += '[.]'
            else:
                result += address[i]
        return result
        