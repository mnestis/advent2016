#!/usr/bin/python

import re

def decompress_text(input_text):
    
    to_be_processed = input_text
    output_text_length = 0

    to_be_processed = re.sub("[\n\r ]", "", to_be_processed)

    while len(to_be_processed) != 0:
        try:
            group_start = to_be_processed.index("(")
        except ValueError:
            output_text_length += len(to_be_processed)
            break

        output_text_length += len(to_be_processed[:group_start])
        to_be_processed = to_be_processed[group_start+1:]

        group_end = to_be_processed.index(")")

        length, multiple = [int(val) for val in to_be_processed[:group_end].split("x")]
        to_be_processed = to_be_processed[group_end+1:]

        repeated_string = to_be_processed[:length]
        to_be_processed = to_be_processed[length:]

        output_text_length += decompress_text(repeated_string) * multiple

    return output_text_length

if __name__=="__main__":
    
    input_string = open("input.txt", "r").read()

    print decompress_text(input_string)
