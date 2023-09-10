#!/usr/bin/python3

import re

count =0

with open('files/emails.txt', 'r') as f:
    file = f.read()
    # pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com') 
    # pattern = re.compile(r'[a-zA-Z0-9.]+@[a-zA-Z-]+\.(com|edu|net)')
    # pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com')

    matches = pattern.finditer(file)
    for match in matches:
        print(match.group(0))
