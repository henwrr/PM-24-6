# table_operations.py
import datetime

def print_table(table):
    for row in table:
        print('\t'.join(map(str, row)))

def get_rows_by_number(table, start_index, end_index=None, copy_table=False):
    if end_index is None:
        end_index = start_index + 1
    rows = table[start_index:end_index]
    if copy_table:
        return [row[:] for row in rows]
    return rows

def get_rows_by_index(table, *index_values, copy_table=False):
    rows = [row for row in table if row[0] in index_values]
    if copy_table:
        return [row[:] for row in rows]
    return rows

def get_column_types(table, use_numeric_index=True):
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
                column_type = str

        if use_numeric_index:
            column_types[col_num] = column_type
        else:
            column_types[table[0][col_num]] = column_type

    return column_types

def set_column_types(table, types_dict, use_numeric_index=True):
    for col_key, col_type in types_dict.items():
        col_num = col_key if use_numeric_index else table[0].index(col_key)
        for row in table[1:]:
            try:
                row[col_num] = col_type(row[col_num])
            except ValueError:
                print(f"Невозможно преобразовать значение '{row[col_num]}' в тип {col_type} для столбца {col_num}")

def get_values(table, column=0):
    if isinstance(column, str):
        column = table[0].index(column)
    column_type = get_column_types(table, use_numeric_index=True)[column]
    return [column_type(row[column]) for row in table[1:]]

def get_value(table, column=0):
    if isinstance(column, str):
        column = table[0].index(column)
    column_type = get_column_types(table, use_numeric_index=True)[column]
    return column_type(table[1][column])

def set_values(table, values, column=0):
    if isinstance(column, str):
        column = table[0].index(column)
    column_type = get_column_types(table, use_numeric_index=True)[column]
    num_rows = len(table) - 1  # Исключаем заголовок
    if len(values) > num_rows:
        print(f"Переданных значений много ({len(values)}), использовались первые {num_rows}.")
        values = values[:num_rows]  # Используем только первые значения, если список длиннее
    for i, value in enumerate(values):
        table[i + 1][column] = column_type(value)

def set_value(table, value, column=0):
    if isinstance(column, str):
        column = table[0].index(column)
    column_type = get_column_types(table, use_numeric_index=True)[column]
    table[1][column] = column_type(value)

def concat(table1, table2):
    if table1[0] != table2[0]:
        raise ValueError("Структура столбцов таблиц не совпадает.")
    return table1 + table2[1:]

def split(table, row_number):
    if row_number <= 0 or row_number >= len(table):
        raise ValueError("Некорректный номер строки для разбиения таблицы.")
    return table[:row_number], table[row_number:]

def convert_column_to_datetime(table, column):
    if isinstance(column, str):
        column = table[0].index(column)
    for row in table[1:]:
        try:
            row[column] = datetime.datetime.strptime(row[column], "%d-%m-%Y")
        except ValueError:
            print(f"Невозможно преобразовать значение '{row[column]}' в формат даты для столбца {column}")


def add(table1, table2, column1, column2, result_column):
    if isinstance(column1, str):
        column1 = table1[0].index(column1)
    if isinstance(column2, str):
        column2 = table2[0].index(column2)

    if len(table1) != len(table2):
        raise ValueError("Таблицы должны иметь одинаковую длину.")

    # Создаем новую таблицу с результатами
    result_table = [table1[0] + [result_column]]
    for i in range(1, len(table1)):
        result_row = table1[i][:]
        result_row.append(table1[i][column1] + table2[i][column2])
        result_table.append(result_row)

    return result_table

def sub(table1, table2, column1, column2, result_column):
    if isinstance(column1, str):
        column1 = table1[0].index(column1)
    if isinstance(column2, str):
        column2 = table2[0].index(column2)

    if len(table1) != len(table2):
        raise ValueError("Таблицы должны иметь одинаковую длину.")

    # Создаем новую таблицу с результатами
    result_table = [table1[0] + [result_column]]
    for i in range(1, len(table1)):
        result_row = table1[i][:]
        result_row.append(table1[i][column1] - table2[i][column2])
        result_table.append(result_row)

    return result_table

def mul(table1, table2, column1, column2, result_column):
    if isinstance(column1, str):
        column1 = table1[0].index(column1)
    if isinstance(column2, str):
        column2 = table2[0].index(column2)

    if len(table1) != len(table2):
        raise ValueError("Таблицы должны иметь одинаковую длину.")

    # Создаем новую таблицу с результатами
    result_table = [table1[0] + [result_column]]
    for i in range(1, len(table1)):
        result_row = table1[i][:]
        result_row.append(table1[i][column1] * table2[i][column2])
        result_table.append(result_row)

    return result_table

def div(table1, table2, column1, column2, result_column):
    if isinstance(column1, str):
        column1 = table1[0].index(column1)
    if isinstance(column2, str):
        column2 = table2[0].index(column2)

    if len(table1) != len(table2):
        raise ValueError("Таблицы должны иметь одинаковую длину.")

    # Создаем новую таблицу с результатами
    result_table = [table1[0] + [result_column]]
    for i in range(1, len(table1)):
        result_row = table1[i][:]
        try:
            result_row.append(table1[i][column1] / table2[i][column2])
        except ZeroDivisionError:
            print(f"Деление на ноль в строке {i}.")
            result_row.append(None)
        result_table.append(result_row)

    return result_table