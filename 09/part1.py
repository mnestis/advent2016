#!/usr/bin/python

import re

def decompress_text(input_text):
    
    to_be_processed = input_text
    output_text = ""

    to_be_processed = re.sub("[\n\r ]", "", to_be_processed)

    while len(to_be_processed) != 0:
        try:
            group_start = to_be_processed.index("(")
        except ValueError:
            output_text += to_be_processed
            break

        output_text += to_be_processed[:group_start]
        to_be_processed = to_be_processed[group_start+1:]

        group_end = to_be_processed.index(")")

        length, multiple = [int(val) for val in to_be_processed[:group_end].split("x")]
        to_be_processed = to_be_processed[group_end+1:]

        repeated_string = to_be_processed[:length]
        to_be_processed = to_be_processed[length:]

        output_text += repeated_string * multiple

    return output_text

if __name__=="__main__":
    
    input_string = open("input.txt", "r").read()

    print len(decompress_text(input_string))
    print "ADVENT", decompress_text("ADVENT")
    print "A(1x5)BC", decompress_text("A(1x5)BC")
    print "(3x3)XYZ", decompress_text("(3x3)XYZ")
    print "A(2x2)BCD(2x2)EFG", decompress_text("A(2x2)BCD(2x2)EFG")
