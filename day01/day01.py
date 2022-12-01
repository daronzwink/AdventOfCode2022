# Advent of Code - 2022 - Day 1

import time
start_time = time.time()

# Initialize
part1_answer = 0
part2_answer = 0
elf_id = 0
elves = {}

# Process file
with open("day01/day01.dat", "r") as fileData:
    for line in fileData:

        # Increment elf_id if blank line and reset total calorie count
        if elf_id == 0 or len(line.strip()) == 0:

            # Increment the elf id
            elf_id += 1
            elves[elf_id] = 0

        else:

            # Update dictionary for current elf with total calorie count
            elves[elf_id] += int(line.strip())

    # Generate sorted list of elf calorie totals, with largest first
    elf_totals = sorted([elves[x] for x in elves], reverse=True)

    # Get Part 1 Answer
    part1_answer = max(elf_totals)

    # Get Part 2 Answer
    part2_answer = sum(elf_totals[:3])

# Print Answers
print("Answer (Part 1): " + str(part1_answer))
print("Answer (Part 2): " + str(part2_answer))
print("--- %s seconds ---" % (time.time() - start_time))
