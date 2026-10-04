class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        target = len(nums) / 2
        for num in counts:
            if counts[num] >= target:
                return num

        