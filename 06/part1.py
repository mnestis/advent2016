#!/usr/bin/python

def recover_message(input_string):

    message = ""

    lines = []

    for line in input_string.split("\n"):
        if line.strip() != "":
            lines.append(line)

    chars = zip(*lines)

    for char_list in chars:
        counts = {}
        for char in char_list:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

        message += sorted(counts.items(), key=lambda a : a[1], reverse=True)[0][0]

    return message

if __name__=="__main__":
    
    input_string = open("input.txt", "r").read()

    print recover_message(input_string)
