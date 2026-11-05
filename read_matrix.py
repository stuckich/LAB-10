import sys
from table import read_matrix


def main():
    input_filename = "matrix.txt"
    output_filename = "report.txt"

    try:
        matrix = read_matrix(input_filename)
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_filename}' не найден.", file=sys.stderr)
        return
    except PermissionError:
        print(f"Ошибка: нет доступа к файлу '{input_filename}'.", file=sys.stderr)
        return
    except UnicodeDecodeError:
        print(f"Ошибка: проблема с кодировкой файла '{input_filename}' (ожидается UTF-8).", file=sys.stderr)
        return
    except ValueError as e:
        print(f"Ошибка валидации данных: {e}", file=sys.stderr)
        return
    except Exception as e:
        print(f"Непредвиденная ошибка при чтении: {e}", file=sys.stderr)
        return

    row_sums = [sum(row) for row in matrix]

    num_cols = len(matrix[0]) if matrix else 0
    col_sums = []
    for col_idx in range(num_cols):
        col_sum = sum(matrix[row_idx][col_idx] for row_idx in range(len(matrix)))
        col_sums.append(col_sum)

    report_content = (
        f"Суммы строк: {' '.join(map(str, row_sums))}\n"
        f"Суммы столбцов: {' '.join(map(str, col_sums))}\n"
    )

    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(report_content)
    except Exception as e:
        print(f"Ошибка при записи файла '{output_filename}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
