"""Classes for parsing individual lines in HY3 file"""

import re
# pylint: disable=W0403
import line_format_errors
from decimal import Decimal


class E1Line(object):
    """E1 Line from HY3 file"""
    # pylint: disable-msg=R0902
    def __init__(self, hy3_line=None):
        """Default constructor for empty instance"""
        self.__gender = None
        self.__team_swimmer_id = None
        self.__last_name = None
        self.__gender1 = None
        self.__gender2 = None
        self.__distance = None
        self.__stroke = None
        self.__lower_age = None
        self.__upper_age = None
        self.__fee = None
        self.__event_number = None
        self.__conv_seed_time_1 = None
        self.__conv_seed_course_1 = None
        self.__seed_time_1 = None
        self.__seed_course_1 = None
        self.__conv_seed_time_2 = None
        self.__conv_seed_course_2 = None
        self.__seed_time_2 = None
        self.__seed_course_2 = None

        if (hy3_line is not None):
            self.__init_hy3_line(hy3_line)

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if (len(hy3_line) == 130 and hy3_line[0:2] == "E1"):
            self._parse_gender(hy3_line[2])
            self._parse_team_swimmer_id(hy3_line[3:8])
            self._parse_last_name(hy3_line[8:13])
            self._parse_gender1(hy3_line[13])
            self._parse_gender2(hy3_line[14])
            self._parse_distance(hy3_line[17:21])
            self._parse_stroke(hy3_line[21])
            self._parse_lower_age(hy3_line[22:25])
            self._parse_upper_age(hy3_line[25:28])
            self._parse_fee(hy3_line[32:38])
            self._parse_event_number(hy3_line[38:42])
            self._parse_conv_seed_time_1(hy3_line[42:50])
            self._parse_conv_seed_course_1(hy3_line[50])
            self._parse_seed_time_1(hy3_line[51:59])
            self._parse_seed_course_1(hy3_line[59])
            self._parse_conv_seed_time_2(hy3_line[60:68])
            self._parse_conv_seed_course_2(hy3_line[68])
            self._parse_seed_time_2(hy3_line[69:77])
            self._parse_seed_course_2(hy3_line[77])
        else:
            raise line_format_errors.InputLineError()

    def _parse_gender(self, raw_gender):
        """Parse gender from a one character string"""
        if (re.match("[MF]", raw_gender.upper())):
            self.__gender = raw_gender.upper()
        else:
            raise line_format_errors.FieldParseError("gender")

    def _parse_team_swimmer_id(self, raw_team_swimmer_id):
        """Parse team swimmer id from the five character string"""
        raw_team_swimmer_id = raw_team_swimmer_id.strip()

        try:
            if len(raw_team_swimmer_id) == 0:
                self.__team_swimmer_id = None
            else:
                self.__team_swimmer_id = int(raw_team_swimmer_id, 10)
        except Exception:
            raise line_format_errors.FieldParseError("team_swimmer_id")

    def _parse_last_name(self, raw_last_name):
        """Parse first part of last name from 5 character string"""
        self.__last_name = raw_last_name.strip()

    def _parse_gender1(self, raw_gender1):
        """Parse event gender 1 from a one character string"""
        raw_gender1 = raw_gender1.strip()

        try:
            if len(raw_gender1) == 0:
                self.__gender1 = None
            elif (re.match("[MF]", raw_gender1.upper())):
                self.__gender1 = raw_gender1.upper()
            else:
                raise line_format_errors.FieldParseError("gender1")
        except Exception:
            raise line_format_errors.FieldParseError("gender1")

    def _parse_gender2(self, raw_gender2):
        """Parse event gender 2 from a one character string"""
        raw_gender2 = raw_gender2.strip()

        try:
            if len(raw_gender2) == 0:
                self.__gender2 = None
            elif (re.match("[MF]", raw_gender2.upper())):
                self.__gender2 = raw_gender2.upper()
            else:
                raise line_format_errors.FieldParseError("gender2")
        except Exception:
            raise line_format_errors.FieldParseError("gender2")

    def _parse_distance(self, raw_distance):
        """Parse distance from four character string"""
        raw_distance = raw_distance.strip()

        try:
            if len(raw_distance) == 0:
                self.__distance = None
            else:
                self.__distance = int(raw_distance, 10)
        except Exception:
            raise line_format_errors.FieldParseError("distance")

    def _parse_stroke(self, raw_stroke):
        """Parse stroke from two character string"""
        raw_stroke = raw_stroke.strip()

        try:
            if len(raw_stroke) == 0:
                self.__stroke = None
            elif (re.match("[ABCDE]", raw_stroke.upper())):
                self.__stroke = raw_stroke.upper()
            else:
                raise line_format_errors.FieldParseError("stroke")
        except Exception:
            raise line_format_errors.FieldParseError("stroke")

    def _parse_upper_age(self, raw_upper_age):
        """Parse upper age from two character string"""
        raw_upper_age = raw_upper_age.strip()

        try:
            if len(raw_upper_age) == 0:
                self.__upper_age = None
            else:
                self.__upper_age = int(raw_upper_age, 10)
        except Exception:
            raise line_format_errors.FieldParseError("upper_age")

    def _parse_lower_age(self, raw_lower_age):
        """Parse upper age from two character string"""
        raw_lower_age = raw_lower_age.strip()

        try:
            if len(raw_lower_age) == 0:
                self.__lower_age = None
            else:
                self.__lower_age = int(raw_lower_age, 10)
        except Exception:
            raise line_format_errors.FieldParseError("lower_age")

    def _parse_fee(self, raw_fee):
        """Parse fee from six character string"""
        raw_fee = raw_fee.strip()

        try:
            if len(raw_fee) == 0:
                self.__fee = None
            else:
                self.__fee = Decimal(raw_fee)
        except Exception:
            raise line_format_errors.FieldParseError("fee")

    def _parse_event_number(self, raw_event_number):
        """Parse event number from three character string"""
        raw_event_number = raw_event_number.strip()

        try:
            if len(raw_event_number) == 0:
                self.__event_number = None
            else:
                self.__event_number = int(raw_event_number, 10)
        except Exception:
            raise line_format_errors.FieldParseError("event_number")

    def _parse_conv_seed_time_1(self, raw_time):
        """Parse converstion seed time 1 from eight character string"""
        raw_time = raw_time.strip()

        try:
            if len(raw_time) == 0:
                self.__conv_seed_time_1 = None
            else:
                self.__conv_seed_time_1 = float(raw_time)
        except Exception:
            raise line_format_errors.FieldParseError("conv_seed_time_1")

    def _parse_conv_seed_course_1(self, raw_course):
        """Parse conversion seed course 1 from one character string"""
        raw_course = raw_course.strip()

        try:
            if len(raw_course) == 0:
                self.__conv_seed_course_1 = None
            elif (re.match("[LSY]", raw_course.upper())):
                self.__conv_seed_course_1 = raw_course.upper()
            else:
                raise line_format_errors.FieldParseError("conv_seed_course_1")
        except Exception:
            raise line_format_errors.FieldParseError("conv_seed_course_1")

    def _parse_seed_time_1(self, raw_time):
        """Parse seed time 1 from eight character string"""
        raw_time = raw_time.strip()

        try:
            if len(raw_time) == 0:
                self.__seed_time_1 = None
            else:
                self.__seed_time_1 = float(raw_time)
        except Exception:
            raise line_format_errors.FieldParseError("seed_time_1")

    def _parse_seed_course_1(self, raw_course):
        """Parse seed course 1 from one character string"""
        raw_course = raw_course.strip()

        try:
            if len(raw_course) == 0:
                self.__seed_course_1 = None
            elif (re.match("[LSY]", raw_course.upper())):
                self.__seed_course_1 = raw_course.upper()
            else:
                raise line_format_errors.FieldParseError("seed_course_1")
        except Exception:
            raise line_format_errors.FieldParseError("seed_course_1")

    def _parse_conv_seed_time_2(self, raw_time):
        """Parse converstion seed time 2 from eight character string"""
        raw_time = raw_time.strip()

        try:
            if len(raw_time) == 0:
                self.__conv_seed_time_2 = None
            else:
                self.__conv_seed_time_2 = float(raw_time)
        except Exception:
            raise line_format_errors.FieldParseError("conv_seed_time_2")

    def _parse_conv_seed_course_2(self, raw_course):
        """Parse conversion seed course 2 from one character string"""
        raw_course = raw_course.strip()

        try:
            if len(raw_course) == 0:
                self.__conv_seed_course_2 = None
            elif (re.match("[LSY]", raw_course.upper())):
                self.__conv_seed_course_2 = raw_course.upper()
            else:
                raise line_format_errors.FieldParseError("conv_seed_course_2")
        except Exception:
            raise line_format_errors.FieldParseError("conv_seed_course_2")

    def _parse_seed_time_2(self, raw_time):
        """Parse seed time 2 from eight character string"""
        raw_time = raw_time.strip()

        try:
            if len(raw_time) == 0:
                self.__seed_time_2 = None
            else:
                self.__seed_time_2 = float(raw_time)
        except Exception:
            raise line_format_errors.FieldParseError("seed_time_2")

    def _parse_seed_course_2(self, raw_course):
        """Parse seed course 2 from one character string"""
        raw_course = raw_course.strip()

        try:
            if len(raw_course) == 0:
                self.__seed_course_2 = None
            elif (re.match("[LSY]", raw_course.upper())):
                self.__seed_course_2 = raw_course.upper()
            else:
                raise line_format_errors.FieldParseError("seed_course_2")
        except Exception:
            raise line_format_errors.FieldParseError("seed_course_2")

    @property
    def gender(self):
        """Gender of swimmer"""
        return self.__gender

    @gender.setter
    def gender(self, gender):
        """Gender of swimmer"""
        self.__gender = gender

    @property
    def team_swimmer_id(self):
        """Swimmer Id from team database"""
        return self.__team_swimmer_id

    @team_swimmer_id.setter
    def team_swimmer_id(self, team_swimmer_id):
        """Swimmer Id from team database"""
        self.__team_swimmer_id = team_swimmer_id

    @property
    def last_name(self):
        """First five letters of swimmer last name"""
        return self.__last_name

    @last_name.setter
    def date_of_birth(self, last_name):
        """First five letters of swimmer last name"""
        self.__last_name = last_name

    @property
    def gender1(self):
        """Gender 1 of event"""
        return self.__gender1

    @gender1.setter
    def gender1(self, gender1):
        """Gender 1 of event"""
        self.__gender1 = gender1

    @property
    def gender2(self):
        """Gender 2 of event"""
        return self.__gender2

    @gender2.setter
    def gender2(self, gender2):
        """Gender 2 of event"""
        self.__gender2 = gender2

    @property
    def distance(self):
        """Event distance"""
        return self.__distance

    @distance.setter
    def distance(self, distance):
        """Event distance"""
        self.__distance = distance

    @property
    def stroke(self):
        """Event stroke"""
        return self.__stroke

    @stroke.setter
    def stroke(self, stroke):
        """Event stroke"""
        self.__stroke = stroke

    @property
    def lower_age(self):
        """Event lower age"""
        return self.__lower_age

    @lower_age.setter
    def lower_age(self, lower_age):
        """Event lower age"""
        self.__lower_age = lower_age

    @property
    def upper_age(self):
        """Event upper age"""
        return self.__upper_age

    @upper_age.setter
    def upper_age(self, upper_age):
        """Event upper age"""
        self.__upper_age = upper_age

    @property
    def fee(self):
        """Event fee"""
        return self.__fee

    @fee.setter
    def fee(self, fee):
        """Event fee"""
        self.__fee = fee

    @property
    def event_number(self):
        """Event number"""
        return self.__event_number

    @event_number.setter
    def event_number(self, event_number):
        """Event number"""
        self.__event_number = event_number

    @property
    def conv_seed_time_1(self):
        """Conversion seed time 1"""
        return self.__conv_seed_time_1

    @conv_seed_time_1.setter
    def conv_seed_time_1(self, conv_seed_time_1):
        """Conversion seed time 1"""
        self.__conv_seed_time_1 = conv_seed_time_1

    @property
    def conv_seed_course_1(self):
        """Conversion seed course 1"""
        return self.__conv_seed_course_1

    @conv_seed_course_1.setter
    def conv_seed_course_1(self, conv_seed_course_1):
        """Conversion seed course 1"""
        self.__conv_seed_course_1 = conv_seed_course_1

    @property
    def seed_time_1(self):
        """Seed time 1"""
        return self.__seed_time_1

    @seed_time_1.setter
    def seed_time_1(self, seed_time_1):
        """Seed time 1"""
        self.__seed_time_1 = seed_time_1

    @property
    def seed_course_1(self):
        """Seed course 1"""
        return self.__seed_course_1

    @seed_course_1.setter
    def seed_course_1(self, seed_course_1):
        """Seed course 1"""
        self.__seed_course_1 = seed_course_1

    @property
    def conv_seed_time_2(self):
        """Conversion seed time 2"""
        return self.__conv_seed_time_2

    @conv_seed_time_2.setter
    def conv_seed_time_2(self, conv_seed_time_2):
        """Conversion seed time 2"""
        self.__conv_seed_time_2 = conv_seed_time_2

    @property
    def conv_seed_course_2(self):
        """Conversion seed course 2"""
        return self.__conv_seed_course_2

    @conv_seed_course_2.setter
    def conv_seed_course_2(self, conv_seed_course_2):
        """Conversion seed course 2"""
        self.__conv_seed_course_2 = conv_seed_course_2

    @property
    def seed_time_2(self):
        """Seed time 2"""
        return self.__seed_time_2

    @seed_time_2.setter
    def seed_time_2(self, seed_time_2):
        """Seed time 2"""
        self.__seed_time_2 = seed_time_2

    @property
    def seed_course_2(self):
        """Seed course 2"""
        return self.__seed_course_2

    @seed_course_2.setter
    def seed_course_2(self, seed_course_2):
        """Seed course 2"""
        self.__seed_course_2 = seed_course_2
