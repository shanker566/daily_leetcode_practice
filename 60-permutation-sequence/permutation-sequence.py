import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers from 1 to n
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Precompute factorials up to n-1
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        # Convert k to 0-indexed
        k -= 1
        
        result = []
        
        # Calculate digit by digit
        for i in range(n - 1, -1, -1):
            # Determine the index of the next number to choose
            idx = k // factorials[i]
            result.append(numbers[idx])
            
            # Remove chosen number so it's not reused
            numbers.pop(idx)
            
            # Update k for the next iteration
            k %= factorials[i]
            
        return "".join(result)
