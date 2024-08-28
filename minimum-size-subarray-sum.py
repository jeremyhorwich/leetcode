#Given an array of positive integers nums and a positive integer target
#return minimal array length whose sum meets or exceeds target.
#Otherwise, return 0

def min_sub_array_len(target: int, nums: list[int]) -> int:
    min_size = len(nums) + 1
    left = 0
    right = 1
    while left < len(nums):
        total = 0
        for i in range(left, right):
            total += nums[i]
        if total >= target:
            subset_size = right - left
            if subset_size == 1:
                return 1
            if subset_size < min_size:
                min_size = subset_size
            left += 1
            continue
        if right == len(nums):
            if min_size == len(nums) + 1:
                return 0
            return min_size
        right += 1

print(min_sub_array_len(7, [2,3,1,2,4,3]))