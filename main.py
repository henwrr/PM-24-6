# main.py
import table as t
import datetime

# Пример таблицы
table = [
    ["Имя", "Возраст", "Пол", "Дата рождения"],
    ["Катя", 30, "ж", "20-12-2010"],
    ["Толя", 25, "м", "10-02-2015"],
    ["Вова", 35, "м", "28-05-2006"]]

# Сохранение таблицы в CSV
t.save_table_csv('table.csv', table)

# Загрузка таблицы из CSV
loaded_table_csv = t.load_table_csv('table.csv')
print('--'*50)
print("Загрузка CSV:")
t.print_table(loaded_table_csv)
print('--'*50)

# Сохранение таблицы в Pickle
t.save_table_pickle('table.pkl', table)

# Загрузка таблицы из Pickle
loaded_table_pickle = t.load_table_pickle('table.pkl')
print('--'*50)
print("\nЗагрузка из Pickle:")
t.print_table(loaded_table_pickle)
print('--'*50)

# Сохранение таблицы в текстовый файл
t.save_table_text('table.txt', table)

# Получение строк по номеру
print("Строки с номерами 1 и 2:")
rows_by_number = t.get_rows_by_number(table, 1, 3)
t.print_table(rows_by_number)
print('--'*50)

# Получение строк по значению в первом столбце
print("Строки с именами 'Катя' и 'Вова':")
rows_by_index = t.get_rows_by_index(table, "Катя", "Вова")
t.print_table(rows_by_index)
print('--'*50)

# Получение типов столбцов
print("\nТипы столбцов (по номеру):")
column_types_by_index = t.get_column_types(table, use_numeric_index=True)
print(column_types_by_index)
print('--'*50)

print("\nТипы столбцов (по имени):")
column_types_by_name = t.get_column_types(table, use_numeric_index=False)
print(column_types_by_name)
print('--'*50)

# Задание типов столбцов
print("\nЗадание типов столбцов (по номеру):")
t.set_column_types(table, {1: str, 2: str}, use_numeric_index=True)
column_types_by_index = t.get_column_types(table, use_numeric_index=True)
print(column_types_by_index)
print('--'*50)

print("\nЗадание типов столбцов (по имени):")
t.set_column_types(table, {"Возраст": str, "Пол": str}, use_numeric_index=False)
column_types_by_name = t.get_column_types(table, use_numeric_index=False)
print(column_types_by_name)
print('Все столбцы теперь str')
print('--'*50)

# Получение значений из столбца
print("\nЗначения из столбца 'Возраст':")
values = t.get_values(table, column="Возраст")
print(values)
print('--'*50)

print("\nЗначение из столбца 'Возраст' для первой строки:")
value = t.get_value(table, column="Возраст")
print(value)
print('--'*50)

# Задание значений в столбец
print("\nЗадание значений в столбец 'Возраст':")
t.set_values(table, [10, 20, 100, 200], column="Возраст")
t.print_table(table)
print('--'*50)

print("\nЗадание значения в столбец 'Возраст' для первой строки:")
t.set_value(table, 0, column="Возраст")
t.print_table(table)
print('--'*50)

table1 = [
    ["Имя", "Возраст", "Пол", "Дата рождения"],
    ["Катя", 30, "ж", "20-12-2010"],
    ["Толя", 25, "м", "10-02-2015"]]

table2 = [
    ["Имя", "Возраст", "Пол", "Дата рождения"],
    ["Вова", 35, "м", "28-05-2006"]]

print('\nДве отдельные таблицы')
t.print_table(table1)
print('--'*50)
t.print_table(table2)
print('--'*50)

t.save_table_csv('table1.csv', table1)
t.save_table_csv('table2.csv', table2)

# Загрузка таблиц из CSV
loaded_table_csv = t.load_table_csv('table1.csv', 'table2.csv')
print('--'*50)
print("Загрузка из 2-х таблиц CSV:")
t.print_table(loaded_table_csv)
print('--'*50)

# Сохранение таблиц в Pickle
t.save_table_pickle('table1.pkl', table1)
t.save_table_pickle('table2.pkl', table2)

# Загрузка таблиц из Pickle
loaded_table_pickle = t.load_table_pickle('table1.pkl', 'table2.pkl')
print('--'*50)
print("Загрузка из 2-х таблиц Pickle:")
t.print_table(loaded_table_pickle)
print('--'*50)

table = [
    ["Имя", "Возраст", "Пол", "Дата рождения"],
    ["Катя", 30, "ж", "20-12-2010"],
    ["Толя", 25, "м", "10-02-2015"],
    ["Вова", 35, "м", "28-05-2006"],
    ["Маша", 28, "ж", "15-07-2003"],
    ["Петя", 32, "м", "05-09-2001"]]

print('\nНовая таблица')
t.print_table(table)
print('--'*50)

# Сохранение таблицы в CSV, разбитой на несколько файлов
t.save_table_csv('table.csv', table, max_rows=2)

# Загрузка таблицы из CSV, разбитой на несколько файлов
loaded_table_csv1 = t.load_table_csv('table_1.csv')
print('--'*50)
loaded_table_csv2 = t.load_table_csv('table_2.csv')
print('--'*50)
loaded_table_csv3 = t.load_table_csv('table_3.csv')
print('--'*50)

print("Загрузка разбитых таблиц CSV:")
print("\nПервая таблица:")
t.print_table(loaded_table_csv1)
print("\nВторая таблица:")
t.print_table(loaded_table_csv2)
print("\nТретья таблица:")
t.print_table(loaded_table_csv3)
print('--'*50)

# Сохранение таблицы в Pickle, разбитой на несколько файлов
t.save_table_pickle('table.pkl', table, max_rows=2)

# Загрузка таблицы из Pickle, разбитой на несколько файлов
loaded_table_pickle = t.load_table_pickle('table_1.pkl', 'table_2.pkl', 'table_3.pkl')
print('--'*50)
print("\nЗагрузка из 3-х таблиц Pickle:")
t.print_table(loaded_table_pickle)
print('--'*50)

print('\nДве отдельные таблицы')
t.print_table(loaded_table_csv1)
print('--'*50)
t.print_table(loaded_table_csv2)
print('--'*50)

# Склеивание таблиц
concatenated_table = t.concat(table1, table2)
print("\nСклеенная таблица:")
t.print_table(concatenated_table)
print('--'*50)

# Разбиение таблицы
split_table1, split_table2 = t.split(concatenated_table, 3)
print("\nПервая часть разбитой таблицы:")
t.print_table(split_table1)
print('--'*50)
print("\nВторая часть разбитой таблицы:")
t.print_table(split_table2)
print('--'*50)

# Вывод таблицы на печать
print("Оригинальная таблица:")
t.print_table(concatenated_table)

# Преобразование столбца "Дата рождения" в datetime
t.convert_column_to_datetime(concatenated_table, column="Дата рождения")
print("\nТипы столбцов после преобразования:")
column_types_by_name = t.get_column_types(concatenated_table, use_numeric_index=False)
print(column_types_by_name)
print('--'*50)

# Пример таблицы без пустых ячеек
table1 = [
    ["Имя", "Оценка", "Пол"],
    ["Катя", 30, "ж"],
    ["Толя", 25, "м"],
    ["Вова", 35, "м"]
]

table2 = [
    ["Имя", "Оценка", "Пол"],
    ["Катя", 10, "ж"],
    ["Толя", 5, "м"],
    ["Вова", 0, "м"]]

print("Оригинальная таблица 1:")
t.print_table(table1)
print('--'*50)

print("Оригинальная таблица 2:")
t.print_table(table2)
print('--'*50)

# Сложение столбцов "Оценка"
result_table_add = t.add(table1, table2, "Оценка", "Оценка", "Сумма")
print("Сложения оценок:")
t.print_table(result_table_add)
print('--'*50)

# Вычитание столбцов "Оценка"
result_table_sub = t.sub(table1, table2, "Оценка", "Оценка", "Разность")
print("\nТаблица после вычитания:")
t.print_table(result_table_sub)
print('--'*50)

# Умножение столбцов "Оценка"
result_table_mul = t.mul(table1, table2, "Оценка", "Оценка", "Произведение")
print("\nТаблица после умножения:")
t.print_table(result_table_mul)
print('--'*50)

# Деление столбцов "Оценка"
result_table_div = t.div(table1, table2, "Оценка", "Оценка", "Частное")
print("\nТаблица после деления:")
t.print_table(result_table_div)
print('--'*50)

table1 = [
    ["Имя", "Оценка", "Пол"],
    ["Катя", 30, "ж"],
    ["Толя", 25, "м"],
    ["Вова", 35, "м"]
]

table2 = [
    ["Имя", "Оценка", "Пол"],
    ["Катя", 10, "ж"],
    ["Толя", 5, "м"]]

# Сложение столбцов разноразмерных таблиц
result_table_add = t.add(table1, table2, "Оценка", "Оценка", "Сумма")
print("Сложения оценок:")
t.print_table(result_table_add)
print('--'*50)