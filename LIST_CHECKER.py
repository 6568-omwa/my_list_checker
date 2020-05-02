def list_checker(num_list):
    """Checks for missing number in a list"""
    first = num_list[0]
    last = num_list[-1]
    numbers = sorted(set(range(first, last + 1)).difference(num_list))
    return numbers
num_list = [1,2,3,5,7,8]
print(list_checker(num_list))
