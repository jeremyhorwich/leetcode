#Given an array of heights, find how much
#rainwater will be trapped between them

def amount_trapped(heights: list[int]) -> int:
    i = 0
    j = len(heights) - 1
    left_max, right_max = i,j
    heights_count, trapped_count, prev_maxes_min = 0,0,0
    while (i < j):

        if heights[left_max] < heights[right_max]:
            if heights[i] > heights[left_max]:
                left_max = i
            i += 1
        else:
            if heights[j] > heights[right_max]:
                right_max = j
            j -= 1

        current_maxes_min = min(heights[left_max],heights[right_max])
        if current_maxes_min > prev_maxes_min:
            height_gained = current_maxes_min - prev_maxes_min
            trapped_count += (right_max - left_max + 1)*height_gained
            prev_maxes_min = current_maxes_min
        
    overall_max = max(heights[left_max],heights[right_max])
    if overall_max > prev_maxes_min:
        trapped_count += (overall_max - prev_maxes_min)
    for height in heights:
        heights_count += height
    trapped_count -= heights_count

    return trapped_count

if __name__ == "__main__":
    print(amount_trapped([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(amount_trapped([4,2,0,3,2,5]))
    print(amount_trapped([1,4,0,5,0,1]))