import re

# Sample text containing dates
text1 = "Today's date is 09/04/2023 and tomorrow's date is 09/05/2023."
# Regular Expression pattern with groups
pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

matches = re.findall(pattern, text1)
for match in matches:
    # print(match)
    month, day, year = match
    print(f'Month: {month} Day: {day}, Year: {year}')

print()
print("-----------------------------")
print()

text2 = """
Phone: 555-123-4567
Phone: 555-987-6543
Phone: 555-555-5555
"""

# Define a regular expression pattern with capturing groups
phone_pattern = r"Phone: (\d{3})-(\d{3}-\d{4})"

matches = re.finditer(phone_pattern, text2)

for match in matches:
    # match.group(0) contains the entire matched text
    # match.group(1) contains the first capturing group (area code)
    # match.group(2) contains the second capturing group (phone number)
    print("Full Match:", match.group(0))
    print("Area Code:", match.group(1))
    print("Phone Number:", match.group(2))
    print()  # Adding an empty line for separation  