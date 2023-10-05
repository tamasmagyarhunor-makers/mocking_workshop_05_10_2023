from lib.journal import *
from lib.string_checker import *
from unittest.mock import Mock, MagicMock, patch
import pytest

def test_journal_instantiates_with_name_string_checker_and_list():
    journal_owner = "Jordan"
    string_checker_mock = Mock()
    journal = Journal(journal_owner, string_checker_mock)

    expected_name = "Jordan"
    expected_string_checker = string_checker_mock
    expected_notebook = []

    actual_name = journal.name
    actual_string_checker = journal.string_checker
    actual_notebook = journal.notebook

    assert expected_name == actual_name
    assert expected_string_checker == actual_string_checker
    assert expected_notebook == actual_notebook


def test_journal_entry_does_not_have_punctuation():
    journal_owner = "Jordan"
    string_checker_mock = Mock()
    journal = Journal(journal_owner, string_checker_mock)

    string_checker_mock.has_punctuation.return_value = False

    with pytest.raises(Exception) as e:
        journal.add("I feel amazing")
    
    expected = "Please add punctuation!"
    actual = str(e.value)

    assert actual == expected




