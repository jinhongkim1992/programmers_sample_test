def solution(priorities, location):
    answer = 0
    printed_list = []
    index_list = list(range(len(priorities)))
    temp_dict = {}

    for i,j in enumerate(priorities):
        temp_dict[i] = j

    while len(index_list) != 0:
        temp = index_list.pop(0)

        if all(temp_dict[temp] >= temp_dict[i] for i in index_list):
            printed_list.append(temp)
        else:
            index_list.append(temp)

    return printed_list.index(location) + 1
