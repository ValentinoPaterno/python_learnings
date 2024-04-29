"""
A regular expression is a special text string that helps to find
patterns in data. A RegEx can be used to check if some pattern
exists in a different data type. First we should import it.
"""
import re 

# re.match() method -> Returns an object or None type
# Searches only in the beginning of the first line of the string
text = 'I love to teach python and javaScript'
match = re.match('I love to teach', text, re.I)
# .span() returns the starting and ending position of the match as tuple
span = match.span()
print(span)
# Finding the start and end position from the span
start, end = span
print(start,end)
substring = text[start:end]
print(substring)
# Should return "I love to teach" substring

# re.search()
text = """Python is the mosth beatufiul language that a human being
has ever created. I recommend python for a first programming 
language """

match = re.search("first", text, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = text[start:end]
print(substring)

# re.findall() -> Better function than .search() and .match()
# it checks for the pattern and returns all the matches as a list
matches = re.findall('language', text, re.I)
print(matches)
matches = re.findall('python', text, re.I)
print(matches)
# because we are using re.I botch lowercase and uppercase letters
# are included. If we do not have the re.I flag, then we'll have 
# to write our pattern differently like this:
matches = re.findall('Python|python', text)
print(matches)  # ['Python', 'python']

# Another way
matches = re.findall('[Pp]ython', text)
print(matches)  # ['Python', 'python']

# Replacing a substring with sub()
match_replaced = re.sub('Python|python', 'JavaScript', text, re.I)
print(match_replaced)
# Another way
match_replaced = re.sub('[Pp]ython', 'JavaScript', text, re.I)
print(match_replaced)

# Splitting text with RegEx split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol

# --- Writing RegEx patterns ---
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctoy way has been replaced by a banana a day keeps the doctor far away'
matches = re.findall(regex_pattern, txt)
print(matches)
# Making it case insensitive adding flag
matches = re.findall(regex_pattern, txt, re.I)
print(matches)


