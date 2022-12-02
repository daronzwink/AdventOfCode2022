# Advent of Code - 2022 - Day 2

import time
start_time = time.time()

# Initialize
part1_answer = 0
part2_answer = 0

def get_result(elf_move, my_move):
    """
    Returns the result of a paper rock scissors game
    """

    if elf_move == my_move:
        # Tie Game
        return 3
    elif elf_move == 1:
        if my_move == 3:
            return 0
        else:
            return 6
    elif elf_move == 2:
        if my_move == 1:
            return 0
        else:
            return 6
    elif elf_move == 3:
        if my_move == 2:
            return 0
        else:
            return 6


def get_required_play(elf_move, desired_result):
    """
    Returns the play needed to get the desired result
    """

    if desired_result == "X":
        # Need to lose
        if elf_move == 1:
            return 3
        elif elf_move == 2:
            return 1
        elif elf_move == 3:
            return 2
    elif desired_result == "Y":
        # Need to tie
        return elf_move
    elif desired_result == "Z":
        # Need to win
        if elf_move == 1:
            return 2
        elif elf_move == 2:
            return 3
        elif elf_move == 3:
            return 1


# Process file
with open("day02/day02.dat", "r") as fileData:
    for line in fileData:

        # Split the line into parts
        parts = line.strip().split(" ")

        # Establish play values for both the elf and myself
        plays = {
            1: ["A", "X"], # Rock
            2: ["B", "Y"], # Paper
            3: ["C", "Z"], # Scissors
        }

        # Lookup play values
        for type, moves in plays.items():
            if parts[0] in moves:
                elf_move = type
            if parts[1] in moves:
                my_move = type

        # Calculate Part 1 answer
        part1_answer += (my_move + get_result(elf_move, my_move))

        # Calculate Part 2 answer
        move_needed = get_required_play(elf_move, parts[1])
        part2_answer += (move_needed + get_result(elf_move, move_needed))

# Print Answers
print("Answer (Part 1): " + str(part1_answer))
print("Answer (Part 2): " + str(part2_answer))
print("--- %s seconds ---" % (time.time() - start_time))
