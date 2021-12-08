"""Day 8 solutions"""

# store length of digits we already know
LEN_MAP = {2: 1, 3: 7, 4: 4, 7: 8}


def process_line(line: str) -> tuple[list[str], list[str]]:
    """Extract signal and result from raw input string"""
    signal, result = line.split(" | ")
    return signal.split(" "), result.split(" ")


def part_1(input: list[tuple[list[str], list[str]]]) -> int:
    """Find number of times 1,3,4 and 7 appear in signal output result"""
    count = 0
    for _, result in input:
        count += sum(len(x) in LEN_MAP for x in result)
    return count


def decode(input_line: tuple[list[str], list[str]]):

    signal, result = input_line

    # get encoding for values we already know from signal item length
    key = {LEN_MAP[len(item)]: set(item) for item in signal if len(item) in LEN_MAP}

    for pattern in signal + result:
        cur = set(pattern)
        if len(pattern) == 6:
            if len(cur - key[4]) == 2:
                key[9] = cur
            elif len(cur - key[1]) == 4:
                key[0] = cur
            else:
                key[6] = cur
        if len(pattern) == 5:
            if len(cur - key[1]) == 3:
                key[3] = cur
            elif len(cur - key[4]) == 2:
                key[5] = cur
            else:
                key[2] = cur
    return key


def convert_key_to_lookup(key: dict[int, set[str]]) -> dict[str, int]:
    lookup = {}
    for k, v in key.items():
        joined = "".join(sorted(v))
        lookup[joined] = k
    return lookup


def solve_output(output: list[str], lookup: dict[str, int]) -> int:
    number = ""
    for digit in output:
        sorted_digit = "".join(sorted(digit))
        number += str(lookup[sorted_digit])
    return int(number)


def part_2(input: list[tuple[list[str], list[str]]]) -> int:
    solved_outputs = []
    for signal, result in input:
        key = decode((signal, result))
        lookup = convert_key_to_lookup(key)
        solved_output = solve_output(result, lookup)
        solved_outputs.append(solved_output)
    return sum(solved_outputs)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        patterns = input.read().splitlines()
        processed_patterns = [process_line(x) for x in patterns]

    part_1_ans = part_1(processed_patterns)
    print(part_1_ans)

    part_2_ans = part_2(processed_patterns)
    print(part_2_ans)
