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


# I decided to use parametrize, as I could pump several examples into
# the same test in a neat way. Good for testing some edge cases
@pytest.mark.parametrize("test_input,expected_table", [
    (json_response_simple, expected_table_simple),
    (json_response_with_single_note, expected_table_with_single_note),
    (json_response_multiple_notes,expected_table_multiple_notes),
    (json_response_many_entries,expected_table_many_entries),
])
def test_cleanse(test_input, expected_table):
    result = cleanse(test_input)[0]

    print(result.keys())

    keys = [
        "entry_number",
        "registration_date",
        "plan_ref",
        "property_description",
        "date_of_lease",
        "lease_term",
        "lessees_title",
        "notes",
    ]

    assert set(keys) == set(result.keys())

    for row in result.values():
        print(row)

    for key in keys:
        assert result[key] == expected_table[0][key], f'{key}'

