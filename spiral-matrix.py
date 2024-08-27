#Given a matrix, return the elements
#in a (clockwise) spiral

def spiral_order(matrix: list[list[int]]) -> list[int]:
    right = lambda a, b : (a, b + 1)
    down = lambda a, b : (a + 1, b)
    left = lambda a, b : (a, b - 1)
    up = lambda a, b : (a - 1, b)
    operations = [right, down, left, up]

    length, width = len(matrix), len(matrix[0])
    size = length * width
    elements_in_order = []

    current_position = (0,0)
    current_operation_index = 0
    current_operation = operations[current_operation_index]
    seen = {(0,0)}
    elements_in_order.append(matrix[0][0])
    while len(elements_in_order) < size:
        prospective_next = current_operation(* current_position)
        x_invalid = prospective_next[1] < 0 or prospective_next[1] >= width
        y_invalid = prospective_next[0] >= length
        already_seen = prospective_next in seen
        if x_invalid or y_invalid or already_seen:
            current_operation_index = (current_operation_index + 1) % 4
            current_operation = operations[current_operation_index]
            current_position = current_operation(* current_position)
            to_append = matrix[current_position[0]][current_position[1]]
            elements_in_order.append(to_append)
            continue
        current_position = prospective_next
        to_append = matrix[current_position[0]][current_position[1]]
        elements_in_order.append(to_append)

    return elements_in_order

print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))