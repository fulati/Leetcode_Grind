class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1

        for n in nums:
            prefix += n
            need = prefix - k 
            count += freq[need]
            freq[prefix] += 1
        
        return count
