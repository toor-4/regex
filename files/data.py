#!/usr/bin/python3

import re

# 1
# with open('data.txt', 'r', encoding='utf-8') as f:
#     file = f.read()
#     # Pattern for telephone number
#     pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
#     # pattern = re.compile(r"[89]00-.+")
#     matches = pattern.finditer(file)
#     for match in matches:
#         print(match.group(0))

# 2
with open('files/data.txt', 'r', encoding='utf-8') as f:
    file = f.read()
    # a. Pattern for address 
    # pattern = re.compile(r"[A-Z].+,\s.+")
    # b. pattern for email address 
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    matches = pattern.finditer(file)
    for match in matches:
        print(match.group(0))

# 3
# with open('data.txt', 'r', encoding='utf-8') as f:
#     file = f.read()
#     # 1.Pattern for person
#     pattern = re.compile(r"[A-Z].+")
#     matches = pattern.finditer(file)
#     for match in matches:
#         if len(match.group(0)) < 20:
#             print(match.group(0))



