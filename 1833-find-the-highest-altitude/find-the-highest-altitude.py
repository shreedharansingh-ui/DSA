class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        for i in range(len(gain)):
            altitude = 0
            for j in range(i + 1):
                altitude += gain[j]
            highest = max(highest, altitude)
        return highest