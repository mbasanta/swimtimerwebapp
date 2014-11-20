"""Classes for parsing individual lines in HY3 file"""

import re
# pylint: disable=W0403
import line_format_errors
from datetime import datetime
from hy3parser.hy3parser.utilities import append_check_sum
from swimapp.models.athlete import Athlete


class D1Line(object):
    """D1 Line from HY3 file"""
    # pylint: disable-msg=R0902
    def __init__(self, hy3_line=None):
        """Default constructor for empty instance"""
        self.__gender = None
        self.__event_swimmer_id = None
        self.__last_name = None
        self.__first_name = None
        self.__nick_name = None
        self.__middle_initial = None
        self.__uss_num = None
        self.__team_swimmer_id = None
        self.__date_of_birth = None
        self.__age = None

        if type(hy3_line) is Athlete:
            self.__init_athlete(hy3_line)
        elif hy3_line is not None:
            self.__init_hy3_line(hy3_line)

    def __init_athlete(self, athlete):
        '''Pseudo-constructor for creating an object from a meet'''
        self.__gender = athlete.gender
        self.__event_swimmer_id = None
        self.__last_name = athlete.last_name
        self.__first_name = athlete.first_name
        self.__nick_name = None
        self.__middle_initial = None
        self.__uss_num = None
        self.__team_swimmer_id = None
        self.__date_of_birth = athlete.date_of_birth
        self.__age = None

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if len(hy3_line) == 130 and hy3_line[0:2] == "D1":
            self._parse_gender(hy3_line[2])
            self._parse_event_swimmer_id(hy3_line[3:8])
            self._parse_last_name(hy3_line[8:28])
            self._parse_first_name(hy3_line[28:48])
            self._parse_nick_name(hy3_line[48:68])
            self._parse_middle_initial(hy3_line[68])
            self._parse_uss_num(hy3_line[69:83])
            self._parse_team_swimmer_id(hy3_line[83:88])
            self._parse_date_of_birth(hy3_line[88:96])
            self._parse_age(hy3_line[97:99])
        else:
            raise line_format_errors.InputLineError()

    def _parse_gender(self, raw_gender):
        """Parse gender from a one character string"""
        if re.match("[MF]", raw_gender.upper()):
            self.__gender = raw_gender.upper()
        else:
            raise line_format_errors.FieldParseError("gender")

    def _parse_event_swimmer_id(self, raw_event_swimmer_id):
        """Parse event swimmer id from the five character string"""
        raw_event_swimmer_id = raw_event_swimmer_id.strip()

        try:
            if len(raw_event_swimmer_id) == 0:
                self.__event_swimmer_id = None
            else:
                self.__event_swimmer_id = int(raw_event_swimmer_id, 10)
        except Exception:
            raise line_format_errors.FieldParseError("event_swimmer_id")

    def _parse_last_name(self, raw_last_name):
        """Parse last name from 20 character string"""
        self.__last_name = raw_last_name.strip()

    def _parse_first_name(self, raw_first_name):
        """Parse first name from 20 character string"""
        self.__first_name = raw_first_name.strip()

    def _parse_nick_name(self, raw_nick_name):
        """Parse nick name from 20 character string"""
        self.__nick_name = raw_nick_name.strip()

    def _parse_middle_initial(self, raw_middle_initial):
        """Parse middle initial from 20 character string"""
        self.__middle_initial = raw_middle_initial.strip()

    def _parse_uss_num(self, raw_uss_num):
        """Parse US Swimming number from 14 character string"""
        try:
            raw_uss_num = raw_uss_num.strip()

            if len(raw_uss_num) == 0:
                self.__uss_num = None
            elif re.match(r"^[\*0-9A-Z]+$", raw_uss_num):
                self.__uss_num = raw_uss_num
            else:
                raise line_format_errors.FieldParseError("uss_num")
        except Exception:
            raise line_format_errors.FieldParseError("uss_num")

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

    def _parse_age(self, raw_age):
        """Parse age from two character string"""
        raw_age = raw_age.strip()

        try:
            if len(raw_age) == 0:
                raise line_format_errors.FieldParseError("age")
            else:
                self.__age = int(raw_age, 10)
        except Exception:
            raise line_format_errors.FieldParseError("age")

    def _parse_date_of_birth(self, raw_date_of_birth):
        """Parse date of birth to date from eight character string"""
        try:
            date_pattern = re.compile(r"^[01][0-9][0-3][0-9][12][0-9]{3}$")
            if date_pattern.match(raw_date_of_birth):
                self.__date_of_birth = datetime.strptime(raw_date_of_birth,
                                                         "%m%d%Y").date()
            else:
                raise line_format_errors.FieldParseError("date_of_birth")
        except Exception:
            raise line_format_errors.FieldParseError("date_of_birth")

    @property
    def hy3_line(self):
        '''return the D1 line for this object'''
        line = 'D1'
        line += self.gender.ljust(1)
        line += str(self.event_swimmer_id).ljust(5)
        line += self.last_name.ljust(20)
        line += self.first_name.ljust(20)
        line += self.nick_name.ljust(20)
        line += self.middle_initial.ljust(1)
        line += self.uss_num.ljust(14)
        line += str(self.team_swimmer_id).ljust(5)
        line += self.date_of_birth.strftime('%m%d%Y')
        line += (' ')
        line += str(self.age).ljust(2)
        line += (' ' * 29)
        return append_check_sum(line)

    @property
    def gender(self):
        """Gender of swimmer"""
        return self.__gender

    @gender.setter
    def gender(self, gender):
        """Gender of swimmer"""
        self.__gender = gender

    @property
    def event_swimmer_id(self):
        """Swimmer ID from event database"""
        return self.__event_swimmer_id

    @event_swimmer_id.setter
    def event_swimmer_id(self, event_swimmer_id):
        """Swimmer ID from event database"""
        self.__event_swimmer_id = event_swimmer_id

    @property
    def last_name(self):
        """Last name of swimmer"""
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        """Last name of swimmer"""
        self.__last_name = last_name

    @property
    def first_name(self):
        """First name of swimmer"""
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        """First name of swimmer"""
        self.__first_name = first_name

    @property
    def nick_name(self):
        """Nick name of swimmer"""
        return self.__nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Nick name of swimmer"""
        self.__nick_name = nick_name

    @property
    def middle_initial(self):
        """Middle initial of swimmer"""
        return self.__middle_initial

    @middle_initial.setter
    def middle_initial(self, middle_initial):
        """Middle initial of swimmer"""
        self.__middle_initial = middle_initial

    @property
    def uss_num(self):
        """US Swimming Id"""
        return self.__uss_num

    @uss_num.setter
    def uss_num(self, uss_num):
        """US Swimming Id"""
        self.__uss_num = uss_num

    @property
    def team_swimmer_id(self):
        """Swimmer Id from team database"""
        return self.__team_swimmer_id

    @team_swimmer_id.setter
    def team_swimmer_id(self, team_swimmer_id):
        """Swimmer Id from team database"""
        self.__team_swimmer_id = team_swimmer_id

    @property
    def date_of_birth(self):
        """Swimmer date of birth"""
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Swimmer date of birth"""
        self.__date_of_birth = date_of_birth

    @property
    def age(self):
        """Swimmer age"""
        return self.__age

    @age.setter
    def age(self, age):
        """Swimmer age"""
        self.__age = age
