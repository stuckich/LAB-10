def selected_sum(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    total = 0
    for r_idx in range(0, len(matrix), 2):
        total += sum(matrix[r_idx])
    return total
