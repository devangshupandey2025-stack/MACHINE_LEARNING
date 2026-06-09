#Combination Sum II

#LC #40 · Medium
#Candidates can repeat in the input but each number can only be used once. Find all unique combinations that sum to target.

class Solution:
    def combinations(self,arr):
        arr.sort()
        result = []

        def backtrack(index, subset, target):
            if (sum(subset) == target):
                result.append(subset[:])
            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i-1]:
                    continue
                subset.append(arr[i])
                backtrack(i+1, subset, target)
                subset.pop()
        backtrack(0,[],target)
        return result

nums = [1, 2, 3]
target = 6
obj = Solution()
print(obj.combinations(nums))

