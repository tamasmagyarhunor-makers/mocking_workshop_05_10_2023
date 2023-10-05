from lib.string_checker import *

def test_has_punctuation():
    string_checker = StringChecker()

    expected = False
    actual = string_checker.has_punctuation("hello WORLD")

    assert actual == expected