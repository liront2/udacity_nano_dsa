"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
def findHighestDurationNumber(phoneDict):
    phoneNumber = ''
    max = 0

    for phone in phoneDict:
        if (phoneDict[phone] > max):
            phoneNumber = phone
            max = phoneDict[phone]

    return (phoneNumber, max)

def printLongestTimePhoneNumber(calls):
    phoneDict = {}

    for call in calls:
        phoneDict[call[0]] = phoneDict.get(call[0], 0) + int(call[3])
        phoneDict[call[1]] = phoneDict.get(call[1], 0) + int(call[3])

    (phone, max) = findHighestDurationNumber(phoneDict)
    print(phone + " spent the longest time, " + str(max) + " seconds, on the phone during\nSeptember 2016.")


printLongestTimePhoneNumber(calls)
