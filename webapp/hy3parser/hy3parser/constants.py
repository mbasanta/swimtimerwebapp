"""
constants.py
"""

class LINE_TYPE_CONSTANTS(object):
    """Constants used for line type objects"""

    MEET_TYPE = {
        "08": "",
        "AG": "",
        "US": "",
        "SR": "",
        "YM": ""
        }

    COURSE_CODE = {
        "L": "LONG_COURSE",
        "S": "SHORT_COURSE",
        "Y": "YARDS"
        }

    LINE_TYPE = {
        "MEET_INFO": "B1",
        "MEET_INFO_CONT": "B2",
        "TEAM_INFO_1": "C1",
        "TEAM_INFO_2": "C2",
        "TEAM_INFO_3": "C3",
        "SWIMMER_INFO_1": "D1",
        "SWIMMER_INFO_2": "D2",
        "SWIMMER_INFO_3": "D3",
        "SWIMMER_INFO_4": "D4",
        "SWIMMER_INFO_5": "D5",
        "INDIVIDUAL_ENTRY": "E1",
        "INDIVIDUAL_RESULTS": "E2",
        "RELAY_ENTRY": "F1",
        "RELAY_RESULTS": "F2"
        }

    TEAM_TYPE = {
        "AGE": "Age Group",
        "HS": "High School",
        "COL": "College",
        "MAS": "Masters",
        "OTH": "Other",
        "REC": "Recreation"
        }

    TEAM_REGISTRATION = {
        "AUST": "Austrailia",
        "BCSS": "Canada (BCSSA)",
        "NZSF": "New Zealand",
        "OTH": "Other",
        "SSA": "South Africa",
        "UK": "United Kingdom",
        "USS": "USA Swimming"
        }
