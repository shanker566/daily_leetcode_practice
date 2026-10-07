class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, current):
            # Target reached
            if remaining == 0:
                result.append(current.copy())
                return

            # Target exceeded
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Choose
                current.append(candidates[i])

                # We use i again because
                # the same number can be selected unlimited times
                backtrack(i, remaining - candidates[i], current)

                # Undo choice
                current.pop()

        backtrack(0, target, [])
        return result