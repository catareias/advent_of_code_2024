def calc_distance_of_two_lists(list1, list2):
    total_distance = 0
    for index, list1_value in enumerate(list1):
        list2_value = list2[index]
        distance = abs(list1_value - list2_value)
        total_distance += distance
    return total_distance

def calc_similarity_of_two_lists(list1, list2):
    total_similarity = 0
    for list1_value in list1:
        # list2_filtered = list(filter(lambda a: a == list1_value, list2))
        list2_filtered = [list2_value for list2_value in list2 if list2_value == list1_value]
        similarity = len(list2_filtered) * list1_value
        total_similarity += similarity
    return total_similarity

def calc_safety_of_reports(reports, acceptable_deltas):
    safe_counter = 0
    for report in reports:
        start_level = int(report[0])
        start_diff = int(report[1]) - start_level

        for index, level in enumerate(report[1:]):
            # index is one behind
            diff = int(level) - int(report[index])
            if diff not in acceptable_deltas or diff * start_diff <= 0:
                # diff of 0 is not acceptable
                # diff * start_diff <= 0 means they are not the same sign
                # diff * start_diff < 0 means they are the same sign and diff is not 0
                break
            else:
                # setup for next iteration
                start_diff = diff
                # if we make it to end of list without breaking, we have a safe report
                if index == len(report) - 2:
                    safe_counter += 1

    return safe_counter
