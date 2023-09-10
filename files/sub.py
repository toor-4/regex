#!/usr/bin/python3

import re

# 1
string = "The quick brown fox jumps over the lazy dog."
pattern = r"\bthe\b"
replacement = "that"

new_string = re.sub(pattern, replacement, string)

print(new_string)
print()
# 2
with open('files/sub.txt', 'r') as f:
    file = f.read()
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    # matches = pattern.finditer(file)
    # for match in matches:
        # print(match)
        # print(match.group(0))
    subt_urls = pattern.sub(r'\2\3', file)     
    # subbed_urls = re.sub(r'https', 'whats up', file)      
print(subt_urls)
