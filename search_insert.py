nums = [1,3,4,7,9]
#       0 1 2 3 4 5

target = 10

def searchInsert(nums,target):
    if target > nums[-1]:
        return len(nums)
    else:
        for n in nums:
            if target <= n:
                return nums.index(n)

def searchInsert2(nums,target):
    if target > nums[-1]:
        return len(nums)
    else:
        for i, n in enumerate(nums):
            if target <= n:
                return i

print(searchInsert2(nums,target))

def searchInsertDichotomie(nums,target):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:           #cas simple
        if target <= nums[0]:
            return 0
        else:
            return 1
    else:                          #cas composé
        pivot_index = len(nums) // 2
        if target == nums[pivot_index]:
            return pivot_index
        elif target < nums[pivot_index]:
            res = searchInsertDichotomie(nums[0:pivot_index],target)
            return res
        else:
            res = searchInsertDichotomie(nums[pivot_index+1:],target) + pivot_index +1
            return res

print(searchInsertDichotomie(nums,target))