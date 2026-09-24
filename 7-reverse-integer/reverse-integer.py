class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        st = str(abs(x))
        rev = st[::-1]
        if x < 0:
            result = int(rev) * -1
        else:
            result = int(rev)
        if result < -2147483648 or result > 2147483647:
            return 0
        return result

