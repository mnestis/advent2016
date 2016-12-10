#!/usr/bin/python

import re
BRACKETS = re.compile("[\[\]]")

def count_tls_supporting_ips(input_ips):
    
    count = 0

    for ip in input_ips:
        if ip_supports_tls(ip):
            count += 1

    return count

def ip_supports_tls(input_ip):
    
    non_hypernet = any([has_abba(component) for component in BRACKETS.split(input_ip)[::2]])
    hypernet = any([has_abba(component) for component in BRACKETS.split(input_ip)[1::2]])

    return not hypernet and non_hypernet

def has_abba(input_string):

    for i in range(len(input_string) - 3):
        if input_string[i:i+4] == input_string[i+3:i-1 if i > 0 else None:-1]: 
            if input_string[i] != input_string[i+1]:
                return True
    else:
        return False

if __name__=="__main__":

    input_string = open("input.txt", "r").read()

    print count_tls_supporting_ips([strng.strip() for strng in input_string.split("\n")])
