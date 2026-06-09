nums = [1,2,1]
ans = []

def subsequences(index, arr):
    if index == len(nums):
        ans.append(arr[:])
        return
    arr.append(nums[index])
    subsequences(index+1,arr)
    arr.pop()
    subsequences(index+1,arr)
subsequences(0,[])
print(ans)
