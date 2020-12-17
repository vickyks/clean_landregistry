import pytest

from orbital_witness.cleanse_lease_data import cleanse, parse_entry
from orbital_witness.tests.json_response import (
    expected_table_simple,
    expected_table_many_entries,
    expected_table_multiple_notes,
    expected_table_with_single_note,
    json_response_simple,
    json_response_many_entries,
    json_response_multiple_notes,
    json_response_with_single_note,

)

@pytest.mark.parametrize("test_input,expected_table", [
    (json_response_simple, expected_table_simple),
    (json_response_with_single_note, expected_table_with_single_note),
    (json_response_multiple_notes,expected_table_multiple_notes),
    (json_response_multiple_notes,expected_table_multiple_notes),
    (json_response_many_entries,expected_table_many_entries),
])
def test_cleanse(test_input, expected_table):
    assert cleanse(test_input) == expected_table


