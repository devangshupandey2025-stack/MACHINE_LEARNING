nums = [1,2,1]
ans = []

def subsequences(index, arr, target):
    if index == len(nums):
        if sum(arr) == 2:
            ans.append(arr[:])
        return
    arr.append(nums[index])
    subsequences(index+1,arr, target)
    arr.pop()
    subsequences(index+1,arr, target)
subsequences(0,[], 2)
print(ans)
