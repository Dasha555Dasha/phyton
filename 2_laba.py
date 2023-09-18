def create_sublists(lst):
    result = []
    for num in lst:
        sublist = list(range(num + 1))
        result.append(sublist)
    return result
my_list = [5, 7, 3]
sublists = create_sublists(my_list)
print(sublists)
