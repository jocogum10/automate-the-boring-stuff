#! python3
# finds phone numbers and email addresses on the clipboard

#import modules
import pyperclip, re

# create phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension

)''', re.VERBOSE)

#todo: create email regex

# todo: find matches in clipboard text

# todo: copy results to the clipboard