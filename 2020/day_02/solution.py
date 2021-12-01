"""
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""


def load_input(file):
    """Load input into named tuple
    (min, max, letter, password)
    """
    with open(file, "r") as f:
        lines = f.readlines()

    raw = [line.split() for line in lines]

    inputs = []
    for record in raw:
        min, max = [int(n) for n in record[0].split("-")]
        letter = record[1][0]
        password = record[2]
        inputs.append((min, max, letter, password))

    return inputs


def check_fn(min, max, letter, password):
    """Checks if it is a valid password"""

    occurances = password.count(letter)
    if occurances >= min and occurances <= max:
        return True
    else:
        return False


def part_2_fn(pos1, pos2, letter, password):
    """Checks if the letter is in exactly one of pos1 or pos2"""

    if password[pos1 - 1] == letter and password[pos2 - 1] == letter:
        return False
    elif password[pos1 - 1] == letter:
        return True
    elif password[pos2 - 1] == letter:
        return True
    else:
        return False


if __name__ == "__main__":
    records = load_input("input.txt")

    "Need to apply check_fn to the whole input list and count booleans"
    check = [check_fn(*record) for record in records]
    print(f"Valid passwords for policy 1 = {sum(check)}")

    policy_2_check = [part_2_fn(*record) for record in records]
    print(f"Valid passwords for policy 2 = {sum(policy_2_check)}")
