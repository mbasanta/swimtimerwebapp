"""Classes for parsing individual lines in HY3 file"""

# pylint: disable=W0403
import re
import line_format_errors
from hy3parser.hy3parser import constants
from hy3parser.hy3parser.utilities import append_check_sum
from swimapp.models.team import Team


class C1Line(object):
    """C1 Line from HY3 file"""
    # pylint: disable-msg=R0902
    def __init__(self, hy3_line=None):
        """Default constructor for empty instance"""
        self.__team_abbr = None
        self.__team_name = None
        self.__team_short_name = None
        self.__team_type = None

        if type(hy3_line) is Team:
            self.__init_team(hy3_line)
        elif hy3_line is not None:
            self.__init_hy3_line(hy3_line)

    def __init_team(self, team):
        '''Pseudo-constructor for creating an object from a meet'''
        self.__team_abbr = team.team_abbr
        self.__team_name = team.team_name
        self.__team_short_name = team.team_short_name
        self.__team_type = team.team_type

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if len(hy3_line) == 130 and hy3_line[0:2] == "C1":
            self._parse_team_abbr(hy3_line[2:7])
            self._parse_team_name(hy3_line[7:37])
            self._parse_team_short_name(hy3_line[37:53])
            self._parse_team_type(hy3_line[119:122])
        else:
            raise line_format_errors.InputLineError()

    def _parse_team_abbr(self, raw_team_abbr):
        """Parse team abbreviation from 5 character string"""
        self.__team_abbr = raw_team_abbr.strip()

    def _parse_team_name(self, raw_team_name):
        """Parse team name from 30 character string"""
        self.__team_name = raw_team_name.strip()

    def _parse_team_short_name(self, raw_team_short_name):
        """Parse team short_name from 16 character string"""
        self.__team_short_name = raw_team_short_name.strip()

    def _parse_team_type(self, raw_team_type):
        """Parse team type from three character string"""
        try:
            raw_team_type = raw_team_type.strip().upper()

            if len(raw_team_type) == 0:
                self.__team_type = None
            elif raw_team_type in constants.LINE_TYPE_CONSTANTS.TEAM_TYPE:
                self.__team_type = raw_team_type
            else:
                raise Exception
        except Exception:
            raise line_format_errors.FieldParseError("team_type")

    @property
    def hy3_line(self):
        '''return the C1 line for this object'''
        line = 'C1'
        line += self.team_abbr.ljust(5)
        line += self.team_name.ljust(30)
        line += self.team_short_name.ljust(16)

        line += (' ' * 66)

        if self.team_type:
            line += self.team_type.type_abbr.rjust(3)
        else:
            line += (' ' * 3)

        line += (' ' * 6)

        return append_check_sum(line)

    @property
    def team_abbr(self):
        """Team abbreviation"""
        return self.__team_abbr

    @team_abbr.setter
    def team_abbr(self, team_abbr):
        """Team abbreviation"""
        self.__team_abbr = team_abbr

    @property
    def team_name(self):
        """Team name"""
        return self.__team_name

    @team_name.setter
    def team_name(self, team_name):
        """Team name"""
        self.__team_name = team_name

    @property
    def team_short_name(self):
        """Team short name"""
        return self.__team_short_name

    @team_short_name.setter
    def team_short_name(self, team_short_name):
        """Team short name"""
        self.__team_short_name = team_short_name

    @property
    def team_type(self):
        """Team type"""
        return self.__team_type

    @team_type.setter
    def team_type(self, team_type):
        """Team type"""
        self.__team_type = team_type


class C2Line(object):
    """C2 Line from HY3 file"""
    # pylint: disable-msg=R0902
    def __init__(self, hy3_line=None):
        """Default constructor for empty instance"""
        self.__addr_name = None
        self.__addr = None
        self.__addr_city = None
        self.__addr_state = None
        self.__addr_zip = None
        self.__addr_country = None
        self.__team_reg = None

        if type(hy3_line) is Team:
            self.__init_team(hy3_line)
        elif hy3_line is not None:
            self.__init_hy3_line(hy3_line)

    def __init_team(self, team):
        '''Pseudo-constructor for creating an object from a meet'''
        self.__addr_name = team.addr_name
        self.__addr = team.addr
        self.__addr_city = team.addr_city
        self.__addr_state = team.addr_state
        self.__addr_zip = team.addr_zip
        self.__addr_country = team.addr_country
        self.__team_reg = team.team_reg

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if len(hy3_line) == 130 and hy3_line[0:2] == "C2":
            self._parse_addr_name(hy3_line[2:32])
            self._parse_addr(hy3_line[32:62])
            self._parse_addr_city(hy3_line[62:92])
            self._parse_addr_state(hy3_line[92:94])
            self._parse_addr_zip(hy3_line[94:104])
            self._parse_addr_country(hy3_line[104:107])
            self._parse_team_reg(hy3_line[108:112])
        else:
            raise line_format_errors.InputLineError()

    def _parse_addr_name(self, raw_addr_name):
        """Parse address name from 30 character string"""
        self.__addr_name = raw_addr_name.strip()

    def _parse_addr(self, raw_addr):
        """Parse address from 30 character string"""
        self.__addr = raw_addr.strip()

    def _parse_addr_city(self, raw_addr_city):
        """Parse address city from 30 character string"""
        self.__addr_city = raw_addr_city.strip()

    def _parse_addr_state(self, raw_addr_state):
        """Parse address state from 2 character string"""
        try:
            raw_addr_state = raw_addr_state.strip().upper()

            if re.match("^([A-Z]{2})?$", raw_addr_state):
                self.__addr_state = raw_addr_state
            else:
                raise Exception
        except Exception:
            raise line_format_errors.FieldParseError("addr_state")

    def _parse_addr_zip(self, raw_addr_zip):
        """Parse address zip from 10 character string"""
        try:
            raw_addr_zip = raw_addr_zip.strip().upper()

            if re.match("^(([0-9]{5})(-[0-9]{4})?)?$", raw_addr_zip):
                self.__addr_zip = raw_addr_zip
            else:
                raise Exception
        except Exception:
            raise line_format_errors.FieldParseError("addr_zip")

    def _parse_addr_country(self, raw_addr_country):
        """Parse address country from 3 character string"""
        try:
            raw_addr_country = raw_addr_country.strip().upper()

            if re.match("^[A-Z]*$", raw_addr_country):
                self.__addr_country = raw_addr_country
            else:
                raise Exception
        except Exception:
            raise line_format_errors.FieldParseError("addr_country")

    def _parse_team_reg(self, raw_team_reg):
        """Parse team reg from three character string"""
        try:
            raw_team_reg = raw_team_reg.strip().upper()

            if len(raw_team_reg) == 0:
                self.__team_reg = None
            elif raw_team_reg in \
                    constants.LINE_TYPE_CONSTANTS.TEAM_REGISTRATION:
                self.__team_reg = raw_team_reg
            else:
                raise Exception
        except Exception:
            raise line_format_errors.FieldParseError("team_reg")

    @property
    def hy3_line(self):
        '''return the C2 line for this object'''
        line = u'C2'
        line += self.addr_name.ljust(30)
        line += self.addr.ljust(30)
        line += self.addr_city.ljust(30)
        line += self.addr_state.ljust(2)
        line += self.addr_zip.ljust(10)
        line += self.addr_country.ljust(3)
        line += (' ')

        if self.team_reg:
            line += self.team_reg.type_abbr.ljust(4)
        else:
            line += (' ' * 4)

        line += (' ' * 16)

        return append_check_sum(line)

    @property
    def addr_name(self):
        """Address name"""
        return self.__addr_name

    @addr_name.setter
    def addr_name(self, addr_name):
        """Address name"""
        self.__addr_name = addr_name

    @property
    def addr(self):
        """Address"""
        return self.__addr

    @addr.setter
    def addr(self, addr):
        """Address"""
        self.__addr = addr

    @property
    def addr_city(self):
        """Address city"""
        return self.__addr_city

    @addr_city.setter
    def addr_city(self, addr_city):
        """Address city"""
        self.__addr_city = addr_city

    @property
    def addr_state(self):
        """Address state"""
        return self.__addr_state

    @addr_state.setter
    def addr_state(self, addr_state):
        """Address state"""
        self.__addr_state = addr_state

    @property
    def addr_zip(self):
        """Address zip"""
        return self.__addr_zip

    @addr_zip.setter
    def addr_zip(self, addr_zip):
        """Address zip"""
        self.__addr_zip = addr_zip

    @property
    def addr_country(self):
        """Address country"""
        return self.__addr_country

    @addr_country.setter
    def addr_country(self, addr_country):
        """Address country"""
        self.__addr_country = addr_country

    @property
    def team_reg(self):
        """Team Registration"""
        return self.__team_reg

    @team_reg.setter
    def team_reg(self, team_reg):
        """Team Registration"""
        self.__team_reg = team_reg


class C3Line(object):
    """C3 Line from HY3 file"""
    # pylint: disable-msg=R0902
    def __init__(self, hy3_line=None):
        """Default constructor for empty instance"""
        self.__daytime_phone = None
        self.__evening_phone = None
        self.__fax = None
        self.__email = None

        if type(hy3_line) is Team:
            self.__init_team(hy3_line)
        elif hy3_line is not None:
            self.__init_hy3_line(hy3_line)

    def __init_team(self, team):
        '''Pseudo-constructor for creating an object from a meet'''
        self.__daytime_phone = team.daytime_phone
        self.__evening_phone = team.evening_phone
        self.__fax = team.fax
        self.__email = team.email

    def __init_hy3_line(self, hy3_line):
        """ Pseudo-constructor for creating and oject from a hy3 file line"""
        if len(hy3_line) == 130 and hy3_line[0:2] == "C3":
            self._parse_daytime_phone(hy3_line[32:52])
            self._parse_evening_phone(hy3_line[52:72])
            self._parse_fax(hy3_line[72:92])
            self._parse_email(hy3_line[92:128])
        else:
            raise line_format_errors.InputLineError()

    def _parse_daytime_phone(self, raw_daytime_phone):
        """Parse daytime phone from 20 character string"""
        self.__daytime_phone = raw_daytime_phone.strip()

    def _parse_evening_phone(self, raw_evening_phone):
        """Parse evening phone from 20 character string"""
        self.__evening_phone = raw_evening_phone.strip()

    def _parse_fax(self, raw_fax):
        """Parse fax from 20 character string"""
        self.__fax = raw_fax.strip()

    def _parse_email(self, raw_email):
        """Parse email address from 36 character string"""
        self.__email = raw_email.strip()

    @property
    def hy3_line(self):
        '''return the C3 line for this object'''
        line = u'C3'
        line += (' ' * 30)
        line += self.daytime_phone.ljust(20)
        line += self.evening_phone.ljust(20)
        line += self.fax.ljust(20)
        line += self.email.ljust(36)

        return append_check_sum(line)

    @property
    def daytime_phone(self):
        """Daytime phone number"""
        return self.__daytime_phone

    @daytime_phone.setter
    def daytime_phone(self, daytime_phone):
        """Daytime phone number"""
        self.__daytime_phone = daytime_phone

    @property
    def evening_phone(self):
        """Evening phone number"""
        return self.__evening_phone

    @evening_phone.setter
    def evening_phone(self, evening_phone):
        """Evening phone number"""
        self.__evening_phone = evening_phone

    @property
    def fax(self):
        """Fax number"""
        return self.__fax

    @fax.setter
    def fax(self, fax):
        """Fax number"""
        self.__fax = fax

    @property
    def email(self):
        """Email number"""
        return self.__email

    @email.setter
    def email(self, email):
        """Email number"""
        self.__email = email
