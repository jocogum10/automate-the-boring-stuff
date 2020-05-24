#! python3
# finds URLS on the clipboard

#import modules
import pyperclip, re

# create URL regex
dateRegex = re.compile(r'''(
    ([0-3]{1}[1-9]{1})                  # day
    \/                                  # separator
    ([0-1]{1}[1-9]{1})                  # month
    \/                                  # separator
    ([1-2]{1}[0-9]{1}[0-9]{1}[0-9]{1})  # year          
)''', re.VERBOSE)

# find matches in clipboard text  
text = str(pyperclip.paste())

matches = []
day_limit = 0 

for groups in dateRegex.findall(text):
    date = groups[1]
    month = groups[2]
    year = groups[3]

    # determine if leap year
    if (year%4)==0:             # if leap year
        if month == 2:         # set february to 29 days
            day_limit = 29
    else:                       # if not leap year
        if month == 2:         # february to 28 days
            day_limit = 28
    # set the month limit
    if month in [4, 6, 9, 11]:         # April
        day_limit == 30
    else:                   # if not april, june, september, or november
        day_limit == 31

    if date <= day_limit:
        matches.append(groups[0])
    else:
        #invalid date
        pass

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print(matches)
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates were found.')