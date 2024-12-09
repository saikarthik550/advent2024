"""Day 3 of Advent of Code 2024.

The goal of part 1 is to find the sum of the products of the two integers in
each 'mul' instruction in the input.txt file.

The goal of part 2 is to find the sum of the products of the two integers in
each 'mul' instruction in the input.txt file, but only if the instruction is
preceded by a 'do()' instruction and not a 'don't()' instruction. We can use a
boolean flag to determine if we should multiply the two integers in the 'mul'
instruction.
"""

import re


class AdventDay3:

    def __init__(self):
        """Read in the input.txt file and find all valid instructions.
        The valid instructions are 'mul(a,b)', 'do()', and 'don't()'. We will
        use regular expressions to find these instructions in the input.txt file.
        """
        self.text_input = ''
        with open('input.txt', 'r') as f:
            for line in f.readlines():
                self.text_input += line
        self._find_valid_instructions()
        self.part1 = 0
        self.part2 = 0

    def _find_valid_instructions(self):
        """Find all valid instructions in the input.txt file."""
        self.valid_instructions =\
            re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)",
                       self.text_input)

    def process_all_multiplications(self):
        """Process all 'mul' instructions in the input.txt file."""
        for mult in self.valid_instructions:
            nums = re.findall(r'\d{1,3}', mult)
            try:
                self.part1 += int(nums[0]) * int(nums[1])
            except IndexError:
                pass

    def process_switch_multiplications(self):
        """Process 'mul' instructions in the input.txt file only if the previous
        non 'mul' instruction was 'do()' and not 'don't()'.

        It is assumed that any 'mul' instruction before any 'do()' or 'don't()'
        instruction is valid and should be processed."""
        mult = True
        for instr in self.valid_instructions:
            if instr == 'do()':
                mult = True
            elif instr == 'don\'t()':
                mult = False
            elif mult:
                nums = re.findall(r'\d{1,3}', instr)
                self.part2 += int(nums[0]) * int(nums[1])


if __name__ == '__main__':
    day3 = AdventDay3()
    day3.process_all_multiplications()
    day3.process_switch_multiplications()
    print(day3.part1, day3.part2)