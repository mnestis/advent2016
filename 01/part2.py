#!/usr/bin/python

def calculate_shortest_distance(input_string):
    
    x = 0
    y = 0
    direction = 0

    instructions = input_string.split(", ")

    visited_locations = [(0, 0)]

    for instruction in instructions:

        if instruction[:1] == "L":
            direction += 3
        elif instruction[:1] == "R":
            direction += 1
        else:
            raise Exception("Neither left nor right...")

        direction %= 4

        distance = int(instruction[1:])

        for i in range(distance):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            else:
                raise Exception("Neither N, E, S, nor W...")

            if (x, y) in visited_locations:
                print instruction
                return abs(x) + abs(y)
            else:
                visited_locations.append((x,y))
    else:
        raise Exception("Never visited anywhere twice...")

if __name__=="__main__":

    input_string = open("input.txt", "r").read()

    print calculate_shortest_distance(input_string)
