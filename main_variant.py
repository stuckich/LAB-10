import sys
from files_lab import read_matrix
from table import selected_sum

def main():
    input_filename = "matrix.txt"
    report_filename = "report.txt"

    try:
        matrix = read_matrix(input_filename)
    except Exception as e:
        print(f"Ошибка при чтении файла {input_filename}: {e}", file=sys.stderr)
        return

    row_sums = [sum(row) for row in matrix]

    if matrix and matrix[0]:
        col_sums = [sum(col) for col in zip(*matrix)]
    else:
        col_sums = []

    indiv_result = selected_sum(matrix)

    report_lines = [
        f"Суммы строк: {' '.join(map(str, row_sums))}",
        f"Суммы столбцов: {' '.join(map(str, col_sums))}",
        f"Результат варианта: {indiv_result}"
    ]
    report_content = "\n".join(report_lines) + "\n"

    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"Отчет успешно записан в {report_filename}")
    except OSError as e:
        print(f"Ошибка записи в файл {report_filename}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
