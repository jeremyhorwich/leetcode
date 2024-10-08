def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + (right - left) // 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(search([2,5],5))