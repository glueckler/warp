import os, sys, re
from decimal import *

directory = os.listdir('.')
directory = list(filter(lambda x: x.find('.', 0, 1) == -1, directory))

for song in directory:
  checkFile = re.match( r'\d+[AB]\s-\s\d\d.*', song)
  
  # if song matches the warp regex
  if checkFile:
    print checkFile.group(0)
    info = re.match( r'(\d+[AB])(\s-\s)(\d\d+)( - )(\d*\s*)(.*)(\..*\b)', song)
    key = info.group(1)
    key = key.lower()
    bpm = info.group(3)
    bpm = int(bpm)
    name = info.group(6)
    extension = info.group(7)
    print key
    print bpm
    print name

    # fold bpm if it's over 138bpm
    if (bpm > 138):
      print "! over 138bpm!!!!"
      if (bpm % 2 != 0):
        bpm = Decimal(bpm)
      bpm = bpm / 2
      print bpm

    print "the formatted name here"
    formatted_name = str(bpm) + ' - ' + key + ' - ' + name + extension
    print formatted_name
    print '-' * 10
  
    #rename the file
    os.rename(song, formatted_name)