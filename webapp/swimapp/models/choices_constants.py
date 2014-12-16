'''Constants for field lookup choices'''
_YARDS = 'Y'
_METERS = 'M'
DISTANCE_UNIT_CHOICES = (
    (_YARDS, 'Yards'),
    (_METERS, 'Meters'),
)

_MALE = 'M'
_FEMALE = 'F'
GENDER_CHOICES = (
    (_MALE, 'Male'),
    (_FEMALE, 'Female'),
)

_SPLIT_RESULT = 'split'
_FINAL_RESULT = 'final'
RESULT_TYPES = (
    (_SPLIT_RESULT, 'Split'),
    (_FINAL_RESULT, 'Final'),
)

EVENT_CODES = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5
}
