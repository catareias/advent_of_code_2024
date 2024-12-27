def export_rows_from_file(filename):
    with open(filename, 'r') as file:
        rows = file.read().splitlines()
        return rows
    
def split_rows_into_columns(rows):
    list1 = []
    list2 = []
    for row in rows:
        columns = row.split('   ')
        list1.append(int(columns[0]))
        list2.append(int(columns[-1]))
    return  list1, list2

def split_rows_into_values(rows):
    values = [value.split(' ') for value in rows]
    return values

def export_columns_from_file(filename):
    rows = export_rows_from_file(filename)
    return split_rows_into_columns(rows)