nums = [1,2]

ans = []

def dfs(index, arr):

    if index == len(nums):
        ans.append(arr[:])
        return

    arr.append(nums[index])

    dfs(index + 1, arr)

    arr.pop()

    dfs(index + 1, arr)

dfs(0, [])

print(ans)