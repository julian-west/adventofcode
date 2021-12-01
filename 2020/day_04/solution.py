"""
Part 1 requirements:
    - should contain the eight fields
    - however, 'cid' can be missing and the passport is still valid

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
"""
import numpy as np
import re


def load_input(file):
    """Load passport info into list of dictionaries"""

    with open(file, "r") as f:
        lines = f.read()

    info = lines.split("\n\n")
    return info


def process_passport_info(passport_info):
    """Parses info and converts to dictionary of key:value pairs"""
    fields = passport_info.split()

    passport_dict = {}
    for field in fields:
        key, value = field.split(":")
        passport_dict[key] = value

    return passport_dict


def check_byr(byr):
    if len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002:
        return True
    else:
        return False


def check_iyr(iyr):
    if len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    else:
        return False


def check_eyr(eyr):
    if len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
        return True
    else:
        return False


def check_hgt(hgt):

    try:
        number, unit = re.match("(\d+)(\w+)", hgt).groups()

        if unit == "cm":
            assert int(number) >= 150 and int(number) <= 193
            return True
        elif unit == "in":
            assert int(number) >= 59 and int(number) <= 76
            return True
        else:
            return False
    except:
        return False


def check_hcl(hcl):
    if re.match("^#(?:[0-9a-f]{6})$", hcl):
        return True
    else:
        return False


def check_ecl(ecl):
    acceptable_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in acceptable_values:
        return True
    else:
        return False


def check_pid(pid):
    if re.match("^\d{9}$", pid):
        return True
    else:
        return False


def validity_test(passport_dict):
    """Return True if passport is valid"""
    if len(passport_dict) == 7:

        byr_check = check_byr(passport_dict["byr"])
        iyr_check = check_iyr(passport_dict["iyr"])
        eyr_check = check_eyr(passport_dict["eyr"])
        hgt_check = check_hgt(passport_dict["hgt"])
        hcl_check = check_hcl(passport_dict["hcl"])
        ecl_check = check_ecl(passport_dict["ecl"])
        pid_check = check_pid(passport_dict["pid"])

        if all(
            [
                byr_check,
                iyr_check,
                eyr_check,
                hgt_check,
                hcl_check,
                ecl_check,
                pid_check,
            ]
        ):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":

    info = load_input("input.txt")

    results = []
    for passport in info:
        passport_info = process_passport_info(passport)
        passport_info.pop("cid", None)
        is_valid = validity_test(passport_info)

        results.append(is_valid)

    print(np.sum(results))
