#!/usr/bin/python

import re

SECTOR_RE = re.compile("[^\d]+(\d+)\[")
CHECKSUM_RE = re.compile("([A-Za-z\-]+)\d+\[([A-Za-z]{1,5})\]")
ROOM_RE = re.compile("([A-Za-z\-]+)\d")

def get_valid_rooms_with_sector(input_string):
    
    sum = 0

    valid_rooms = []

    for line in input_string.split("\n"):
        if line != "":
            if valid_checksum_p(line):
                valid_rooms.append((get_encrypted_room_name(line), get_sector_id(line)))

    return valid_rooms

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

def get_encrypted_room_name(room_id_string):
    return ROOM_RE.match(room_id_string).groups()[0]

def get_sector_id(room_id_string):
    return int(SECTOR_RE.match(room_id_string).groups()[0])

def decrypt_room_name(encrypted_name, sector_id):

    plaintext_name = ""

    for char in encrypted_name:
        plaintext_name += chr((((ord(char) - ord("a")) + sector_id) % 26) + ord("a")) if char != "-" else " "

    return plaintext_name


if __name__=="__main__":
    
    input_string = open("input.txt", "r").read()

    for room, sector in get_valid_rooms_with_sector(input_string):
        if decrypt_room_name(room, sector).startswith("north"):
            print sector
