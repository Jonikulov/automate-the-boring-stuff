## PAGE -> 179
# Printing a Table of Contents
"""
tableOfContents = {"Introduction":1, "Part 1: Introducing AI":5, "CHAPTER 1: Introducing AI":5,
"CHAPTER 2: Defining the Role of Data":21, "CHAPTER 3: Considering the Use of Algorithms":39,
"CHAPTER 4: Pioneering Specialized Hardware":155}

def printContents(dictData, leftWidth, rightWidth):
    for k,v in dictData.items():
        if k.lower().startswith("part"):
            print("")
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))

printContents(tableOfContents, 50, 3)
"""
######################################################################
# Adding Bullets to Wiki Markup
"""

'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
"""
######################################################################
# Table Printer
"""
tableData = [['apples', 'oranges', 'cherries', 'banana'], \
             ['Alice', 'Bob', 'Carol', 'David'], \
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(Data):
    # Get the maximum width of each column
    colWidth = [0]*len(Data)
    for i in range(len(Data)):
        colWidth[i] = len(max(Data[i],key = len))
        
    # Print    
    for j in range(len(Data[0])):
        for i in range(len(Data)):
            print(Data[i][j].rjust(colWidth[i]), end = ' ')
        print('\r')

printTable(tableData)
""" 
######################################################################
# Finding phone numbers in a text
"""
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


import re

text = "345-965-3486"

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
"""
######################################################################
# PRACTICE PYTHON > Password Generator > Ex 16
'''
import random

symbols = "!@#$%^&*=;:'~{}[]<>?_/*-+"
up_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_letters = "abcdefghijklmnopqrstuvwxyz"

def StrongPasswordGenerator():
    password = ""
    """16 character long, strong password generator"""
    while True:
        num = str(random.randint(1000, 9999))
        if num[0]==num[1]==num[2] or num[1]==num[2]==num[3]:
            continue
        break
    password += num

    while True:
        symbol = random.choice(symbols)
        up_letter = random.choice(up_letters)
        low_letter = random.choice(low_letters)

        if (symbol not in password) and (up_letter not in password) and (low_letter not in password):
            password += symbol
            password += up_letter
            password += low_letter

        if len(password)==16:
            break
        continue


    index_list = list(range(16))
    pwd = ""
    new_list = []

    while True:
        index = random.choice(index_list)
        if index not in new_list:
            new_list.append(index)
            pwd += password[index]
        if len(new_list)==16:
            break
        continue

    return pwd

print(StrongPasswordGenerator())
'''
######################################################################
# password genereator
"""
import random, string

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
pwd =  "".join(random.sample(s,8))
print(pwd)

# print(string.digits)
# print(string.ascii_letters)
# print(string.punctuation)
"""
######################################################################
# Use the BeautifulSoup and requests Python packages to print out a
# list of all the article titles on the New York Times homepage.
"""
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
"""
######################################################################
"""
# mapIt.py - Launches a map in the browser using an
# address from the command line or clipboard.
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
# wb.open(url)
print(url)
# sample address: 870 Valencia St, San Francisco, CA 94110
"""
######################################################################
# BeautifulSoup > select method
"""
soup.select('div')                  - All elements named <div>
soup.select('#author')              - The element with an id attribute of author
soup.select('.notice')              - All elements that use a CSS class attribute named notice
soup.select('div span')             - All elements named <span> that are within an element named <div>
soup.select('div > span')           - All elements named <span> that are directly within an element
                                      named <div>, with no other element in between
soup.select('input[name]')          - All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]') - All elements named <input> that have an attribute named type with value button
"""
