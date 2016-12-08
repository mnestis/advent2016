#!/usr/bin/python

def determine_code(input_string):
    
    code = ""

    digit = "5"
    for instruction in input_string.split("\n"):
        if instruction.strip() != "":
            digit =  get_next_digit(instruction, digit)
            code += digit

    return code

def get_next_digit(instruction, start_digit):

    index = [(int(start_digit)-1)%3, (int(start_digit)-1)/3]

    for inst in instruction:
        if inst == "D":
            index[1] = index[1] + 1 if index[1] != 2 else 2
        elif inst == "U":
            index[1] = index[1] - 1 if index[1] != 0 else 0
        elif inst == "R":
            index[0] = index[0] + 1 if index[0] != 2 else 2
        elif inst == "L":
            index[0] = index[0] - 1 if index[0] != 0 else 0
        else:
            raise Exception("Unknown direction...")

    return str(1 + index[0] + index[1]*3)


if __name__=="__main__":
    
    input_string = open("input.txt", "r").read()

    print determine_code(input_string)
