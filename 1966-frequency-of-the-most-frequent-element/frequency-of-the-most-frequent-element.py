class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        max_frq = 0
        windows_sum = 0
        for r in range(len(nums)):
            windows_sum += nums[r]
            
            # FIXED: Changed '1' to 'l' and added '* nums[r]'
            while (r - l + 1) * nums[r] - windows_sum > k:
                # FIXED: Changed nums[1] to nums[l]
                windows_sum -= nums[l]
                l += 1
                
            max_frq = max(max_frq, r - l + 1)
        return max_frq
