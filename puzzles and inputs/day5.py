input5 = open('input5.txt')
boarding_passes = [i[0:-1] for i in input5.readlines()]
seat_list = []


def find_row_column(seat, range_rows, range_columns):
    global seat_list
    lowest_row = range_rows[0]
    mid_row = range_rows[len(range_rows) // 2]
    highest_row = range_rows[-1]
    lowest_column = range_columns[0]
    mid_column = range_columns[len(range_columns) // 2]
    highest_column = range_columns[-1]
    if len(seat) == 0:
        seat_list.append([range_rows[0], range_columns[0]])
        return [range_rows[0], range_columns[0]]
    if len(seat) == 1:
        if seat == 'L':
            range_columns = range(lowest_column, mid_column + 1)
        elif seat == 'R':
            range_columns = range(mid_column, highest_column + 1)
        seat_list.append([range_rows[0], range_columns[0]])
        return [range_rows[0], range_columns[0]]
    if seat[0] == 'F':
        range_rows = range(lowest_row, mid_row + 1)
        return find_row_column(seat[1:], range_rows, range_columns)
    elif seat[0] == 'B':
        range_rows = range(mid_row, highest_row + 1)
        return find_row_column(seat[1:], range_rows, range_columns)
    elif seat[0] == 'L':
        range_columns = range(lowest_column, mid_column + 1)
        return find_row_column(seat[1:], range_rows, range_columns)
    elif seat[0] == 'R':
        range_columns = range(mid_column, highest_column + 1)
        return find_row_column(seat[1:], range_rows, range_columns)


def find_seats(passes):
    global seat_list
    seat_id_list = []
    for p in passes:
        find_row_column(p, range(128), range(8))
    for s in seat_list:
        seat_id = (s[0] * 8) + s[1]
        seat_id_list.append(seat_id)
    return seat_id_list


print(find_seats(boarding_passes))


def find_missing_seats(id_list):
    possible_id_list = []
    missing_id_list = []
    for r in range(128):
        for c in range(8):
            possible_id = ((r * 8) + c)
            possible_id_list.append(possible_id)
    for seat in possible_id_list:
        if seat not in id_list:
            missing_id_list.append(seat)
    return missing_id_list


print(find_missing_seats(find_seats(boarding_passes)))
