def pivot_ind(nums, mid_ind):
    c = 0
    maxin = len(nums)
    while c < maxin:
        if sum(nums[:c]) == sum(nums[c + 1:]):
            return c
        else:
            c = c + 1
    return -1

nums = [1,2,3,4]

mid_ind = len(nums) // 2
print(pivot_ind(nums, mid_ind))