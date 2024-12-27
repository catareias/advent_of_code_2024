from helpers.file_helpers import export_columns_from_file
from helpers.list_helpers import calc_similarity_of_two_lists

# file into list:
data = export_columns_from_file("inputs/day01_p2.txt")
list1 = data[0]
list2 = data[1]

total_similarity = calc_similarity_of_two_lists(list1, list2)

print(total_similarity)