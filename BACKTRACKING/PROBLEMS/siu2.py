#Permutations II

#LC #47 · Medium
#Like Permutations I but input has duplicates. Uses a visited[] array + the same sort-and-skip trick to avoid duplicate permutations.

class Solution:
    def permutations(self, arr):
        arr.sort()
        result = []
        def backtrack(index, visited):
            if len(visited) == len(arr):
                result.append(visited[:])
            for i in range(0,len(arr)):
                if arr[i] in visited:
                    continue
                visited.append(arr[i])
                backtrack(i+1, visited)
                visited.pop()
        backtrack(0,[])
        return result

nums = [1, 2, 3]
obj = Solution()
print(obj.permutations(nums))
