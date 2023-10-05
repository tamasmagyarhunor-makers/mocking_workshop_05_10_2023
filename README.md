# Mocking workshop 05 10 2023

# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

```
As a User
So I can write remember my life in the future
I want to be able to write a Journal.
```

```
As a User
So I can make sure my sentences are correct
I want to be able to check for puntuation.
```

```
As a User
So I can make sure my sentences are correct
I want to be able to fix capitalisation.
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

class Journal():
    # Parameter:
    #   name => name Journal belongs to
    # Instance variables:
    #   name => name Journal belongs to
    #   notebook => List to store entries in the Journal
    #   string_checker => String Checker to run our entries through for checks
    #   
    def __init__(self, name, string_checker):
        self.name = name
        self.string_checker = string_checker
        self.notebook = []
    
    def add(self, entry):
        # gets an entry
        # checks for puntuation
        # fixes capitalisation
        # returns nothing or Exception
        punctuation_correct = self.string_checker.has_punctuation
        if punctuation_correct:
            entry = self.string_checker.fix_capitalisation(entry)
            self.notebook.append(
                {
                    "date": "23 10 2023",
                    "entry": entry
                }
            )
        else:
            throw Exception("Please add punctuation!")

class StringChecker():
    def has_punctuation(string):
        # gets a string and returns True or False based on punctuation being present or not
        return string[-1] == '.' or string[-1] == '!' or string[-1] == "?"
    
    def fix_capitalisation(entry):
        # gets a string
        # returns it capitalised.
        return entry[0].capitalize()

    

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string with no punctuation
It returns False
"""
string_checker.has.punctuation("hello WORLD") => False


"""
Given a string with "!"
It returns True
"""
string_checker.has_punctuation("hello WORLD!") => False

"""
Given a string with "."
It returns True
"""
string_checker.has_punctuation("hello WORLD!") => False

"""
Given a string with "?"
It returns True
"""
string_checker.has_punctuation("hello WORLD!") => False

"""
Given a string starting with lowercase
It returns the string with uppercase
"""
string_checker.fix_capitalisation("hello, how are you?") => "Hello, how are you?"

"""
Given I try to add an entry to my Journal with correct capitalisation and correct punctuation
It adds the entry to notebook
"""
journal.add('I feel amazing today!') => returns nothing, side effects: it adds the entry to the notebook List

"""
Given I try to add an entry to my Journal with incorrect capitalisation and correct punctuation
It fixes the capitaliation and it adds the entry to notebook
"""
journal.add('i feel amazing today!') => returns nothing, side effects: 1. capitalises the entry, 2. it adds the entry to the notebook List

"""
Given I try to add an entry to my Journal with correct capitalisation but incorrect punctuation
It throws an error
"""
journal.add("I feel amazing today") => throws an error

"""
Given I try to add an entry to my Journal with incorrect capitalisation and incorrect punctuation
It throws an error
"""
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!

