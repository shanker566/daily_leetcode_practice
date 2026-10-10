class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        new_sum = 0
        min_length = float('inf')
        
        while r < len(nums):
            new_sum += nums[r]
            
            # FIX 1: We squeeze when the sum is >= target
            while new_sum >= target:
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                
                # FIX 2: Always shrink, un-indented from the 'if' statement
                new_sum -= nums[l]
                l += 1
                
            r += 1
            
        # FIX 3: Moved all the way to the left, outside the outer while loop
        if min_length == float('inf'):
            return 0
        else:
            return min_length