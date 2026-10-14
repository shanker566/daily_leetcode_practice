class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k is greater than array length
        
        # Helper function to reverse a segment of the array in place
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)  # Step 1: Reverse entire array
        reverse(0, k - 1)  # Step 2: Reverse first k elements
        reverse(k, n - 1)  # Step 3: Reverse the rest
