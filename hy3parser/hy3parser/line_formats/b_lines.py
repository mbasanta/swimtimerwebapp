"""Classes for parsing individual lines in HY3 file"""

import re
# pylint: disable=W0403
import line_format_errors
from datetime import datetime
from .. import constants


class B1Line(object):
    """B1 Line from HY3 file"""
    # pylint: disable-msg=R0902
    def __init__(self, hy3_line=None):
        """Default constructor for empty instance"""
        self.__meet_name = None
        self.__facility = None
        self.__start_date = None
        self.__end_date = None
        self.__age_up_date = None
        self.__elevation = None

        if (hy3_line is not None):
            self.__init_hy3_line(hy3_line)

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if (len(hy3_line) == 130 and hy3_line[0:2] == "B1"):
            self._parse_meet_name(hy3_line[2:47])
            self._parse_facility(hy3_line[47:92])
            self._parse_start_date(hy3_line[92:100])
            self._parse_end_date(hy3_line[100:108])
            self._parse_age_up_date(hy3_line[108:116])
            self._parse_elevation(hy3_line[116:121])
        else:
            raise line_format_errors.InputLineError()

    def _parse_meet_name(self, raw_meet_name):
        """Parse meet name from 45 character string"""
        self.__meet_name = raw_meet_name.strip()

    def _parse_facility(self, raw_facility):
        """Parse facility name from 45 character string"""
        self.__facility = raw_facility.strip()

    def _parse_start_date(self, raw_start_date):
        """Parse start date to date from eight character string"""
        try:
            raw_start_date = raw_start_date.strip()

            date_pattern = re.compile(r"^[01][0-9][0-3][0-9][12][0-9]{3}$")
            if (len(raw_start_date) == 0):
                self.__start_date = None
            elif (date_pattern.match(raw_start_date)):
                self.__start_date = datetime.strptime(raw_start_date,
                                                      "%m%d%Y").date()
            else:
                raise line_format_errors.FieldParseError("start_date")
        except Exception:
            raise line_format_errors.FieldParseError("start_date")

    def _parse_end_date(self, raw_end_date):
        """Parse end date to date from eight character string"""
        try:
            raw_end_date = raw_end_date.strip()

            date_pattern = re.compile(r"^[01][0-9][0-3][0-9][12][0-9]{3}$")
            if (len(raw_end_date) == 0):
                self.__end_date = None
            elif (date_pattern.match(raw_end_date)):
                self.__end_date = datetime.strptime(raw_end_date,
                                                    "%m%d%Y").date()
            else:
                raise line_format_errors.FieldParseError("end_date")
        except Exception:
            raise line_format_errors.FieldParseError("end_date")

    def _parse_age_up_date(self, raw_age_up_date):
        """Parse end date to date from eight character string"""
        try:
            raw_age_up_date = raw_age_up_date.strip()

            date_pattern = re.compile(r"^[01][0-9][0-3][0-9][12][0-9]{3}$")
            if (len(raw_age_up_date) == 0):
                self.__age_up_date = None
            elif (date_pattern.match(raw_age_up_date)):
                self.__age_up_date = datetime.strptime(raw_age_up_date,
                                                       "%m%d%Y").date()
            else:
                raise line_format_errors.FieldParseError("age_up_date")
        except Exception:
            raise line_format_errors.FieldParseError("age_up_date")

    def _parse_elevation(self, raw_elevation):
        """Parse event number from three character string"""
        raw_elevation = raw_elevation.strip()

        try:
            if len(raw_elevation) == 0:
                self.__elevation = None
            else:
                self.__elevation = int(raw_elevation, 10)
        except Exception:
            raise line_format_errors.FieldParseError("elevation")

    @property
    def meet_name(self):
        """Event meet name"""
        return self.__meet_name

    @meet_name.setter
    def meet_name(self, meet_name):
        """Event meet name"""
        self.__meet_name = meet_name

    @property
    def facility(self):
        """Facility Name"""
        return self.__facility

    @facility.setter
    def facility(self, facility):
        """Facility Name"""
        self.__facility = facility

    @property
    def start_date(self):
        """Event start date"""
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        """Event start date"""
        self.__start_date = start_date

    @property
    def end_date(self):
        """Event end date"""
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        """Event end date"""
        self.__end_date = end_date

    @property
    def age_up_date(self):
        """Swimmer age up date"""
        return self.__age_up_date

    @age_up_date.setter
    def age_up_date(self, age_up_date):
        """Swimmer age up date"""
        self.__age_up_date = age_up_date

    @property
    def elevation(self):
        """Event elevation"""
        return self.__elevation

    @elevation.setter
    def elevation(self, elevation):
        """Event elevation"""
        self.__elevation = elevation


class B2Line(object):
    """B2 Line from HY3 file"""
    # pylint: disable-msg=R0902
    def __init__(self, hy3_line=None):
        """Default constructor for empty instance"""
        self.__meet_type_1 = None
        self.__meet_type_2 = None
        self.__course_code_1 = None
        self.__course_code_2 = None

        if (hy3_line is not None):
            self.__init_hy3_line(hy3_line)

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if (len(hy3_line) == 130 and hy3_line[0:2] == "B2"):
            self._parse_meet_type_1(hy3_line[94:96])
            self._parse_meet_type_2(hy3_line[96:98])
            self._parse_course_code_1(hy3_line[98])
            self._parse_course_code_2(hy3_line[106])
        else:
            raise line_format_errors.InputLineError()

    def _parse_meet_type_1(self, raw_meet_type_1):
        """Parse meet type 1 from 2 character string"""
        try:
            raw_meet_type_1 = raw_meet_type_1.strip().upper()

            if (len(raw_meet_type_1) == 0):
                self.__meet_type_1 = None
            elif (re.match("06", raw_meet_type_1)):
                self.__meet_type_1 = raw_meet_type_1
            else:
                raise line_format_errors.FieldParseError("meet_type_1")
        except Exception:
            raise line_format_errors.FieldParseError("meet_type_1")

    def _parse_meet_type_2(self, raw_meet_type_2):
        """Parse meet type 2 from 2 character string"""
        try:
            raw_meet_type_2 = raw_meet_type_2.strip().upper()

            if (len(raw_meet_type_2) == 0):
                self.__meet_type_2 = None
            elif (raw_meet_type_2 in constants.LINE_TYPE_CONSTANTS.MEET_TYPE):
                self.__meet_type_2 = raw_meet_type_2
            else:
                raise line_format_errors.FieldParseError("meet_type_2")
        except Exception:
            raise line_format_errors.FieldParseError("meet_type_2")

    def _parse_course_code_1(self, raw_course_code_1):
        """Parse course code 1 from 1 character string"""
        try:
            raw_course_code_1 = raw_course_code_1.strip().upper()

            if (len(raw_course_code_1) == 0):
                self.__course_code_1 = None
            elif (raw_course_code_1 in
                    constants.LINE_TYPE_CONSTANTS.COURSE_CODE):
                self.__course_code_1 = raw_course_code_1
            else:
                raise line_format_errors.FieldParseError("course_code_1")
        except Exception:
            raise line_format_errors.FieldParseError("course_code_1")

    def _parse_course_code_2(self, raw_course_code_2):
        """Parse course code 2 from 1 character string"""
        try:
            raw_course_code_2 = raw_course_code_2.strip().upper()

            if (len(raw_course_code_2) == 0):
                self.__course_code_2 = None
            elif (raw_course_code_2 in
                    constants.LINE_TYPE_CONSTANTS.COURSE_CODE):
                self.__course_code_2 = raw_course_code_2
            else:
                raise line_format_errors.FieldParseError("course_code_2")
        except Exception:
            raise line_format_errors.FieldParseError("course_code_2")

    @property
    def meet_type_1(self):
        """Event meet type 1"""
        return self.__meet_type_1

    @meet_type_1.setter
    def meet_type_1(self, meet_type_1):
        """Event meet type 1"""
        self.__meet_type_1 = meet_type_1

    @property
    def meet_type_2(self):
        """Event meet type 2"""
        return self.__meet_type_2

    @meet_type_2.setter
    def meet_type_2(self, meet_type_2):
        """Event meet type 2"""
        self.__meet_type_2 = meet_type_2

    @property
    def course_code_1(self):
        """Event course code 1"""
        return self.__course_code_1

    @course_code_1.setter
    def course_code_1(self, course_code_1):
        """Event course code 1"""
        self.__course_code_1 = course_code_1

    @property
    def course_code_2(self):
        """Event course code 2"""
        return self.__course_code_2

    @course_code_2.setter
    def course_code_2(self, course_code_2):
        """Event course code 2"""
        self.__course_code_2 = course_code_2
