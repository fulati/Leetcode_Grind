class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            new_sets = []
            for s in res:
                new_sets.append(s + [x])
            res.extend(new_sets)
        return res
