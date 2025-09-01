class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left_pass = 1
        for i in range(len(nums)):
            output[i] = left_pass
            left_pass *= nums[i]
        
        right_pass = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right_pass
            right_pass *= nums[i]
        
        return output