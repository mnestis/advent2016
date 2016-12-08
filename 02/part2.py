#!/usr/bin/python

KEYPAD = {
    (0,2) : "5",
    (1,1) : "A",
    (1,2) : "6",
    (1,3) : "2",
    (2,0) : "D",
    (2,1) : "B",
    (2,2) : "7",
    (2,3) : "3",
    (2,4) : "1",
    (3,1) : "C",
    (3,2) : "8",
    (3,3) : "4",
    (4,2) : "9"
}


def determine_code(input_string):
    
    code = ""

    digit = "5"
    for instruction in input_string.split("\n"):
        if instruction.strip() != "":
            digit =  get_next_digit(instruction, digit)
            code += digit

    return code

def get_next_digit(instruction, start_digit):

    for index in KEYPAD:
        if KEYPAD[index] == start_digit:
            x, y = index

    for inst in instruction:

        next_x, next_y = x, y
        
        if inst == "U":
            next_y += 1
        elif inst == "D":
            next_y -= 1
        elif inst == "R":
            next_x += 1
        elif inst == "L":
            next_x -= 1
        else:
            raise Exception("Unrecognised instruction: %s" % (inst,))

        if (next_x, next_y) in KEYPAD:
            x, y = next_x, next_y    

    return KEYPAD[(x, y)]

if __name__=="__main__":
    
    input_string = open("input.txt", "r").read()

    print determine_code(input_string)
