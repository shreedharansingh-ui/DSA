class Solution:
    def findDifference(self, nums1, nums2):
        first = []
        second = []
        for num in nums1:
            if num not in nums2 and num not in first:
                first.append(num)
        for num in nums2:
            if num not in nums1 and num not in second:
                second.append(num)
        return [first, second]