#Given a sorted array, swap out duplicates in place
#and return number of unique elements

def remove_duplicates(nums: list[int]) -> int:
    i = 0
    seen = set()
    for j in range(0, len(nums)):
        if nums[j] not in seen:
            seen.add(nums[j])
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return i

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))