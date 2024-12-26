# csv_module.py
import csv
import os
import datetime

def auto_detect_column_types(table):
    column_types = {}
    num_columns = len(table[0])

    for col_num in range(num_columns):
        column_data = [row[col_num] for row in table[1:]]  # Пропускаем заголовок
        column_type = str  # Начальное значение типа

        for value in column_data:
            if isinstance(value, bool):
                column_type = bool
            elif isinstance(value, float):
                column_type = float
            elif isinstance(value, int):
                column_type = int
            elif isinstance(value, datetime.datetime):
                column_type = datetime.datetime
            elif isinstance(value, str):
                try:
                    datetime.datetime.strptime(value, "%d-%m-%Y")
                    column_type = datetime.datetime
                except ValueError:
                    column_type = str

        column_types[table[0][col_num]] = column_type

    return column_types

def load_table(*file_paths, auto_detect_types=False):
    if not file_paths:
        raise ValueError("Необходимо указать хотя бы один файл для загрузки.")

    table = []
    header = None

    for file_path in file_paths:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            if not header:
                header = rows[0]
                table.append(header)
                table.extend(rows[1:])
            else:
                if rows[0] != header:
                    raise ValueError(f"Структура столбцов в файле {file_path} не соответствует структуре столбцов предыдущих файлов.")
                table.extend(rows[1:])

    column_types = auto_detect_column_types(table)
    print("Загружена таблица:")
    for col_name, col_type in column_types.items():
        print(f"{col_name}: {col_type.__name__}")

    return table

def save_table(file_path, table, max_rows=None):
    if max_rows is None:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(table)
    else:
        base_name, ext = os.path.splitext(file_path)
        header = table[0]
        rows = table[1:]
        for i in range(0, len(rows), max_rows):
            chunk = rows[i:i + max_rows]
            chunk_file_path = f"{base_name}_{i // max_rows + 1}{ext}"
            with open(chunk_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(chunk)