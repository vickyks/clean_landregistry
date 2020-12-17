'''
Some helper data to feed into the parametrize decorator
'''
json_response_simple = [
    {
        "leaseschedule": {
            "scheduletype": "schedule of notices of lease",
            "scheduleEntry": [
                {
                    "entryNumber": "1",
                    "entryDate": "",
                    "entryType": "Schedule of Notices of Leases",
                    "entryText": [
                        "28.01.2009      Transformer Chamber (Ground   23.01.2009      EGL551039  ",
                        "tinted blue     Floor)                        99 years from              ",
                        "(part of)                                     23.1.2009"
                    ]
                }
            ]
        }
    }
]

expected_table_simple = [
    {
        "entry_number": "1",
        "registration_date": "28.01.2009",
        "plan_ref": "tinted blue (part of)",
        "property_description": "Transformer Chamber (Ground Floor)",
        "date_of_lease": "23.01.2009",
        "lease_term": "99 years from 23.1.2009",
        "lessees_title": "EGL551039",
        "notes": []
    }
]

json_response_with_single_note = [
    {
        "leaseschedule": {
            "scheduletype": "schedule of notices of lease",
            "scheduleEntry": [
                {
                    "entryNumber": "93",
                    "entryDate": "",
                    "entryType": "Schedule of Notices of Leases",
                    "entryText": [
                        "22.02.2010      Flat 2308 Landmark West       03.02.2010      EGL568130  ",
                        "Edged and       Tower (twenty third floor     999 years from             ",
                        "numbered 4 in   flat)                         1.1.2009                   ",
                        "blue (part of)                                                           ",
                        "NOTE: See entry in the Charges Register relating to a Deed of Rectification dated 26 January 2018"
                    ]
                },
            ]
        }
    }
]

expected_table_with_single_note = [
    {
        "entry_number": "93",
        "registration_date": "22.02.2010",
        "plan_ref": "Edged and numbered 4 in blue (part of)",
        "property_description": "Flat 2308 Landmark West Tower (twenty third floor flat)",
        "date_of_lease": "03.02.2010",
        "lease_term": "999 years from 1.1.2009",
        "lessees_title": "EGL568130",
        "notes": ["NOTE: See entry in the Charges Register relating to a Deed of Rectification dated 26 January 2018"]
    }
]

json_response_multiple_notes = [
    {
        "leaseschedule": {
            "scheduleType": "SCHEDULE OF NOTICES OF LEASE",
            "scheduleEntry": [
                {
                    "entryNumber": "1",
                    "entryDate": "",
                    "entryType": "Schedule of Notices of Leases",
                    "entryText": [
                        "28.11.2018      Shoreditch High Street        11.11.2016      AGL461975  ",
                        "Station more particularly     From 02:00 on              ",
                        "described in the lease        13 November                ",
                        "2016 to 01:59              ",
                        "on 15 November             ",
                        "2026                       ",
                        "NOTE 1: The lease comprises also other land.",
                        "NOTE 2: No copy of the Lease referred to is held by HM Land Registry."
                    ]
                }
            ]
        }
    },
]
expected_table_multiple_notes = [
    {
        "entry_number": "1",
        "registration_date": "28.11.2018",
        "plan_ref": "",
        "property_description": "Shoreditch High Street Station more particularly described in the lease",
        "date_of_lease": "11.11.2016",
        "lease_term": "",
        "lessees_title": "AGL461975",
        "notes": [
            "NOTE 1: The lease comprises also other land.",
            "NOTE 2: No copy of the Lease referred to is held by HM Land Registry.",
        ],
    }
]

json_response_many_entries = [
    {
        "leaseschedule": {
            "scheduleType": "SCHEDULE OF NOTICES OF LEASE",
            "scheduleEntry": [
                {
                    "entryNumber": "1",
                    "entryDate": "",
                    "entryType": "Schedule of Notices of Leases",
                    "entryText": [
                        "10.09.1987      89H Denmark Hill (Second      03.08.1987      SGL493290  ",
                        "Edged and       Floor Flat)                   125 years from             ",
                        "numbered 30                                   3.8.1987                   ",
                        "(Part of) in                                                             ",
                        "brown                                                                    ",
                        "NOTE 1: A Deed dated 21 May 1992 made between (1) Orbit Housing Association and (2) Carol Jean Pryce is supplemental to the Lease dated 3 August 1987 of 89H Denmark Hill referred to above. It rectifies the lease plan.",
                        "NOTE 2: Copy Deed filed under SGL493290"
                    ]
                },
                {
                    "entryNumber": "2",
                    "entryDate": "",
                    "entryType": "Schedule of Notices of Leases",
                    "entryText": [
                        "17.11.1987      89E Denmark Hill (First       30.10.1987      SGL501009  ",
                        "edged and       Floor Flat)                   125 years from             ",
                        "numbered in                                   30.10.1987                 ",
                        "brown 13 (part                                                           ",
                        "of)"
                    ]
                },
                {
                    "entryNumber": "3",
                    "entryDate": "",
                    "entryType": "Schedule of Notices of Leases",
                    "entryText": [
                        "17.02.1988      11 Ashworth Close (Second     15.02.1988      SGL507575  ",
                        "Edged and       Floor Flat)                   125 years from             ",
                        "numbered 22                                   1.2.1988                   ",
                        "(Part of) in                                                             ",
                        "brown                                                                    ",
                        "NOTE 1: By a Deed dated 5 May 1995 made between (1) Orbit Housing Association (2) Anna Julie Price and (3) Nationwide Building Society the terms of the Lease were varied.  (Original Deed filed under SGL507575).",
                        "NOTE 2: A Deed dated 20 February 1996 made between (1) Orbit Housing Association (2) Anna Julie Price (3) Nationwide Building Society and (4) Haco Limited is supplemental to the lease. It substitutes a new plan for the original lease plan. (Copy Deed filed under SGL507575)"
                    ]
                }
            ]
        }
    },
]

expected_table_many_entries = [
    {
        "entry_number": "1",
        "registration_date": "10.09.1987",
        "plan_ref": "Edged and numbered 30 (Part of) in brown",
        "property_description": "89H Denmark Hill (Second Floor Flat)",
        "date_of_lease": "03.08.1987",
        "lease_term": "125 years from 3.8.1987",
        "lessees_title": "SGL493290",
        "notes": [
            "NOTE 1: A Deed dated 21 May 1992 made between (1) Orbit Housing Association and (2) Carol Jean Pryce is supplemental to the Lease dated 3 August 1987 of 89H Denmark Hill referred to above. It rectifies the lease plan.",
            "NOTE 2: Copy Deed filed under SGL493290"
        ],
    },
    {
        "entry_number": "2",
        "registration_date": "17.11.1987",
        "plan_ref": "edged and numbered in brown 13 (part of)",
        "property_description": "89E Denmark Hill (First Floor Flat)",
        "date_of_lease": "30.10.1987",
        "lease_term": "125 years from 30.10.1987",
        "lessees_title": "SGL501009",
        "notes": [
        ]
    },
    {
        "entry_number": "3",
        "registration_date": "17.02.1988",
        "plan_ref": "Edged and numbered 22 (Part of) in brown",
        "property_description": "11 Ashworth Close (Second Floor Flat)",
        "date_of_lease": "15.02.1988",
        "lease_term": "125 years from 1.2.1988",
        "lessees_title": "SGL507575",
        "notes": [
            "NOTE 1: By a Deed dated 5 May 1995 made between (1) Orbit Housing Association (2) Anna Julie Price and (3) Nationwide Building Society the terms of the Lease were varied.  (Original Deed filed under SGL507575).",
            "NOTE 2: A Deed dated 20 February 1996 made between (1) Orbit Housing Association (2) Anna Julie Price (3) Nationwide Building Society and (4) Haco Limited is supplemental to the lease. It substitutes a new plan for the original lease plan. (Copy Deed filed under SGL507575)"
        ],
    },
]


# A really good "edge case with ambiguous lines and a very long 3rd column"
json_response_long_date_format = [
{
    "leaseschedule": {
        "scheduleType": "SCHEDULE OF NOTICES OF LEASE",
        "scheduleEntry": [
        {
	"entryNumber": "141",
	"entryDate": "",
	"entryType": "Schedule of Notices of Leases",
	"entryText": [
	    "17.10.2017      47 Sheringham (Third Floor    13.10.2017      NGL973748  ",
	    "Flat)                         From and                   ",
	    "including 13               ",
	    "October 2017               ",
	    "to and                     ",
	    "including 21               ",
	    "November 2174              ",
	    "NOTE: The lease was made under the provisions of section 56 or 93(4) of the Leasehold Reform, Housing and Urban Development Act 1993."
                    ]
                }
            ]
        }
    }
]
