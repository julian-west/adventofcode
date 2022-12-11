"""day 6 solution"""


def get_message_marker(datastream: str, window_size: int) -> int:
    for i in range(len(datastream) - window_size + 1):
        window = datastream[i : i + window_size]
        seq_start_index = i + window_size
        if len(set(window)) == window_size:
            return seq_start_index
    raise ValueError("No sequence without repeated characters")


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        datastream = puzzle_input.read().strip()

    part_1_ans = get_message_marker(datastream, window_size=4)
    print(part_1_ans)

    part_2_ans = get_message_marker(datastream, window_size=14)
    print(part_2_ans)
