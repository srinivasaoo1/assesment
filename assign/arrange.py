def get_distinct_elements(input_list):
    unique_elements = []
    seen = set()

    for item in input_list:
        if item not in seen:
            unique_elements.append(item)
            seen.add(item)

    return unique_elements

input_list = eval(input('the the list:'))
distinct_elements = get_distinct_elements(input_list)
print(distinct_elements)
