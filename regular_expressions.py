import re

# using * asterisk multiple occurrences of the character preceding it
print
print re.findall("ab*c", "ac")  # ['ac']
print re.findall("ab*c", "abcd")  # ['abc']
print re.findall("ab*c", "acc")  # ['ac']
print re.findall("ab*c", "abcac")  # ['abc','ac']
print re.findall("ab*c", "abdc")  # []
print re.findall("ab*c", "ABC")  # [] case sensitive

'''
Our regular expression, ab*c, matches any part of the string that begins with an
-a-, ends with a -c-, and has zero or more of -b- in between the two. This function
returns a list of all matches.
'''
print

# using . period any single occurrence
print re.findall("a.c", "abc")  # ['abc']
print re.findall("a.c", "abbc")  # []
print re.findall("a.c", "ac")  # []
print re.findall("a.c", "acc")  # ['acc']


print

# combining . with *
print re.findall("a.*c", "abc")  # ['abc']
print re.findall("a.*c", "abbc")  # ['abbc']
print re.findall("a.*c", "ac")  # ['ac']

print

results = re.search("ab*c", "ABC", re.IGNORECASE)
print results.group()

print

# the sub() function - allows us to replace text in a string that matches a regular exp
a_string = "Everything we do is <replaced> if it is indeed inside <tags>."
a_string = re.sub("<.*>", "coming up roses", a_string)
print a_string


print

another_string = "Everything we do is <replaced> if it is indeed inside <tags>."
another_string = re.sub("<.*?>", "coming up roses", another_string)
print another_string

