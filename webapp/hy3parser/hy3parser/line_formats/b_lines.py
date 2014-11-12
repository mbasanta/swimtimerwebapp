"""Classes for parsing individual lines in HY3 file"""

import re
# pylint: disable=W0403
import line_format_errors
from datetime import datetime
from hy3parser.hy3parser import constants
from hy3parser.hy3parser.utilities import append_check_sum
from swimapp.models.meet import Meet


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

        if type(hy3_line) is Meet:
            self.__init_meet(hy3_line)
        elif hy3_line is not None:
            self.__init_hy3_line(hy3_line)

    def __init_meet(self, meet):
        '''Pseudo-constructor for creating an object from a meet'''
        self.__meet_name = meet.meet_name
        self.__facility = meet.facility.facility_name
        self.__start_date = meet.start_date
        self.__end_date = meet.end_date
        self.__age_up_date = meet.age_up_date
        self.__elevation = meet.facility.elevation

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if len(hy3_line) == 130 and hy3_line[0:2] == "B1":
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
            if len(raw_start_date) == 0:
                self.__start_date = None
            elif date_pattern.match(raw_start_date):
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
            if len(raw_end_date) == 0:
                self.__end_date = None
            elif date_pattern.match(raw_end_date):
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
            if len(raw_age_up_date) == 0:
                self.__age_up_date = None
            elif date_pattern.match(raw_age_up_date):
                self.__age_up_date = datetime.strptime(raw_age_up_date,
                                                       "%m%d%Y").date()
            else:
                raise line_format_errors.FieldParseError("age_up_date")
        except Exception:
            raise line_format_errors.FieldParseError("age_up_date")

    def _parse_elevation(self, raw_elevation):
        """Parse event number from five character string"""
        raw_elevation = raw_elevation.strip()

        try:
            if len(raw_elevation) == 0:
                self.__elevation = None
            else:
                self.__elevation = int(raw_elevation, 10)
        except Exception:
            raise line_format_errors.FieldParseError("elevation")

    @property
    def hy3_line(self):
        '''return the b1 line for this object'''
        line = 'B1'
        line += self.meet_name.ljust(45)
        line += self.facility.ljust(45)
        line += self.start_date.strftime('%m%d%Y')
        line += self.end_date.strftime('%m%d%Y')
        line += self.age_up_date.strftime('%m%d%Y')
        line += unicode('' if self.elevation is None else self.elevation) \
            .ljust(5)
        line += (' ' * 7)
        return append_check_sum(line)

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
        self.__meet_masters = None
        self.__meet_type = None
        self.__course_code_1 = None
        self.__course_code_2 = None

        if type(hy3_line) is Meet:
            self.__init_meet(hy3_line)
        elif hy3_line is not None:
            self.__init_hy3_line(hy3_line)

    def __init_meet(self, meet):
        '''Pseudo-constructor for creating an object from a meet'''
        self.__meet_masters = '06' if meet.meet_masters else ''
        if meet.meet_type:
            self.__meet_type = meet.meet_type.type_abbr
        if meet.course_code_1:
            self.__course_code_1 = meet.course_code_1.type_abbr
        if meet.course_code_2:
            self.__course_code_2 = meet.course_code_2.type_abbr

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if len(hy3_line) == 130 and hy3_line[0:2] == "B2":
            self._parse_meet_masters(hy3_line[94:96])
            self._parse_meet_type(hy3_line[96:98])
            self._parse_course_code_1(hy3_line[98])
            self._parse_course_code_2(hy3_line[106])
        else:
            raise line_format_errors.InputLineError()

    def _parse_meet_masters(self, raw_meet_masters):
        """Parse meet type 1 from 2 character string"""
        try:
            raw_meet_masters = raw_meet_masters.strip().upper()

            if len(raw_meet_masters) == 0:
                self.__meet_masters = False
            elif re.match("06", raw_meet_masters):
                self.__meet_masters = True
            else:
                raise line_format_errors.FieldParseError("meet_masters")
        except Exception:
            raise line_format_errors.FieldParseError("meet_masters")

    def _parse_meet_type(self, raw_meet_type):
        """Parse meet type from 2 character string"""
        try:
            raw_meet_type = raw_meet_type.strip().upper()

            if len(raw_meet_type) == 0:
                self.__meet_type = None
            elif raw_meet_type in constants.LINE_TYPE_CONSTANTS.MEET_TYPE:
                self.__meet_type = raw_meet_type
            else:
                raise line_format_errors.FieldParseError("meet_type")
        except Exception:
            raise line_format_errors.FieldParseError("meet_type")

    def _parse_course_code_1(self, raw_course_code_1):
        """Parse course code 1 from 1 character string"""
        try:
            raw_course_code_1 = raw_course_code_1.strip().upper()

            if len(raw_course_code_1) == 0:
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

            if len(raw_course_code_2) == 0:
                self.__course_code_2 = None
            elif (raw_course_code_2 in
                  constants.LINE_TYPE_CONSTANTS.COURSE_CODE):
                self.__course_code_2 = raw_course_code_2
            else:
                raise line_format_errors.FieldParseError("course_code_2")
        except Exception:
            raise line_format_errors.FieldParseError("course_code_2")

    @property
    def hy3_line(self):
        '''return the b1 line for this object'''
        line = u'B2'
        line += (' ' * 92)
        line += '06' if self.meet_masters else '  '

        if self.meet_type:
            line += self.meet_type.rjust(2)
        else:
            line += (' ' * 2)

        if self.course_code_1:
            line += self.course_code_1
        else:
            line += ' '

        line += (' ' * 7)

        if self.course_code_2:
            line += self.course_code_2
        else:
            line += ' '

        line += (' ' * 21)

        return append_check_sum(line)

    @property
    def meet_masters(self):
        """Event meet type 1"""
        return self.__meet_masters

    @meet_masters.setter
    def meet_masters(self, meet_masters):
        """Event meet masters"""
        self.__meet_masters = meet_masters

    @property
    def meet_type(self):
        """Event meet type"""
        return self.__meet_type

    @meet_type.setter
    def meet_type(self, meet_type):
        """Event meet type 2"""
        self.__meet_type = meet_type

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
