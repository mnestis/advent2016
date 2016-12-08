#!/usr/bin/python

def calculate_shortest_distance(input_string):
    
    x = 0
    y = 0
    direction = 0

    instructions = input_string.split(", ")

    for instruction in instructions:

        print x, y, "=>", instruction, direction,

        if instruction[:1] == "L":
            direction += 3
        elif instruction[:1] == "R":
            direction += 1
        else:
            raise Exception("Neither left nor right...")

        direction %= 4

        distance = int(instruction[1:])

        print "=>", direction, distance, "blocks",

        if direction == 0:
            y += distance
        elif direction == 1:
            x += distance
        elif direction == 2:
            y -= distance
        elif direction == 3:
            x -= distance
        else:
            raise Exception("Neither N, E, S, nor W...")

        print x, y

    return abs(x) + abs(y)

if __name__=="__main__":

    input_string = open("input.txt", "r").read()

    print calculate_shortest_distance(input_string)
