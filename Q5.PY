def find_duplicates(arr):
    duplicates = []
    num_dict = {}

    for num in arr:
        if num in num_dict:
            duplicates.append(num)
        else:
            num_dict[num] = 1

    return duplicates

arr = [1, 2, 3, 2, 4, 5, 3, 6]
duplicate_nums = find_duplicates(arr)
print("Duplicate numbers:", duplicate_nums)