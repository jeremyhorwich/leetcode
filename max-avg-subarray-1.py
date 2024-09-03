#Given an array of ints, and an int k, find the max contiguous
#subarray over k, avged

def find_max_average(nums: list[int], k: int):
    highest = 0
    for i in range(0,k):
        highest += nums[i]
    val = highest
    i = 0
    j = k - 1
    while j < len(nums) - 1:
        val -= nums[i]
        i += 1
        j += 1
        val += nums[j]
        if val > highest:
            highest = val
    return highest / k

print(find_max_average([1,12,-5,-6,50,3], 4))