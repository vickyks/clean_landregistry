import itertools
import argparse
import re
import json

def parse_line(line):
    # list comprehension is more pythonic, but filter is faster
    return list(filter(len, line.strip().split('  ')))



def parse_entry(entry):
    '''
    Take the whole entry - it also contains the entry number

    '''
    entry_data = {}
    entry_data['entry_number'] = entry["entryNumber"]

    entry_table = [parse_line(line) for line in entry['entryText']]

    # Lessees title is always the last "word" of the first row
    # Pop this to make lists transposable
    entry_data['lessees_title'] = entry_table[0].pop()

    # Match any rows starting with NOTE, an optional character, and :
    entry_data['notes'] = [line.pop() for line in entry_table if re.search("NOTE.*?:", line[0])]

    for i, key in enumerate(['date_of_lease','length_of_term','start_of_term']):
        # Now the lessees title is out of the table, the last of each row is the lease term information
        entry_data[key] = entry_table[i].pop().strip()

    # transpose rows - easier for descriptions
    entry_table = [list(row) for row in itertools.zip_longest(*entry_table, fillvalue='')]
    entry_data['registration_date'] = entry_table[0].pop(0).strip()
    entry_data['plan_ref'] = ' '.join(entry_table[0]).strip()
    entry_data["property_description"] = ''.join(entry_table[1]).strip()

    return entry_data


def cleanse(json_response):
    '''
    cleanse data from api response
    '''
    parsed_schedule_entries = [
        parse_entry(entry)
        for lease_schedule in json_response
        for entry in lease_schedule['leaseschedule']['scheduleEntry']
    ]
    return parsed_schedule_entries


if __name__ == '__main__':
    '''
    read in the sample file, output the cleansed data
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('response')
    args = parser.parse_args()

    with open(args.response, 'r') as infile, open('cleansed_data.json', 'w') as outfile:
        json_response = infile.read()
        final_data = cleanse(json_response)
        json.dump(final_data, outfile)

