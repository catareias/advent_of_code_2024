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