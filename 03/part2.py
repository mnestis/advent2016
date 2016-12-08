#!/usr/bin/python

def count_triangles(input_string):
    
    count = 0

    rows = []
    
    for line in input_string.split("\n"):
        if line.strip() != "":
            a, b, c = filter(lambda a: a != "", line.strip().split(" "))

            a, b, c = int(a), int(b), int(c)
            
            rows.append((a, b, c))

    print rows[-3:]

    triangles = []
    for i in range(0, len(rows), 3):
        triangles.extend(zip(*rows[i:i+3]))

    print triangles[-3:]

    for a, b, c in triangles:
        if a + b <= c:
            pass
        elif a + c <= b:
            pass
        elif b + c <= a:
            pass
        else:
            count += 1

    return count

if __name__=="__main__":

    input_string = open("input.txt", "r").read()

    print count_triangles(input_string)
