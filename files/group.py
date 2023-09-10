import re

# Sample text containing dates
text = "Today's date is 09/04/2023 and tomorrow's date is 09/05/2023."
# Regular Expression pattern with groups
pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

matches = re.findall(pattern, text)
for match in matches:
    month, day, year = match
    print(f'Month: {month} Day: {day}, Year: {year}')
