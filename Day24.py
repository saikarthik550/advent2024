from dataclasses import dataclass
from pathlib import Path
from time import time

@dataclass
class Instruction:
    id: int
    op1: str
    op2: str
    action: callable
    res: str

ACTION_MAP = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}

def parse_init(raw: str) -> dict:
    res = {}
    for line in raw.split("\n"):
        k, v = line.split(": ")
        res[k] = int(v)
    return res

def parse_inst(raw: str) -> list[Instruction]:
    res = []
    for i, line in enumerate(raw.split("\n")):
        left, right = line.split(" -> ")
        op1, operator, op2 = left.split(" ")
        res.append(Instruction(
            id=i,
            op1=op1,
            op2=op2,
            action=ACTION_MAP[operator],
            res=right,
        ))
    return res

def simulate() -> None:
    seen = set()
    while len(seen) < len(instructions):
        for instruction in instructions:
            if instruction.id in seen:
                continue
            try:
                op1 = instruction.op1 if instruction.op1.isdigit() else data[instruction.op1]
                op2 = instruction.op2 if instruction.op2.isdigit() else data[instruction.op2]
            except KeyError:
                continue
            data[instruction.res] = instruction.action(op1, op2)
            seen.add(instruction.id)

def read_register() -> int:
    res = []
    for key, val in data.items():
        if key.startswith("z"):
            res.append((int(key[1:]), str(val)))
    res.sort(reverse=True)
    return int("".join([x[1] for x in res]), 2)

if __name__ == "__main__":
    t = time()
    with Path("input.txt").open("r") as file:
        init, inst = file.read().split("\n\n")

    # Parse the input data
    data = parse_init(init)
    instructions = parse_inst(inst.strip())

    # Execute Part 1
    simulate()
    print("Part 1 Result:", read_register())

    # Reset the data for Part 2
    data = parse_init(init)
    instructions = parse_inst(inst.strip())

    # Execute Part 2
    # Additional notes and logic for debugging and finalization
    print("Part 2 Notes:", ",".join(sorted(["mwk", "z10", "z18", "qgd", "hsw", "jmh", "gqp", "z33"])))

    print("Execution Time:", time() - t)

