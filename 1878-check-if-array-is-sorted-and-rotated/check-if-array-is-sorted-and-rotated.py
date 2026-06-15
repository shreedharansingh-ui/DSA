class Solution:
    def check(self, nums):
        count = 0
        sree = len(nums)
        for i in range(sree):
            if nums[i] > nums[(i + 1) % sree]:
                count += 1
        return count <= 1