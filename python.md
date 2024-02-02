# Python nuances

At the time of this writing, interviews are conducted with the language chosen
by the interviewee.  

It is not essential to know the deepest functions of the language but knowing
so give the interviewee an edge in the interview.  

For example, when asked to sort an array, the interviewee should NOT use the
`.sort()` built-in function.  Interviewee should implement their own naive
function to show their knowledge of sorting.  

Interviewee should know the nuances of the language of their choosing such as
knowing how a `Set()` type behaves compared to a `list()`.  

## PEP 8

Official Python style guide.

## PEP 484

Python typing guide.  

The `typing` library was introduced in
[Python3.5](https://docs.python.org/3.5/whatsnew/3.5.html).  

## Features by release version

Summary of most notable features but not a complete collection.  
See <https://docs.python.org/3/whatsnew/index.html> for complete feature release
by version.  

Python 3.7

Python 3.6

Python 3.5

- PEP 484 `typing` library
- f-string formatting (`f"""{myvar}"""` vs `"{}".format()`)
- PEP 471 `os.scandir()`, better than conventional `os.walk()`

Python 3.2

- PEP 405 `venv` virtual environments to keep dependencies local
- PEP 389 `argparse` library for reading in command line args

## Data types explained in Python

Sets

Dictionaries.

The Dictionary is Python's version of a hashmap which contains a key and value.  

Python 3.7 and later: Dictionaries are ordered.  
Python 3.6 and earlier: Dictionaries are unordered.  
"""
d = dict()
d = {"mykey": "some value"}

print(d)
print(f"dict length: ", len(d))
