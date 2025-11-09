class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]

        for i in range(len(nums)):

            cur = []

            for s in subsets:  

                cur.append(s + [nums[i]])
            
            subsets.extend(cur)

        return subsets