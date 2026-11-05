def read_matrix(path: str) -> list[list[int]]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        raise ValueError("Файл пустой")

    header_parts = lines[0].split()
    if len(header_parts) != 2:
        raise ValueError("Неверный формат заголовка: ожидалось два числа (строки и столбцы)")

    try:
        rows_expected = int(header_parts[0])
        cols_expected = int(header_parts[1])
    except ValueError:
        raise ValueError("Заголовок содержит нецелочисленные значения")

    data_lines = lines[1:]
    if len(data_lines) != rows_expected:
        raise ValueError(
            f"Неправильное количество строк: ожидалось {rows_expected}, найдено {len(data_lines)}"
        )

    matrix = []
    for i, line in enumerate(data_lines, start=2):
        parts = line.split()
        if len(parts) != cols_expected:
            raise ValueError(
                f"В строке {i} ожидалось {cols_expected} чисел, а найдено {len(parts)}"
            )
        try:
            row_ints = [int(x) for x in parts]
        except ValueError:
            raise ValueError(f"В строке {i} обнаружена нечисловая ячейка")
        matrix.append(row_ints)

    return matrix
