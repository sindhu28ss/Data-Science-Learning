# In computing, a regular expression, also referred to as “regex” or “regexp”, provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters. 
# A regular expression is written in a formal language 
# that can be interpreted by a regular expression processor.
# Really clever “wild card” expressions for matching and parsing strings.


# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

import os
os. getcwd()
#setwd("/Users/sindhujaarivukkarasu/Desktop/R files")

#setwd("/Users/sindhujaarivukkarasu/Documents/BAN 601 Tech Fund/class python programs)
os.chdir(r'/Users/sindhujaarivukkarasu/Documents/BAN 601 Tech Fund/class python programs') 
# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip() # rstrip() method removes any trailing characters (characters at the end a string)
    if re.search('From:', line):
        print(line)

# Search for lines that start with 'From'
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)


# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# Search for lines that start with From and have an at sign
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)

# Search sub-strings that match the regular expression
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# Search for lines that have an at sign between characters
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
# The results will be slightly more accurate than the prvious one for email addresses
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9\-.]\S+@[a-zA-Z0-9].\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# Search for lines that start 'X' followed by any non whitespace
# characters and ':' then output the first group of non whitespace
# characters that follows
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: (\S+)', line)
    if not x: continue
    print(x)

# Search for lines that start with 'X' followed by any non whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

# Search for lines that start with 'X' followed by any non whitespace characters and ':' 
# followed by a space and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)

# Search for lines that contain 'Author:' followed by any characters,
# an at sign, and any non whitespace character
# Then print the character group that follows the at sign
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('Author:.*@(\S+)', line)
    if not x: continue
    print(x)

# Search for lines that contain 'New Revision: ' followed by a number
# Then turn the number into a float and append it to nums
# Finally print the length and the average of nums
hand = open('mbox-short.txt')
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) == 1:
        val = float(x[0])
        nums.append(val)
print(len(nums))
print(sum(nums)/len(nums))



