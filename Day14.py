import re
import numpy as np
from collections import defaultdict
from functools import reduce
from operator import mul


def parse_data(file_name: str) -> list:
    """Parse data from the input file."""
    with open(file_name) as f:
        return [
            tuple(int(num) for num in re.match(r'^p=(\d+),(\d+) v=(-?\d+),(-?\d+)$', line).groups())
            for line in f.readlines()
        ]


def find_safety(data: list, bounds: tuple, steps: int = 100) -> list:
    """Calculate safeties based on robot movements."""
    qs_nums = [[1, 2], [3, 4]]
    safeties = []

    for idx in range(steps):
        new_positions = []
        qs = defaultdict(int)

        for robot in data:
            x, y, dx, dy = robot
            new_x = (x + dx) % bounds[0]
            new_y = (y + dy) % bounds[1]
            new_positions.append((new_x, new_y, dx, dy))

            if (new_x != (bounds[0] // 2)) and (new_y != (bounds[1] // 2)):
                qs[qs_nums[new_x < (bounds[0] // 2)][new_y < (bounds[1] // 2)]] += 1

        safeties.append((reduce(mul, qs.values()), idx + 1))
        data = new_positions

    return safeties


def part1(data: list, bounds: tuple) -> int:
    """Solve part 1."""
    return find_safety(data, bounds)[-1][0]


def part2(data: list, bounds: tuple) -> int:
    """Solve part 2."""
    return min(find_safety(data, bounds, 10000))[1]


def draw_pict(data: list, bounds: tuple, steps: int):
    """Visualize the robots' positions."""
    robots = np.zeros(tuple(reversed(bounds)))

    for robot in data:
        x, y, dx, dy = robot
        robots[((y + dy * steps) % bounds[1], (x + dx * steps) % bounds[0])] += 1

    for line in robots:
        print(''.join(('.' if ch == 0 else str(int(ch))) for ch in line))


if __name__ == "__main__":
    # Parse data from input.txt
    data = parse_data('input.txt')

    # Part 1
    print('Part 1:', part1(data, (101, 103)))

    # Part 2
    p2 = part2(data, (101, 103))
    print('Part 2:', p2)

    # Draw the pictorial representation
    draw_pict(data, (101, 103), p2)
