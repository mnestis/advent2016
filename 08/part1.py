#!/usr/bin/python

import numpy
import re

def get_screen(instructions):

    screen = numpy.zeros((50, 6))

    COL_ROTATE = re.compile("rotate column x=(\d+) by (\d+)")
    ROW_ROTATE = re.compile("rotate row y=(\d+) by (\d+)")
    DRAW_RECT = re.compile("rect (\d+)x(\d+)")

    for instruction in instructions:
        match = COL_ROTATE.match(instruction)
        if match is not None:
            col, rows = [int(group) for group in match.groups()]
            rotate_col(screen, col, rows)
        match = ROW_ROTATE.match(instruction)
        if match is not None:
            row, cols = [int(group) for group in match.groups()]
            rotate_row(screen, row, cols)
        match = DRAW_RECT.match(instruction)
        if match is not None:
            width, height = [int(group) for group in match.groups()]
            apply_rect(screen, width, height)

    return screen


def apply_rect(screen, width, height):
    screen[:width, :height] = numpy.ones((width, height))

def rotate_row(screen, row, cols):
    for i in range(cols):
        temp = screen[-1,row]
        screen[1:,row] = screen[:-1,row]
        screen[0,row] = temp

def rotate_col(screen, col, rows):
    for i in range(rows):
        temp = screen[col,-1]
        screen[col,1:] = screen[col,:-1]
        screen[col,0] = temp

def print_screen(screen):
    width, height = screen.shape
    
    for y in range(height):
        row = ""
        for x in range(width):
            if screen[x, y] == 1:
                row += "8"
            else:
                row += " "
        print row

if __name__=="__main__":

    input_string = open("input.txt", "r").read()

    screen = get_screen([instruction.strip() for instruction in input_string.split("\n")])
    print_screen(screen)
