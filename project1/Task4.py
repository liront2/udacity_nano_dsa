"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def printTelemarketingNumbers(calls, texts):
    telemarketersSet = set()
    noTeleSet = set()

    for call in calls:
        telemarketersSet.add(call[0])
        noTeleSet.add(call[1])

    for text in texts:
        noTeleSet.add(text[0])
        noTeleSet.add(text[1])

    telemarketersSet -= noTeleSet
    sortedNumbers = sorted(telemarketersSet)
    print("These numbers could be telemarketers:")
    for phone in sortedNumbers:
        print(phone)

printTelemarketingNumbers(calls, texts)

