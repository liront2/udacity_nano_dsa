"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import math


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def isFromBangalore(number):
    return number.startswith('(080)')

# 3A

def getCalleePrefix(number):
    if number.startswith('(0') == True:
        prefix = number.split(")")
        return prefix[0] + ")"
    if number.startswith("140") == True:
       return "140"
    if number.startswith(("7","8","9"))  == True and number.find(' ') != -1:
        return number[:4]

def printUniqueCodes(calls):
    uniqueCodesSet = set()

    for call in calls:
        if isFromBangalore(call[0]):
            uniqueCodesSet.add(getCalleePrefix(call[1]))
    sortedCodes = sorted(uniqueCodesSet)
    print("The numbers called by people in Bangalore have codes:")
    for code in sortedCodes:
        print(code)

printUniqueCodes(calls)

# 3B
def printBangaloreCallsPercentage(calls):
    fromBangaloreCounter = 0
    toBangaloreCounter = 0

    for call in calls:
        if isFromBangalore(call[0]):
            fromBangaloreCounter += 1
            if isFromBangalore(call[1]):
                toBangaloreCounter += 1
    rawBangaloreCallsPercentage = (toBangaloreCounter / fromBangaloreCounter) * 100

    print(str(round(rawBangaloreCallsPercentage, 2)) +
    "% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

printBangaloreCallsPercentage(calls)

