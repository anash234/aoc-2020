input4 = open('input4.txt')
raw_data = [i[0:-1] for i in input4.readlines()]

raw_data_1 = raw_data[0:407]
raw_data_2 = raw_data[407:577]
raw_data_3 = raw_data[577:886]
raw_data_4 = raw_data[886:]

passport_list = []
passport = {}


def data_collection(data_list):
    global passport_list
    global passport
    if len(data_list) == 0:
        passport_list.append(passport)
        passport = {}
        return
    elif data_list[0] == '':
        passport_list.append(passport)
        passport = {}
        return data_collection(data_list[1:])
    else:
        if ':' in data_list[0]:
            colon_index = data_list[0].index(':')
            key = data_list[0][0:colon_index]
            if ' ' in data_list[0]:
                space_index = data_list[0].index(' ')
                value = data_list[0][colon_index + 1:space_index]
                passport[key] = value
                data_list[0] = data_list[0][space_index + 1:]
                return data_collection(data_list)
        value = data_list[0][colon_index + 1:]
        passport[key] = value
        return data_collection(data_list[1:])


data_collection(raw_data_1)
data_collection(raw_data_2)
data_collection(raw_data_3)
data_collection(raw_data_4)


def validate(passports):
    valid_passports = []
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for p in passports:
        if all(item in p for item in required):
            valid_passports.append(p)
    return valid_passports


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def check_byr(byr):
    if len(byr) != 4:
        return False
    if not is_int(byr):
        return False
    if 1920 <= int(byr) <= 2002:
        return True
    return False


def check_iyr(iyr):
    if type(iyr) != str:
        return False
    if not is_int(iyr):
        return False
    if len(iyr) != 4:
        return False
    if 2010 <= int(iyr) <= 2020:
        return True
    return False


def check_eyr(eyr):
    if len(eyr) != 4:
        return False
    if not is_int(eyr):
        return False
    if 2020 <= int(eyr) <= 2030:
        return True
    return False


def check_hgt(hgt):
    if len(hgt) != 4 and len(hgt) != 5:
        return False
    if not is_int(hgt[0:-2]):
        return False
    if hgt[-2:] != 'cm' and hgt[-2:] != 'in':
        return False
    elif hgt[-2:] == 'cm':
        if 150 <= int(hgt[0:-2]) <= 193:
            return True
        return False
    elif hgt[-2:] == 'in':
        if 59 <= int(hgt[0:-2]) <= 76:
            return True
        return False


def check_hcl(hcl):
    characters = '0123456789abcdef'
    if len(hcl) != 7:
        return False
    if hcl[0] == '#':
        if all(chara in characters for chara in hcl[1:]):
            return True
    return False


def check_ecl(ecl):
    colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if len(ecl) == 3:
        if ecl in colours:
            return True
    return False


def check_pid(pid):
    if is_int(pid) and len(pid) == 9:
        return True
    return False


def num_valid(passports):
    valid = 0
    for p in passports:
        tests = [check_byr(p['byr']), check_iyr(p['iyr']), check_eyr(p['eyr']), check_hgt(p['hgt']),
                 check_hcl(p['hcl']), check_ecl(p['ecl']), check_pid(p['pid'])]
        if all(test == True for test in tests):
            valid += 1
    return valid


example_list = [{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
                 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'},
                {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884',
                    'hcl':  '#cfa07d', 'byr': '1929'},
                {'hcl': '#ae17e1', 'iyr': '2013',
                 'eyr': '2024',
                 'ecl': 'brn', 'pid': '760753108', 'byr': '1931',
                 'hgt': '179cm'},
                {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648',
                 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}]

print(validate(example_list))
print(num_valid(validate(passport_list)))