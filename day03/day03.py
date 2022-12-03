# Advent of Code - 2022 - Day 3

import time
start_time = time.time()

# Initialize
part1_answer = 0
part2_answer = 0
containers = []
container_number = 0

def get_priority(item):
    """
    Returns the priority of a given item
    """
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96


# Process file
with open("day03/day03.dat", "r") as fileData:
    for line in fileData:
        containers.append(line.strip())

for container in containers:

    # Assign container number
    container_number += 1

    compartment1 = container[:(int(len(container)/2))]
    compartment2 = container[(int(len(container)/2)):]

    # Initialize priority
    priority = None

    # Check for matching item in both compartments
    for item in compartment1:
        if item in compartment2 and priority is None:
            priority = get_priority(item)
            part1_answer += priority

    # Check if final container for group of 3
    if container_number % 3 == 0:

        # Initialize badge
        badge_id = None

        # Check for matching item in last three containers until found
        for item in containers[container_number-1]:
            if item in containers[container_number-2] and badge_id is None:
                if item in containers[container_number-3] and badge_id is None:
                    badge_id = item
                    part2_answer += get_priority(badge_id)

# Print Answers
print("Answer (Part 1): " + str(part1_answer))
print("Answer (Part 2): " + str(part2_answer))
print("--- %s seconds ---" % (time.time() - start_time))
