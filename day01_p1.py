from helpers.file_helpers import export_from_file
from helpers.list_helpers import calc_distance_of_two_lists

# file into list:
data = export_from_file("inputs/day01.txt")

# sort 
list1 = sorted(data[0])
list2 = sorted(data[1])

# iterate through and sum up --> abs value
total_distance = calc_distance_of_two_lists(list1, list2)

print(total_distance) 

