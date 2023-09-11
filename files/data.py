#!/usr/bin/python3

import re

## Using with statement to open and read the data.txt file
with open('../files/data.txt', 'r', encoding='utf-8') as f:
    file = f.read()
    """ pattern for names """
    pattern = re.compile(r"([A-Z][a-z]+ [A-Z][a-z]+)\n")
    # pattern = re.compile(r"[A-Z][a-z]+ [A-Z][a-z]+\n")

    """ pattern for address"""
    # pattern = re.compile(r"[A-Z].+,\s.+")

    """ pattern for email address"""
    # pattern = re.compile(r'[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    # pattern = re.compile(r'[A-Z].+:\s[a-zA-Z].+')
    # pattern = re.compile(r'[A-Z].+:\s[a-zA-Z].+(net|org)')

    """ pattern for phone"""
    # pattern = re.compile(r'[A-Z].+:\s\d{3}-.+')
    
    matches = pattern.finditer(file)
    for match in matches:
        # print(match)
        print(match.group(0).strip())
        # print(match.group(1).strip())
