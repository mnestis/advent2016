#!/usr/bin/python

import re
BRACKETS = re.compile("[\[\]]")

def count_ssl_supporting_ips(input_ips):
    
    count = 0

    for ip in input_ips:
        if ip_supports_ssl(ip):
            count += 1

    return count

def ip_supports_ssl(input_ip):
    
    abas = filter(lambda x: x != [], [has_aba(component) for component in BRACKETS.split(input_ip)[::2]])

    if abas != []:
        abas = reduce(lambda a, b: a + b, abas)

    hypernets = BRACKETS.split(input_ip)[1::2]

    if abas == []:
        return False
    
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        for hypernet in hypernets:
            if bab in hypernet:
                return True
    else:
        return False


def has_aba(input_string):

    abas = []

    for i in range(len(input_string) - 2):
        if input_string[i:i+3] == input_string[i+2:i-1 if i > 0 else None:-1]: 
            if input_string[i] != input_string[i+1]:
                abas.append(input_string[i:i+3])
    
    return abas

if __name__=="__main__":

    input_string = open("input.txt", "r").read()

    print count_ssl_supporting_ips([strng.strip() for strng in input_string.split("\n")])
