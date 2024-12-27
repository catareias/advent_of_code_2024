def export_from_file(filename):
    with open(filename, 'r') as file:
        rows = file.read().splitlines()
        list1 = []
        list2 = []
        for row in rows:
            columns = row.split('   ')
            list1.append(int(columns[0]))
            list2.append(int(columns[-1]))
        return  list1, list2