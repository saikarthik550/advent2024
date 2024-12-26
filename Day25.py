from pathlib import Path
from time import time

def parse_input(raw: str) -> int:
    items = keys if raw[0] == "." else locks
    item = []
    lines = raw.split("\n")
    for i in range(len(lines[0])):
        item.append(sum(1 if line[i] == "#" else 0 for line in lines) - 1)
    items.append(item)
    return len(lines) - 2

if __name__ == "__main__":
    t = time()
    with Path(f"input.txt").open("r") as file:
        data = file.read().split("\n\n")
    keys = []
    locks = []
    for raw in data:
        available_space = parse_input(raw.strip())

    # Part 1
    matching = 0
    for key in keys:
        for lock in locks:
            for k, l in zip(key, lock):
                if k + l > available_space:
                    break
            else:
                matching += 1
    print("Part 1 Result:", matching)

    # Part 2
    swaps_needed = []
    for i, key in enumerate(keys):
        for j, lock in enumerate(locks):
            for k, l in zip(key, lock):
                if k + l > available_space:
                    swaps_needed.append((i, j))
                    break
    print("Part 2 Result: Swaps Needed:", swaps_needed)

    print("Execution Time:", time() - t)
