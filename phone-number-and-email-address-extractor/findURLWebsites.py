#! python3
# finds URLS on the clipboard

#import modules
import pyperclip, re

# create URL regex
urlRegex = re.compile(r'''(
    (http://|https://)  # http or https protocol
    ([^\s]){1,}         # everything that follows before a white space
)''', re.VERBOSE)

# find matches in clipboard text  
text = str(pyperclip.paste())

matches = []

for groups in urlRegex.findall(text):
    matches.append(groups[0])

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No website URLs were found.')