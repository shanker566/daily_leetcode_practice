class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current_sum = nums[i]
            complement = target - current_sum
            if complement in seen:
                return [seen[complement], i]
            seen[current_sum] = i
        