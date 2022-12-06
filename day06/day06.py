# Advent of Code - 2022 - Day 6

import time
import copy

start_time = time.time()

# Initialize
part1_answer = ""
part2_answer = ""

def get_packet_start(transmission, length):
    """
    Returns the start of packet position based on length
    """
    for character in range(len(transmission)):
        if character > length-2:
            if duplicate_character_found(transmission[character-length+1:character+1]):
                return character+1


def duplicate_character_found(string):
    """
    Checks if a duplicate character exists in a string and returns a True/False
    """
    duplicate_characters = []
    for character in string:
        if character in duplicate_characters:
            return False
        else:
            duplicate_characters.append(character)
    return True


# Process file
with open("day06/day06.dat", "r") as fileData:
    for line in fileData:

        transmission = line.strip()

        part1_answer = get_packet_start(transmission, 4)
        part2_answer = get_packet_start(transmission, 14)

# Print Answers
print("Answer (Part 1): " + str(part1_answer))
print("Answer (Part 2): " + str(part2_answer))
print("--- %s seconds ---" % (time.time() - start_time))
