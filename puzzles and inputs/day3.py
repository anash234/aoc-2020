input3 = open('input3.txt')
map = [i[0:-1] for i in input3.readlines()]


def tree_count_3_1(slope):
    current_pos = [0, 0]
    trees_hit = 0
    while current_pos[1] < len(slope) - 1:
        while current_pos[0] + 3 > len(slope[current_pos[1] + 1]):
            slope[current_pos[1] + 1] = slope[current_pos[1] + 1] * 2
        if slope[current_pos[1]][current_pos[0]] == '#':
            trees_hit += 1
        current_pos[0] += 3
        current_pos[1] += 1
    if slope[current_pos[1]][current_pos[0]] == '#':
        trees_hit += 1
    return trees_hit


def tree_count_1_1(slope):
    current_pos = [0, 0]
    trees_hit = 0
    while current_pos[1] < len(slope) - 1:
        while current_pos[0] + 1 > len(slope[current_pos[1] + 1]):
            slope[current_pos[1] + 1] = slope[current_pos[1] + 1] * 2
        if slope[current_pos[1]][current_pos[0]] == '#':
            trees_hit += 1
        current_pos[0] += 1
        current_pos[1] += 1
    if slope[current_pos[1]][current_pos[0]] == '#':
        trees_hit += 1
    return trees_hit


def tree_count_5_1(slope):
    current_pos = [0, 0]
    trees_hit = 0
    while current_pos[1] < len(slope) - 1:
        while current_pos[0] + 5 > len(slope[current_pos[1] + 1]):
            slope[current_pos[1] + 1] = slope[current_pos[1] + 1] * 2
        if slope[current_pos[1]][current_pos[0]] == '#':
            trees_hit += 1
        current_pos[0] += 5
        current_pos[1] += 1
    if slope[current_pos[1]][current_pos[0]] == '#':
        trees_hit += 1
    return trees_hit


def tree_count_7_1(slope):
    current_pos = [0, 0]
    trees_hit = 0
    while current_pos[1] < len(slope) - 1:
        while current_pos[0] + 7 > len(slope[current_pos[1] + 1]):
            slope[current_pos[1] + 1] = slope[current_pos[1] + 1] * 2
        if slope[current_pos[1]][current_pos[0]] == '#':
            trees_hit += 1
        current_pos[0] += 7
        current_pos[1] += 1
    if slope[current_pos[1]][current_pos[0]] == '#':
        trees_hit += 1
    return trees_hit


def tree_count_7_2(slope):
    current_pos = [0, 0]
    trees_hit = 0
    while current_pos[1] < len(slope) - 1:
        while current_pos[0] + 7 > len(slope[current_pos[1] + 2]):
            slope[current_pos[1] + 2] = slope[current_pos[1] + 2] * 2
        if slope[current_pos[1]][current_pos[0]] == '#':
            trees_hit += 1
        current_pos[0] += 7
        current_pos[1] += 2
    if slope[current_pos[1]][current_pos[0]] == '#':
        trees_hit += 1
    return trees_hit


print(tree_count_3_1(map))
print(tree_count_1_1(map))
print(tree_count_5_1(map))
print(tree_count_7_1(map))
print(tree_count_7_2(map))

print(tree_count_3_1(map) * tree_count_1_1(map) * tree_count_5_1(map) * tree_count_7_1(map) * tree_count_7_2(map))
