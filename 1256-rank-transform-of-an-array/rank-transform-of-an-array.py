class Solution:
    def arrayRankTransform(self, arr):

        sorted_arr = sorted(arr)
        rank = {}
        current_rank = 1

        for num in sorted_arr:
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]

        return arr