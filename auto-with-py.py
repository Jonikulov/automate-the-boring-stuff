#### PAGE -> 192
# Finding Patterns of Text Without Regular Expressions

message = "Call me at 415-555-1011 tomorrow. 645-012-9999 is my office."

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    if text[:3].isdecimal() and text[4:7].isdecimal() and text[8:].isdecimal():
        if text[3]=='-' and text[7]=='-':
            return True
    return False

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f"Phone number: {chunk}")


### PAGE 194
# Finding Patterns of Text with Regular Expressions
import re
text = "345-965-3486"

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

######################################################################
# Use the BeautifulSoup and requests Python packages to print out a
# list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://nytimes.com'
r = requests.get(url)

text_html = r.text

soup = BeautifulSoup(text_html, features="html5lib")

# title = soup.find_all('h2')
# print(title)

for title in soup.find_all('span'):
    print(title.get_text())

for story_heading in soup.find_all(class_="css-hdqqnpa"): 
    print(story_heading)

for story_heading in soup.find_all('h1'): 
    print(story_heading)


# filename = 'html_file.html'
# with open(filename,'w') as file:
#     for link in soup.find_all('h3'):
#         file.write(link.get_text())
#         file.write('\n')

######################################################################

# map_it.py - Launches a map in the browser using an
# address from the command line or clipboard.
# sample address: 870 Valencia St, San Francisco, CA 94110

import webbrowser as wb
import sys, pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

string_address = ""
for char in address:
    if char.isalnum() or char.isspace():
        string_address += char

string_address = '+'.join(string_address.split())
url = f"https://google.com/maps/place/{string_address}/"
wb.open(url)
print(url)

######################################################################
# BeautifulSoup > select method
'''
soup.select('div')                  - All elements named <div>
soup.select('#author')              - The element with an id attribute of author
soup.select('.notice')              - All elements that use a CSS class attribute named notice
soup.select('div span')             - All elements named <span> that are within an element named <div>
soup.select('div > span')           - All elements named <span> that are directly within an element
                                      named <div>, with no other element in between
soup.select('input[name]')          - All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]') - All elements named <input> that have an attribute named type with value button
'''