from helpers.file_helpers import export_rows_from_file, split_rows_into_values
from helpers.list_helpers import calc_safety_of_reports

reports = split_rows_into_values(export_rows_from_file("inputs/day02_p1.txt"))

acceptable_deltas = [-3, -2, -1, 1, 2, 3]

safety = calc_safety_of_reports(reports, acceptable_deltas)

print(safety)
