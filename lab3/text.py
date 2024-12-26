# text_module.py
def print_table(table):
    for row in table:
        print('\t'.join(map(str, row)))

def save_table(file_path, table):
    with open(file_path, 'w') as file:
        for row in table:
            file.write('\t'.join(map(str, row)) + '\n')
