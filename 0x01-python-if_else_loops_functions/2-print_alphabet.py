#!/usr/bin/python3
#2-print_alphabet.py

"""print the alphabet in lowercase, not followed by a new line."""
output = ''
for i in range(ord('a'), ord('z')+1):
    output += chr(i)

print("{}{}".format(output, ''), end='')
