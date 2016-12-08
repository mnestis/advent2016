#!/usr/bin/python

def count_triangles(input_string):
    
    aye_count = 0
    nay_count = 0

    for line in input_string.split("\n"):
        if line.strip() != "":
            a, b, c = filter(lambda a: a != "", line.strip().split(" "))
            
            a, b, c = int(a), int(b), int(c)

            if a + b <= c:
                nay_count += 1
            elif a + c <= b:
                nay_count += 1
            elif b + c <= a:
                nay_count += 1
            else:
                aye_count += 1

    return aye_count

if __name__=="__main__":

    input_string = open("input.txt", "r").read()

    print count_triangles(input_string)
