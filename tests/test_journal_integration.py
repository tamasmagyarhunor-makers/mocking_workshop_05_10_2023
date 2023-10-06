from lib.journal import *
from lib.string_checker import *
import pytest

def test_journal_entry_does_not_have_punctuation():
    journal_owner = "Jordan"
    string_checker_mock = StringChecker()
    journal = Journal(journal_owner, string_checker_mock)

    with pytest.raises(Exception) as e:
        journal.add("I feel amazing")
    
    expected = "Please add punctuation!"
    actual = str(e.value)

    assert actual == expected