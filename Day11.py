from collections import defaultdict
import re

# Custom implementation of read_input
def read_input(filename='input.txt', split_lines=True):
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return data.splitlines() if split_lines else data
    except FileNotFoundError:
        raise Exception(f"File '{filename}' not found.")

# Custom implementation of nums
def nums(input_data):
    # Supports both single string or list of lines
    if isinstance(input_data, list):
        input_data = "\n".join(input_data)
    return list(map(int, re.findall(r'-?\d+', input_data)))

# Main program logic
lines = read_input(split_lines=False)
stones = {n: 1 for n in nums(lines)}

def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            lh, rh = s[: len(s) // 2], s[len(s) // 2 :]
            new_stones[int(lh)] += count
            new_stones[int(rh)] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

# Part 1
p1 = stones.copy()
for i in range(25):
    p1 = blink(p1)
print("Part 1:", sum(p1.values()))

# Part 2
p2 = stones.copy()
for i in range(75):
    p2 = blink(p2)
print("Part 2:", sum(p2.values()))
