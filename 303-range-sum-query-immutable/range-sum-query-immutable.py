class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
        


'''
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        current_sum = 0
        
        # Just keep a running total!
        for num in nums:
            current_sum += num
            self.prefix.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        # If we are starting from the very beginning, just grab the right side
        if left == 0:
            return self.prefix[right]
            
        # Otherwise, take the right side and subtract the part before the left side
        else:
            return self.prefix[right] - self.prefix[left - 1]'''

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)