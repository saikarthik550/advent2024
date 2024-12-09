import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

# Set recursion limit for deep recursions
sys.setrecursionlimit(10**6)

# Get the input.txt filename from the command line argument or default to '9.in'
infile = sys.argv[1] if len(sys.argv) >= 2 else '9.in'

# Open and read the input.txt file
with open(infile) as f:
    D = f.read().strip()

def solve(part2):
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0
    for i, c in enumerate(D):
        if i % 2 == 0:  # Process file blocks
            if part2:
                A.append((pos, int(c), file_id))
            for _ in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:  # Process free space blocks
            SPACE.append((pos, int(c)))
            for _ in range(int(c)):
                FINAL.append(None)
                pos += 1

    # Rearrange files in the available spaces
    for (pos, sz, file_id) in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos + i] == file_id, f'{FINAL[pos + i]=}'
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break

    # Calculate checksum by summing up the position * file_id for each block
    ans = 0
    for i, c in enumerate(FINAL):
        if c is not None:
            ans += i * c
    return ans

# Solve for part 1 and part 2
p1 = solve(False)
p2 = solve(True)

# Print and copy the results
pr(p1)
pr(p2)
