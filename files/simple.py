#!/usr/bin/python3

import re

with open('simple.txt', 'r') as f:
    file = f.read()
    # pattern = re.compile(r'abc')
    # pattern = re.compile(r'\.')
    # pattern = re.compile(r'\d\d\d.+')
    # pattern = re.compile(r'\d{3}-\d{3}-\d{3,4}')
    # pattern = re.compile(r'\d{3}[-*.]\d{3}[.*-]\d{3,4}')
    # pattern = re.compile(r'Mr\.?')   
    # pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  
    # pattern = re.compile(r'Mr\.?\s.+') 
    # pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  
    pattern = re.compile(r'(Mr|Ms|Mrs)\.? [A-Z]\w*')  
    matches = pattern.finditer(file)
    for match in matches:
        print(match.group(0))
