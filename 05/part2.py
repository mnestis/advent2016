#!/usr/bin/python

from hashlib import md5

def generate_door_code(door_id):
    
    door_code="________"
    counter = 0

    while("_" in door_code):
        hash = md5(door_id + str(counter)).hexdigest()
        if hash.startswith("00000"):
            if int(hash[5], 16) < 8:
                if door_code[int(hash[5], 16)] == "_":
                    door_code = door_code[:int(hash[5])] + hash[6] + door_code[int(hash[5])+1:]
        counter += 1

    return door_code


if __name__=="__main__":

    print generate_door_code("reyedfim")
