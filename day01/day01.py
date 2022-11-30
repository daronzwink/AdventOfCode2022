# Advent of Code - 2022 - Day 1

import time
start_time = time.time()

# Initialize
depths = []
part1_answer = 0
part2_answer = 0

# Process file
with open("day01/day01.dat", "r") as fileData:
    for depth in fileData:

        # Add depth to list of depts
        depths.append(int(depth))

        # Check to see if current depth has increased from previous depth (Part 1)
        if len(depths) > 1 and depths[-2] < depths[-1]:
            part1_answer += 1

        # Check to see if sum of last three depths has increased from the sum of the
        # previous three depths (Part 2)
        if len(depths) > 3:
            depths_last_set = sum([depths[-1], depths[-2], depths[-3]])
            depths_previous_set = sum([depths[-2], depths[-3], depths[-4]])
            if depths_last_set > depths_previous_set:
                part2_answer += 1

# Print Answers
print("Answer (Part 1): " + str(part1_answer))
print("Answer (Part 2): " + str(part2_answer))
print("--- %s seconds ---" % (time.time() - start_time))
