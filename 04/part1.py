#!/usr/bin/python

import re

SECTOR_RE = re.compile("[^\d]+(\d+)\[")
CHECKSUM_RE = re.compile("([A-Za-z\-]+)\d+\[([A-Za-z]{1,5})\]")

def get_sum_of_real_room_sectors(input_string):
    
    sum = 0

    for line in input_string.split("\n"):
        if line != "":
            if valid_checksum_p(line):
                sum += get_sector_id(line)

    return sum

def valid_checksum_p(room_id_string):
    room_name, checksum = CHECKSUM_RE.match(room_id_string).groups()

    room_name = room_name.replace("-", "")

    characters = {}

    for char in room_name:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    expected_checksum = "".join(zip(*sorted(characters.items(), cmp=cmp_char_count, reverse=True))[0][:5])

    return checksum == expected_checksum

def cmp_char_count(a, b):
    return a[1] - b[1] if a[1] - b[1] != 0 else ord(b[0]) - ord(a[0])

def get_sector_id(room_id_string):
    return int(SECTOR_RE.match(room_id_string).groups()[0])

if __name__=="__main__":
    
    input_string = open("input.txt", "r").read()

    print get_sum_of_real_room_sectors(input_string)
