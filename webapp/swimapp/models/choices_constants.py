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

_HY3_FILE = 'hy3_file'
FILE_UPLOAD_CHOICES = (
    (_HY3_FILE, 'HY3 File'),
)
