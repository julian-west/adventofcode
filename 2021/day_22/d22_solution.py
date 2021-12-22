"""Day 22 Solution"""
import re
from collections import Counter

if __name__ == "__main__":

    with open("input.txt", "r") as puzzle_input:
        cubes = Counter()
        for line in puzzle_input.read().splitlines():
            nsgn = 1 if line.split()[0] == "on" else -1
            nx0, nx1, ny0, ny1, nz0, nz1 = map(int, re.findall(r"-?\d+", line))

            update = Counter()
            for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cubes.items():
                ix0 = max(nx0, ex0)
                ix1 = min(nx1, ex1)
                iy0 = max(ny0, ey0)
                iy1 = min(ny1, ey1)
                iz0 = max(nz0, ez0)
                iz1 = min(nz1, ez1)
                if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
                    update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn
            if nsgn > 0:
                update[(nx0, nx1, ny0, ny1, nz0, nz1)] += nsgn
            cubes.update(update)

        part_1_ans = sum(
            (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
            for (x0, x1, y0, y1, z0, z1), sgn in cubes.items()
            if all(-50 <= i <= 50 for i in [x0, x1, y0, y1, z0, z1])
        )
        print(part_1_ans)

        part_2_ans = sum(
            (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
            for (x0, x1, y0, y1, z0, z1), sgn in cubes.items()
        )
        print(part_2_ans)
