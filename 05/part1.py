#!/usr/bin/python

from hashlib import md5

def generate_door_code(door_id):
    
    door_code = ""
    counter = 0

    while(len(door_code) < 8):
        hash = md5(door_id + str(counter)).hexdigest()
        if hash.startswith("00000"):
            door_code += hash[5]
        counter += 1

    return door_code


if __name__=="__main__":

    print generate_door_code("reyedfim")
