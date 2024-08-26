#Given an unsorted array nums, return the smallest positive integer
#not present in nums. 
#O(n) time, O(1) space

def first_missing_positive(nums: list[int]) -> int:
        max_length = (2**31)-1
        seen = [0] * max_length
        largest_possible = 1 + len(nums)
        
        for num in nums:
            if num < 1 or num >= largest_possible:
                continue
            seen[num] = 1

        for i in range(1,largest_possible + 1):
            if seen[i] == 0:
                return i
    
print(first_missing_positive([1,2,0]))
print(first_missing_positive([3,4,-1,1]))
print(first_missing_positive([7,8,9,11,12]))