input2 = open('input2.txt')
passwords = [i[0:-1] for i in input2.readlines()]


def sled_password_check(password_list):
    valid_passwords = 0
    for item in password_list:
        if item[1] == '-' and item[3] == ' ':
            least_allowed = int(item[0])
            most_allowed = int(item[2])
            letter = item[4]
            password = item[7:]
        elif item[1] == '-' and item[4] == ' ':
            least_allowed = int(item[0])
            most_allowed = int(item[2:4])
            letter = item[5]
            password = item[8:]
        elif item[2] == '-' and item[5] == ' ':
            least_allowed = int(item[0:2])
            most_allowed = int(item[3:5])
            letter = item[6]
            password = item[9:]
        letter_count = 0
        for chara in password:
            if chara == letter:
                letter_count += 1
        if least_allowed <= letter_count <= most_allowed:
            valid_passwords += 1
    return valid_passwords


def toboggan_password_check(password_list):
    valid_passwords = 0
    for item in password_list:
        if item[1] == '-' and item[3] == ' ':
            pos_1 = int(item[0])
            pos_2 = int(item[2])
            letter = item[4]
            password = item[7:]
        elif item[1] == '-' and item[4] == ' ':
            pos_1 = int(item[0])
            pos_2 = int(item[2:4])
            letter = item[5]
            password = item[8:]
        elif item[2] == '-' and item[5] == ' ':
            pos_1 = int(item[0:2])
            pos_2 = int(item[3:5])
            letter = item[6]
            password = item[9:]
        # print(item, pos_1, pos_2, letter, password)
        if password[pos_1 - 1] != letter:
            check_1 = False
        else:
            check_1 = True
        if password[pos_2 - 1] != letter:
            check_2 = False
        else:
            check_2 = True
        if check_1 ^ check_2:
            valid_passwords += 1
            print(item, pos_1, pos_2, letter, password, check_1, check_2)
    return valid_passwords


print(sled_password_check(passwords))
print(toboggan_password_check(passwords))