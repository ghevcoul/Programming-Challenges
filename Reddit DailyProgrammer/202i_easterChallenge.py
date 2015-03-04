# Written for Python 3.4
# 
# /r/dailyprogrammer Challenge #202 Intermediate - Easter Challenge
# https://www.reddit.com/r/dailyprogrammer/comments/2wbvuu/20150218_challenge_202_intermediate_easter/

import datetime
from ephem import next_full_moon
from veryprettytable import VeryPrettyTable

# Easter falls on the first Sunday after the full moon on or
# after the vernal equinox (defined by the Church as March 21)

tab = VeryPrettyTable()
tab.field_names = ["Year", "Full Moon", "Easter Sunday"]
for i in range(2015, 2026):
    fullMoon = next_full_moon(datetime.date(i, 3, 21)).datetime()
    fmDate = datetime.date(fullMoon.year, fullMoon.month, fullMoon.day)
    if fmDate.weekday() < 6:
        easter = fmDate + datetime.timedelta(days=(6-fmDate.weekday()))
    else:
        easter = fmDate + datetime.timedelta(days=7)
    tab.add_row([i, fmDate.strftime("%b %d"), easter.strftime("%b %d")])
print(tab)
