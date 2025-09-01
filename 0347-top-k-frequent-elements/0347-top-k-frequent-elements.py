class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #store the nums in a hashmap
        hash_num = defaultdict(int)
        for i in range(len(nums)):
            hash_num[nums[i]] += 1

        #order the nums based in frequency
        freq = [[] for _ in range(len(nums)+1)]
        for keyy, val in hash_num.items():
            freq[val].append(keyy)

        #return the k nums
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: 
                output.append(n)
                if len(output) == k:
                    return output