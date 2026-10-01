class Solution:
    def check(self, nums: list[int]) -> bool:
        drops = 0
        for i in range(0,len(nums) - 1):
            if nums[i] > nums[i+1]:
                drops += 1
        if nums[-1] > nums[0]:
            drops += 1
        if drops <= 1:
            return True
        else:
            return False
            
        