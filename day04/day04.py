# Advent of Code - 2022 - Day 4

import time
start_time = time.time()

# Initialize
part1_answer = 0
part2_answer = 0

def get_range(line_part):
    """
    Returns a list of numbers from start to end, based on the line_parts
    """
    section_range = line_part.split("-")
    return list(range(int(section_range[0]), int(section_range[1])+1, 1))

# Process file
with open("day04/day04.dat", "r") as fileData:
    for line in fileData:

        line_parts = line.strip().split(",")
        elf_1_sections = get_range(line_parts[0])
        elf_2_sections = get_range(line_parts[1])

        # Check to see if either section is fully contained in the other
        if (
            all(section_id in elf_2_sections for section_id in elf_1_sections) or
            all(section_id in elf_1_sections for section_id in elf_2_sections)
        ):
            part1_answer += 1

        # Check to see if either section overlaps with the other
        for section_id in elf_1_sections:
            if section_id in elf_2_sections:
                part2_answer += 1
                break

# Print Answers
print("Answer (Part 1): " + str(part1_answer))
print("Answer (Part 2): " + str(part2_answer))
print("--- %s seconds ---" % (time.time() - start_time))
