def find_two_numbers(L):
    for entry_1 in L:
        for entry_2 in L:
            if entry_1 != entry_2 and entry_1 + entry_2 == 2020:
                return entry_1 * entry_2


def find_three_numbers(L):
    for entry_1 in L:
        for entry_2 in L:
            for entry_3 in L:
                if entry_1 != entry_2 != entry_3 and entry_1 + entry_2 + entry_3 == 2020:
                    return entry_1 * entry_2 * entry_3


input1 = open('input1.txt')
file_items = input1.readlines()
expense_report = [int(i[0:-1]) for i in file_items]
print(find_two_numbers(expense_report))
print(find_three_numbers(expense_report))