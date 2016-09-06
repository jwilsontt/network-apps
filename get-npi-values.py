import os.path
import re
import time
import sys
import codecs

# logfeed_file = raw_input(u "Enter filename: ")
logfeed = open("/Users/jasonwilson/Documents/ProgWork/CWC-CVOIP-NPI/Cayman/LOGS.recorddata.20160903_12_00.txt", mode='r')

# for line in logfeed:
#     print (line)

logfeed.seek(0)
lines = logfeed.read()
# print lines
sw_clli = re.search(r"\b(GEO.+?)\b", lines)
clli = sw_clli.group(0)
print clli
#
#
# if clli == "GEORKXOTGBC":
#     print "This is the Cayman C20"
# else:
#     print "Unknown clli, try again!"

# Return to beginning of file
logfeed.seek(0)
#
logfeed_num = logfeed.read()
# print logfeed_num
feednum = re.findall(r"\b(NPI.+?)\b([A-Z].+?)\b(\d{2}[:]?\d{2}[:]?\d{2})", logfeed_num)
feed = feednum
print len(feed)

for i in feed:
    print (re.sub(r"[^\w]", ' ', i[0])), (re.sub(r"[^\w]", ' ', i[1])), (i[2])


logfeed.close()
