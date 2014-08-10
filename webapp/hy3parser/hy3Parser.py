"""HY3 file parser"""
# pylint: disable=E1101, W0703, W0403

#Hack for testing
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from django.db import transaction
from swimapp.models import (Meet, Facility, CourseCode, MeetType,
                            Team, TeamType, TeamRegistration,
                            Athlete, Event, Stroke)
from hy3parser.constants import LINE_TYPE_CONSTANTS
from hy3parser.line_formats.b_lines import B1Line, B2Line
from hy3parser.line_formats.c_lines import C1Line, C2Line, C3Line
from hy3parser.line_formats.d1_line import D1Line
from hy3parser.line_formats.e1_line import E1Line
from hy3parser.utilities import MultipleLinesFoundException, vals_from_dict

LINE_TYPE = LINE_TYPE_CONSTANTS.LINE_TYPE


class Hy3Parser(object):
    """hy3 file parser"""

    __LINE_TYPE = LINE_TYPE_CONSTANTS.LINE_TYPE

    @staticmethod
    def __break_out_events(input_file):
        """
        Split up the HY3 file into sections the begin with a B1 line and
        continue until the next B1 Line

        Return a list of lists with the outer list being events and the
        inner lists being the lines for that event inclusive of the B1
        Line
        """
        events = []
        event_lines = []

        with open(input_file) as text:
            for line in text.read().splitlines():
                # reset event if a new b1 line is found
                if (line[0:2] == Hy3Parser.__LINE_TYPE['MEET_INFO'] and
                        len(event_lines) > 0):

                    events.append(event_lines)
                    event_lines = []

                # only capture lines we can handle
                if line[0:2] in vals_from_dict(Hy3Parser.__LINE_TYPE):
                    event_lines.append(line)

            events.append(event_lines)

        return events

    @staticmethod
    def __create_meet_and_facility(meet_info_line, meet_info_cont_line, team):
        """
        Given meet info lines (B1 and B2) retrieve and/or create the
        neccesary entries in the database for meet and facility

        Return the meet
        """

        b1_line = B1Line(meet_info_line)
        b2_line = B2Line(meet_info_cont_line)

        # find or create the faclity
        facility, new_facility = Facility.objects.get_or_create(
            facility_name=b1_line.facility,
            defaults={'elevation': b1_line.elevation}
            )

        if new_facility:
            try:
                length_1 = CourseCode.objects.get(
                    type_abbr=b2_line.course_code_1
                    )
                facility.length_1 = length_1
            except Exception:
                pass

            try:
                length_2 = CourseCode.objects.get(
                    type_abbr=b2_line.course_code_2
                    )
                facility.length_2 = length_2
            except Exception:
                pass

            facility.save()

        # find or create the meet
        meet, new_meet = Meet.objects.get_or_create(
            meet_name=b1_line.meet_name,
            defaults={
                'meet_name': b1_line.meet_name,
                'start_date': b1_line.start_date,
                'end_date': b1_line.end_date,
                'age_up_date': b1_line.age_up_date,
                'facility': facility,
                'meet_masters': b2_line.meet_masters
                }
            )

        if new_meet:
            course_code_1, new_course_code_1 = CourseCode.objects.get_or_create(
                type_abbr=b2_line.course_code_1,
                defaults={'type_name': b2_line.course_code_1}
                )

            course_code_2, new_course_code_2 = CourseCode.objects.get_or_create(
                type_abbr=b2_line.course_code_2,
                defaults={'type_name': b2_line.course_code_2}
                )

            meet_type, new_meet_type = MeetType.objects.get_or_create(
                type_abbr=b2_line.meet_type,
                defaults={'type_name': b2_line.meet_type}
                )

            meet.team = team

            meet.save()

        # return the created meet, if needed facility can come from meet
        return meet

    @staticmethod
    def __create_event(event_line, athlete, meet):
        """
        Get or create the event for a given athlete and return the event
        """
        e1_line = E1Line(event_line)

        stroke, new_stroke = Stroke.objects.get_or_create(
            type_abbr=e1_line.stroke,
            defaults={'type_name': e1_line.stroke}
            )

        event, new_event = Event.objects.get_or_create(
            event_number=e1_line.event_number,
            lower_age=e1_line.lower_age,
            upper_age=e1_line.upper_age,
            gender=e1_line.gender,
            stroke=stroke,
            distance=e1_line.distance,
            distance_units=meet.distance_units
            )

        if new_event:
            event.event_name = event.lower_age + r"/" + \
                event.upper_age + event.gender + r" " + \
                event.distance + event.distance_units + " " + \
                event.stroke.type_name + \
                (" Relay" if event.is_relay else "")

        event.meets.add(meet)
        event.save()

        return event

    @staticmethod
    def __create_entry(event, athlete):
        """
        Get or create the entry for a given athlete and event
        Return the entry
        """
        Entry.objects.get_or_create(
                event = event,
                athlete
            )
    @staticmethod
    def __create_athlete(athlete_line, team):
        """
        Get or create the athlete and assign to team
        Return the athlete
        """

        d1_line = D1Line(athlete_line)

        athlete, new_athlete = Athlete.objects.get_or_create(
            first_name=d1_line.first_name,
            last_name=d1_line.last_name,
            date_of_birth=d1_line.date_of_birth,
            gender=d1_line.gender
            )

        if new_athlete:
            athlete.teams.add(team)
            athlete.save()

        # hack for vim folding
        return athlete

    @staticmethod
    def __create_team(team_name_line, team_address_line, team_contact_line):
        """
        Given the appropriate lines (C1, C2, C3) create and return
        a team if new or just return the team if it already exists
        """

        c1_line = C1Line(team_name_line)
        c2_line = C2Line(team_address_line)
        c3_line = C3Line(team_contact_line)

        team_type, new_team_type = TeamType.objects.get_or_create(
            type_abbr=c1_line.team_type,
            defaults={'type_name': c1_line.team_type}
            )

        team_reg, new_team_reg = TeamRegistration.objects.get_or_create(
            type_abbr=c2_line.team_reg,
            defaults={'type_name': c2_line.team_reg}
            )

        team, new_team = Team.objects.get_or_create(
            team_abbr=c1_line.team_abbr,
            defaults={
                'team_name': c1_line.team_name,
                'team_short_name': c1_line.team_short_name,
                'team_type': team_type,
                'addr_name': c2_line.addr_name,
                'addr': c2_line.addr,
                'addr_city': c2_line.addr_city,
                'addr_state': c2_line.addr_state,
                'addr_zip': c2_line.addr_zip,
                'addr_country': c2_line.addr_country,
                'team_reg': team_reg,
                'daytime_phone': c3_line.daytime_phone,
                'evening_phone': c3_line.evening_phone,
                'fax': c3_line.fax,
                'email': c3_line.email
                }
            )
        # return team
        return team

    @staticmethod
    def __filter_line_type(lines_list, line_type, multiple=False):
        """
        Find line_type in lines_list

        Return a list of lines of the particular type

        If multiple is set to false (default) will throw a
        MultipleLinesFoundException if more than one line of given
        type is found.
        """

        found_lines = []

        for line in lines_list:
            if line[0:2] == line_type:
                if len(found_lines) == 0:
                    found_lines.append(line)
                elif len(found_lines) > 0 and multiple:
                    found_lines.append(line)
                else:
                    raise MultipleLinesFoundException

        return found_lines

    @staticmethod
    def __filter_athlete_lines(lines_list):
        """
        Give a list of lines returns a list of athletes and entries in
        following format
        [
            {
                'athlete': string D1 line
                'events': list of E1 lines
            }
        ]
        """

        athletes = []
        athlete = ""
        events = []

        for line in lines_list:
            if line[0:2] == Hy3Parser.__LINE_TYPE['SWIMMER_INFO_1']:
                if len(athlete) == 0:
                    athlete = line
                else:
                    athletes.append({
                        'athlete': athlete,
                        'events': events
                        })
                    athlete = ""
                    events = []
            if line[0:2] == Hy3Parser.__LINE_TYPE['INDIVIDUAL_ENTRY']:
                events.append(line)

        return athletes

    @staticmethod
    @transaction.atomic
    def parse_file(input_file):
        """
        Parse event info out of a HY3 file and write to the database
        """
        event_lines = Hy3Parser.__break_out_events(input_file)

        for event in event_lines:
            meet_info = Hy3Parser.__filter_line_type(
                event,
                Hy3Parser.__LINE_TYPE['MEET_INFO']
                )

            meet_info_cont = Hy3Parser.__filter_line_type(
                event,
                Hy3Parser.__LINE_TYPE['MEET_INFO_CONT']
                )

            team_name = Hy3Parser.__filter_line_type(
                event,
                Hy3Parser.__LINE_TYPE['TEAM_INFO_1']
                )

            team_address = Hy3Parser.__filter_line_type(
                event,
                Hy3Parser.__LINE_TYPE['TEAM_INFO_2']
                )

            team_contact = Hy3Parser.__filter_line_type(
                event,
                Hy3Parser.__LINE_TYPE['TEAM_INFO_3']
                )

            athletes = Hy3Parser.__filter_athlete_lines(event)

        team = Hy3Parser.__create_team(team_name[0],
                                       team_address[0],
                                       team_contact[0])

        meet = Hy3Parser.__create_meet_and_facility(meet_info[0],
                                                    meet_info_cont[0],
                                                    team)

        athlete_ids = []
        for athlete in athletes:
            athlete_obj = Hy3Parser.__create_athlete(athlete['athlete'], team)
            athlete_ids.append(athlete_obj.id)

            for event in athlete['events']:
                event_obj = Hy3Parser.__create_event(event, athlete_obj, meet)
                entry_obj = Hy3Parser.__create_entry(event_obj, athlete_obj)

        return (meet.id, team.id, athlete_ids)


# TODO: Remove eventually
def break_out_lines(input_file):
    """Split HY3 file into individual lines and return as dictionary"""
    # pylint: disable=R0912
    file_data = {}
    text = open(input_file)

    for line in text.read().splitlines():

        if line[0:2] == LINE_TYPE['MEET_INFO']:
            if not LINE_TYPE['MEET_INFO'] in file_data:
                file_data[LINE_TYPE['MEET_INFO']] = []
            file_data[LINE_TYPE['MEET_INFO']].append(B1Line(line))

        if line[0:2] == LINE_TYPE['MEET_INFO_CONT']:
            if not LINE_TYPE['MEET_INFO_CONT'] in file_data:
                file_data[LINE_TYPE['MEET_INFO_CONT']] = []
            file_data[LINE_TYPE['MEET_INFO_CONT']].append(B2Line(line))

        if line[0:2] == LINE_TYPE['TEAM_INFO_1']:
            if not LINE_TYPE['TEAM_INFO_1'] in file_data:
                file_data[LINE_TYPE['TEAM_INFO_1']] = []
            file_data[LINE_TYPE['TEAM_INFO_1']].append(C1Line(line))

        if line[0:2] == LINE_TYPE['TEAM_INFO_2']:
            if not LINE_TYPE['TEAM_INFO_2'] in file_data:
                file_data[LINE_TYPE['TEAM_INFO_2']] = []
            file_data[LINE_TYPE['TEAM_INFO_2']].append(C2Line(line))

        if line[0:2] == LINE_TYPE['TEAM_INFO_3']:
            if not LINE_TYPE['TEAM_INFO_3'] in file_data:
                file_data[LINE_TYPE['TEAM_INFO_3']] = []
            file_data[LINE_TYPE['TEAM_INFO_3']].append(C3Line(line))

        if line[0:2] == LINE_TYPE['SWIMMER_INFO_1']:
            if not LINE_TYPE['SWIMMER_INFO_1'] in file_data:
                file_data[LINE_TYPE['SWIMMER_INFO_1']] = []
            file_data[LINE_TYPE['SWIMMER_INFO_1']].append(D1Line(line))

        if line[0:2] == LINE_TYPE['SWIMMER_INFO_2']:
            pass
        if line[0:2] == LINE_TYPE['SWIMMER_INFO_3']:
            pass
        if line[0:2] == LINE_TYPE['SWIMMER_INFO_4']:
            pass
        if line[0:2] == LINE_TYPE['SWIMMER_INFO_5']:
            pass
        if line[0:2] == LINE_TYPE['INDIVIDUAL_ENTRY']:
            if not LINE_TYPE['INDIVIDUAL_ENTRY'] in file_data:
                file_data[LINE_TYPE['INDIVIDUAL_ENTRY']] = []
            file_data[LINE_TYPE['INDIVIDUAL_ENTRY']].append(E1Line(line))

        if line[0:2] == LINE_TYPE['INDIVIDUAL_RESULTS']:
            pass
        if line[0:2] == LINE_TYPE['RELAY_ENTRY']:
            pass
        if line[0:2] == LINE_TYPE['RELAY_RESULTS']:
            pass

    text.close()
    return file_data
