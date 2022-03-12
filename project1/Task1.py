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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

def printUniqueNumbersCombined(texts, calls):
    """Prints the different telephone numbers in the records"""

    # prepare a Set of unique phone numbers
    phoneNumbersSet = set()

    """iterate the lists and if a number, add it to the set"""
    for i in range(len(texts)):
        phoneNumbersSet.add(texts[i][0])
        phoneNumbersSet.add(texts[i][1])

    for i in range(len(calls)):
        phoneNumbersSet.add(calls[i][0])
        phoneNumbersSet.add(calls[i][1])

    # Print the desired output
    print("There are %s different telephone numbers in the records." % len(phoneNumbersSet))

printUniqueNumbersCombined(texts, calls)
