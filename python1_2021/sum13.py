def sum13(nums):
    diff_list = nums

    if diff_list == 0 or diff_list[0] == 13:
        return 0
    elif 13 in diff_list:
        lucky13 = diff_list.index(13)
        print("lucky13 ", lucky13)
        first_half = diff_list[0:lucky13]
        print(first_half)
        return (sum(first_half))
    else:
        return sum(diff_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sum13([1, 2, 2, 1]))
    print(sum13([13, 1, 2, 13, 2, 1, 13]) )
    print(sum13([1, 2, 2, 1]))
    print(sum13([1, 2, 13, 2, 1, 13]))
    print(sum13([13, 1, 2, 13, 2, 1, 13]))
    print(sum13([1, 1]))


