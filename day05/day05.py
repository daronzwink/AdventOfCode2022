# Advent of Code - 2022 - Day 5

import time
import copy

start_time = time.time()

# Initialize
part1_answer = ""
part2_answer = ""
num_stacks = None
stacks = {}
moves = []

def get_top_of_stack(stack, num_stacks):
    """
    Returns a string with the top of the stack
    """
    answer = ""
    for column in range(num_stacks):
        answer += stack[column][0]
    return answer

# Process file
with open("day05/day05.dat", "r") as fileData:
    for line in fileData:

        # Get Stacks
        if "[" in line:

            # Get number of stacks to process
            if not num_stacks:
                num_stacks = int((len(line) + 1)/3)

            # Get starting stack configuration
            for stack in range(num_stacks):
                container = line[(stack*4)+1:(stack*4)+2]

                if stack not in stacks:
                    stacks[stack] = []

                if container.strip() != '':
                    stacks[stack].append(container.strip())

        # Get Moves
        if "move" in line:

            directives = line.split(' ')

            move_num_containers = directives[1]
            from_stack = directives[3]
            to_stack = directives[5]

            moves.append({
                "amount": int(move_num_containers),
                "from" : int(from_stack),
                "to" : int(to_stack),
            })

    # Create copys to process each part of the initial stacks
    stacks_part1 = copy.deepcopy(stacks)
    stacks_part2 = copy.deepcopy(stacks)

    # Execute moves for Part 1
    for move in moves:
        for move_num in range(move["amount"]):
            container = stacks_part1[move["from"]-1].pop(0)
            stacks_part1[move["to"]-1].insert(0, container)

    part1_answer += get_top_of_stack(stacks_part1, num_stacks)

    # Execute moves for Part 2
    for move in moves:
        containers = stacks_part2[move["from"]-1][0:move["amount"]]
        del stacks_part2[move["from"]-1][0:move["amount"]]
        for container in reversed(containers):
            stacks_part2[move["to"]-1].insert(0, container)

    part2_answer += get_top_of_stack(stacks_part2, num_stacks)

# Print Answers
print("Answer (Part 1): " + str(part1_answer))
print("Answer (Part 2): " + str(part2_answer))
print("--- %s seconds ---" % (time.time() - start_time))
