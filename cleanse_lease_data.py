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

    # Assuming last word of line is a whopping assumption
    # Check against line length, limit is 73 for rows excluding notes
    # remove these from the table and re-append later
    plan_ref_widow, property_description_widow = [],[]
    for i, row in enumerate(entry['entryText']):
        if (len(row) == 73):
            # data appears to retain its length most of the time if
            # the plan ref starts the line
            if (len(entry_table[i]) == 1) or (len(entry_table[i]) == 2):
                plan_ref_widow.append(entry_table[i].pop(0))
                continue

        if (len(entry_table[i]) == 2) & (len(row) < 73):
            if row.endswith('  '):
                # one of the "lossy cases"
                property_description_widow.append(entry_table[i].pop(0))
            else:
                plan_ref_widow.append(entry_table[i].pop(0))


    # Get the last "word" of each line, this is the lease information
    lease_date_information = [line.pop().strip() for line in entry_table if line]
    entry_data['date_of_lease'] = lease_date_information.pop(0)
    entry_data['lease_term'] = ' '.join(lease_date_information)

    # transpose rows - easier for descriptions
    entry_table = [list(row) for row in itertools.zip_longest(*entry_table, fillvalue='')]
    entry_data['registration_date'] = entry_table[0].pop(0)

    # These two are the most likely to give incorrect data, as it's very hard to determine which is which
    # use regex to prevent stray whitespaces in the join
    entry_data['plan_ref'] = re.sub(' +', ' ', ' '.join(entry_table[0] + plan_ref_widow))

    entry_data["property_description"] = re.sub(' +', ' ',' '.join(entry_table[1] + property_description_widow))


    # last bit of data cleansing
    entry_data.update({k: v.strip() for k,v in entry_data.items() if isinstance(v, str)})
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

