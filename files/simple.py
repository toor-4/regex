#!/usr/bin/python3

import re

with open('files/simple.txt', 'r') as f:
    file = f.read()
    # print(file[:3])
    # pattern = re.compile(r'abc')
    # pattern = re.compile(r'\.')
    # pattern = re.compile(r'\d\d\d.+')
    # pattern = re.compile(r'1234.+')
    # pattern = re.compile(r'\D\D\D')
    # pattern = re.compile(r'\[\{')    
    # pattern = re.compile(r'coreyms\.com')
    # pattern = re.compile(r'\W')
    # pattern = re.compile(r'\BHa')
    # pattern = re.compile(r'\bcha')
    # pattern = re.compile(r'\bcha')
    # pattern = re.compile(r"end.'$")
   
    # pattern = re.compile(r"\d\d\d[-*].+") # matches characters that's inside the bracket
    # pattern = re.compile(r"(8|9).+") # matches characters that's inside the bracket
    # pattern = re.compile(r"[89]00.+") # matches characters that's inside the bracket
    # pattern = re.compile(r'^[abcABC].+')
    # pattern = re.compile(r'^[abcABC]')
    # pattern = re.compile(r'^[a-zA-Z]')
    # pattern = re.compile(r'[^cmp]at')
    # pattern = re.compile(r'[^b]at')
    # pattern = re.compile(r"\d\d\d[.*]\d\d\d[.*]\d\d\d\d")
    # pattern = re.compile(r"\d{3}[.*]\d{3}[.*]\d{4}")
    # pattern = re.compile(r"\d{3}[-].+")
    # pattern = re.compile(r'Mr\.?')
    # pattern = re.compile(r'Mr\.?')   ######### this period here is used literally
    # pattern = re.compile(r'Mr\..+')   ######### this period here is used literally
    

    # pattern = re.compile(r'Mr\.?\s[A-Z].')
    # pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  ######### this period here is used literally
    # pattern = re.compile(r'Mr\.?\s.+') 
    # pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  ######### this period here is used literally
    pattern = re.compile(r'(Mr.)\s[A-Z]\w*')  ######### this period here is used literally
    matches = pattern.finditer(file)
    for match in matches:
        print(match)
