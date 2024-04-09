#Given a k number of sorted lists, return
#a merged (sorted) list of elements

def merge_k_lists(lists: list[list[int]]) -> list[int]:
    k = len(lists)
    if k == 0:
        return []
    
    ABOVE_HIGHEST_INTEGER_IN_INPUT = 10001   #According to Leetcode doc
    indices = [0]*k
    merged = list()
    while True:
        list_updated = False
        current_min = ABOVE_HIGHEST_INTEGER_IN_INPUT
        current_min_list = None
        for list_to_check, index_value in enumerate(indices):
            if index_value >= len(lists[list_to_check]):
                continue
            if lists[list_to_check][index_value] is None:
                continue
            if lists[list_to_check][index_value] < current_min:
                current_min = lists[list_to_check][index_value]
                current_min_list = list_to_check

        if current_min == ABOVE_HIGHEST_INTEGER_IN_INPUT:
            break

        indices[current_min_list] += 1
        merged.append(current_min)
    return merged


if __name__ == "__main__": 
    print(merge_k_lists([[1,2,3],[2,3,4]]))
    print(merge_k_lists([[1,4,5],[1,3,4],[2,6]]))
    print(merge_k_lists([]))
    print(merge_k_lists([[]]))