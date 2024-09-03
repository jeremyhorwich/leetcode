#Given an unsorted array nums, return the smallest positive integer
#not present in nums. 
#O(n) time, O(1) space

def first_missing_positive(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] <= 0 or nums[i] > len(nums):
            i += 1
            continue
        if nums[i] == i + 1:
            i += 1
            continue
        index_to_swap_to = nums[i] - 1
        if nums[i] == nums[index_to_swap_to]:
            i += 1
            continue
        nums[i], nums[index_to_swap_to] = nums[index_to_swap_to], nums[i]
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
    
print(first_missing_positive([1,2,0]))
print(first_missing_positive([1]))
print(first_missing_positive([3,4,-1,1]))
print(first_missing_positive([7,8,9,11,12]))