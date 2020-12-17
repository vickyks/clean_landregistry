import argparse
import re
import json


def parse_entry(entry):
    '''
    Take the whole entry - it also contains the entry number
    '''
    entry_data = {}
    entry_data['entry_number'] = entry["entryNumber"]

    entry_text = entry["entryText"]
    # Match any rows starting with NOTE, an optional character, and :
    r = re.compile("NOTE.*?:")
    entry_data['notes'] = filter(r.match, entry_text)

    # Is it worth popping off the notes, to make parsing the rest easier?
    entry_text = list(set(entry_text) - set(entry_data['notes']))

    # registration date is always the first word of the first row
    entry_data['registration_date'] = entry_text[0].split('  ')[0]

    # Lessees title is always the last "word" of the first row
    entry_data['lessees_title'] = entry_text[0].strip().split('  ')[-1]



    entry_data["date_of_lease"] = entry_text[0]
    entry_data["start_of_term"] = entry_text[0]
    entry_data["length_of_term"] = entry_text[0]

    entry_data["plan_ref"] = entry_text[0]
    entry_data["property_description"] = entry_text[0]

    entry_text = '\n'.join(entry_text)

    return entry_data


def cleanse(json_response):
    '''
    cleanse data from api response
    '''
    parsed_schedule_entries = [
        parse_entry(entry)
        for lease_schedule in json_response
        for entry in lease_schedule['leaseschedule']['scheduleentry']
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

