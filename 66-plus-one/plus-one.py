class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = "".join(map(str, digits))
        totalresult = int(result) + 1
        return [int(char) for char in str(totalresult)]