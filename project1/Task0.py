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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def printFirstTextAndLastCall(texts, calls):
    """Prints the first record of texts and the last record of calls"""

    # Grab the first text and last call
    first = texts[0]
    last = calls[len(calls)-1]

    # Print the desired output
    print("First record of texts, %s texts %s at time %s" % (first[0], first[1], first[2]))
    print("Last record of calls, %s calls %s at time %s, lasting %s seconds" % (last[0], last[1], last[2], last[3]))

printFirstTextAndLastCall(texts, calls)
