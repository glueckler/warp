import os
import sys
import re
from decimal import *

directory = os.listdir('.')

# prevent hidden files from being processed
directory = list(filter(lambda x: x.find('.', 0, 1) == -1, directory))

print "Non-hidden Files in directory"
for li in directory:
    print li

print '---------------------------'

for song in directory:
    print song

    checkFile = re.match(r'\d+[AB]\s-\s\d\d.*', song)
    # if song matches the warp regex ie 3A - 87 - .......
    if checkFile:
        info = re.match(
            r'(\d+[AB])(\s-\s)(\d\d+)( - )(\d*\s*)(.*)(\..*\b)', song)

        key = info.group(1)
        key = key.lower()

        bpm = info.group(3)
        bpm = int(bpm)
        # fold bpm if it's over 138bpm
        if (bpm > 138):
            if (bpm % 2 != 0):
                bpm = Decimal(bpm)
            bpm = bpm / 2

        name = info.group(6)

        extension = info.group(7)

        print key
        print bpm
        print name
        print extension

        formatted_name = str(bpm) + ' - ' + key + ' - ' + name + extension
        print formatted_name
        print '-' * 10

        # rename the file
        os.rename(song, formatted_name)

    else:
        print "File Not Needs Processing, moving on.. "


