def make_bricks(number_small, number_large, goal):

    small_size = 1
    large_size = 5
    large_bricks_used = 0
    small_bricks_used = 0
    space_used = 0
    print("space used: ", space_used)

    print(number_large)
    print(large_bricks_used)
    print("Goal: ", goal)

    while space_used <= goal:
        while large_bricks_used <= number_large:
            print("large bricks used: ", large_bricks_used)
            print("Space used: ", space_used)
            large_bricks_used += 1
            space_used += large_size


        while small_bricks_used <= number_small:
            print("small bricks used: ", small_bricks_used)
            print("Space used: ", space_used)
            small_bricks_used += 1
            space_used += small_size



if __name__ == '__main__':
   print(make_bricks(3, 1, 8))
   print(make_bricks(3, 1, 9))
   print(make_bricks(3, 2, 10))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
