#Given an array of heights, find the two heights
#that can hold the most water

def largest_container(heights: list[int]) -> int:
    i = 0
    j = len(heights) - 1
    largest = 0
    while i < j:
        area = (j-i)*min(heights[i],heights[j])
        largest = max(largest,area)
        if heights[i]<heights[j]:
            i += 1
        else:
            j -= 1
    return largest


if __name__ == "__main__":
    print(largest_container([1,8,6,2,5,4,8,3,7]))
    print(largest_container([8,3,6,2,1,10,6,32,4,7,3,9,3,2,65,23,7]))