class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Loop backwards from the last index down to 0
        for i in range(len(num) - 1, -1, -1):
            # Check if the digit at index i is odd
            if int(num[i]) % 2 != 0:
                # Return the substring from the start up to this digit
                return num[:i + 1]
        
        # If the loop finishes without finding any odd digit
        return ""

    
        
        
        
        
        
        ''' l = 0
        r = len(num) - 1
        while l < r:
            for i in num:
                i = int(i)
                if i % 2 != 0:
                    return i'''