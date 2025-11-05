class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero = 0
        one = 0
        two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1
            elif nums[i] == 1:
                one+=1
            elif nums[i] == 2:
                two+=1

        for i in range(zero):
            nums[i] = 0
        
        for i in range(zero, zero + one):
            nums[i] = 1
        
        for i in range(zero + one, zero + one + two):
            nums[i] = 2
    
