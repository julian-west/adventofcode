"""Day 20 Solution"""
import numpy as np
from scipy.ndimage import convolve

BIN_2_DEC = 2 ** np.arange(9).reshape(3, 3)


def process_algo(algo_input: str) -> np.ndarray:
    return np.array([int(p == "#") for p in algo_input])


def process_image(image_input: list[str]) -> np.ndarray:
    return np.pad([[int(p == "#") for p in row] for row in image_input], (51, 51))


def enhance(algo: np.ndarray, image: np.ndarray) -> np.ndarray:
    return algo[convolve(image, BIN_2_DEC)]


def solve(algo: np.ndarray, image: np.ndarray, steps: int) -> int:
    for _ in range(steps):
        image = enhance(algo, image)
    return image.sum()


if __name__ == "__main__":
    with open("input.txt", "r") as puzzle_input:
        algo_input, _, *image_input = puzzle_input.read().splitlines()

    algo = process_algo(algo_input)
    image = process_image(image_input)

    part_1_ans = solve(algo, image, steps=2)
    print(part_1_ans)

    part_2_ans = solve(algo, image, steps=50)
    print(part_2_ans)
