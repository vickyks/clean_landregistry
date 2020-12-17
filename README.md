# Orbital Witness Software Engineering Exercise

## Context
The Land Registry's API gives access to digitized "Schedule of notices of leases" documents.

The text in the original document is formatted in a tabular structure, but the texts have been
parsed line by line, with some loss of spaces.  As a result, the entry data comes in out of order.

The table should have the following columns:
* Registration date and Plan ref
* Property description
* Date of lease and term
* Lessee's title

And some entries have one extra row at the bottom of the table, spanning all 4 columns.

## The Task
Take the output of the API and cleanse the data such that it is structured in a format
where column data and optional notes can be independently referenced.

This solution supports the JSON response from the Land Registry's API.


## Approach

After a bit of playing around with some of the data, I figured out a way to get most of the data out.

I took advantage of pytest's parameterization for the tests, as it's easy to the human eye
to identify which fields each part tof the schedule entry it should end up in, so a few
tables of expected output can be manually created.
It also speeds up the feedback loop of development.

Using pytest for tests, and flake8 for quality.

Python 3.7 was chosen simply because that's what was installed on my home machine at the time.

Other than this, the exercise doesn't need much in the way of dependencies, 
so the directory structure is fairly simple.


The output of the cleansed table should contain the following fields

* `registration_date`
* `plan_ref`
* `property_description`
* `date_of_lease`
* `start_of_term`
* `length_of_term`
* `lessees_title`
* `notes`

I chose to use a list of dicts as the structure, as I don't know how the output is intended to be used.
For example, I don't know whether the Lessee's title is known elsewhere, and would therefore be
appropriate as a key. Assuming this is not the case, list of dicts makes it easy parseable.

I could have indexed the data structure in the form
`{entry_number: {k:v for k,v in entry_data.items()}}`
but entry number is not unique. Besides this, I felt like "list of dicts" was more easily parsable en-masse.


For parsing the entryText data. What is definitely known:
* The column lengths are right padded with spaces. It looks like there's more than one space of delimiter.
* Date of lease and term is always at last 3 rows
* Lessees title is always the last "word" of the first row
* Registration date is always the first word of the first row
* notes are prepended with the word NOTE
* notes come at the end
* other than the first row, the final "field" in each row (excluding date) is the Date of lease and term column 

Edge cases:
* the third row can cause problems. If it is only one field, it's a date (from the date of lease and term)
* if it is not the only field, it can either be part of description, or plan ref, and there's no real way to tell
* The structure of the api data isn't strictly consistent in the larger dataset. json_response['leaseschedule']
  isn't necessarily a dict with the 'scheduleentry' key. It's sometimes a list of 'scheduleentry' dicts
* If there are 1 or 2 "words" left within the last few rows , it can be unclear which column the data comes from.
* The lease date/term information usually follows a consistent structure, but just occasionally it contains an end date too



### Questions / improvements?

* Do we want dates in datetime object format?
* Should the "NOTE {X}: " part be removed for cleanliness?
* Term of lease: is it worth removing the "from" 



## Installation

```
python3.7 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Development
To run:
```
python cleanse_lease_data.py response=response_json.json
```


## Tests

* For python tests, run 
```
pytest
```
from the main directory.


