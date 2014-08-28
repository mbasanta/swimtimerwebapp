# -*- coding: utf-8 -*-
"""
Spyder Editor

Populates swimtimer app data base with some preconfigured teams, athletes, 
meets, events, and entries.

Requires male and female athlete files ('Male Athletes.csv' and
 'Female Athletes.csv')

Flags:
    createDomainTables: recreates all domain level tables
    createTeamsAndAthletes: self explainatory

This temporary script file is located here:
/Users/bkant/.spyder2/.temp.py
"""

import sys
import psycopg2
import datetime
import random
import copy
import numpy as np

#takes csv string of athlete properties and returns a dictionary
def athleteFromProps(propsStr):
    props = propsStr.split(',')
    athlete = {}
    athlete['first_name']       = props[0]
    athlete['last_name']        = props[1]
    athlete['gender']           = props[2]
    athlete['date_of_birth']    = props[3]
    athlete['time_entered']     = props[4]
    athlete['time_modified']    = props[5]
    
    return athlete
    

createDomainTables = False
createTeamsAndAthletes = False

#date time use in several places
now = datetime.datetime.now()

try:
    conn = psycopg2.connect("dbname='swimteam_dev' user='swimteam_user' host='swimtimer.cloudapp.net' password='swimteam_user'")
except Exception as e:
    print "I am unable to connect to the database"
    print e
    
curs = conn.cursor()

#clean out everything
try:
    curs.execute("""DELETE FROM swimapp_athleteentry;""")
    print "\tDeleted athlete entry"
    curs.execute("""DELETE FROM swimapp_entry;""")
    print "\tDeleted entry"
    curs.execute("""DELETE FROM swimapp_meetevent;""")
    print "\tDeleted meet event"
    curs.execute("""DELETE FROM swimapp_event;""")
    print "\tDeleted event"
    curs.execute("""DELETE FROM swimapp_meet_teams;""")
    print "\tDeleted meet teams"
    curs.execute("""DELETE FROM swimapp_meet;""")
    print "\tDeleted meet"
    
    if createTeamsAndAthletes:
        curs.execute("""DELETE FROM swimapp_athlete_teams;""")
        print "\tDeleted athlete teams"
        curs.execute("""DELETE FROM swimapp_athlete;""")
        print "\tDeleted athlete"
        curs.execute("""DELETE fROM swimapp_facility;""")
        print "\tDeleted facility"
        curs.execute("""DELETE FROM swimapp_team_users;""")
        print "\tDeleted team users"
        curs.execute("""DELETE FROM swimapp_team;""")
        print "\tDeleted team"
        
    if createDomainTables:
        curs.execute("""DELETE FROM swimapp_coursecode;""")
        print "\tDeleted course code"
        curs.execute("""DELETE FROM swimapp_meetconfig;""")
        print "\tDeleted meet config"
        curs.execute("""DELETE FROM swimapp_meettype;""")
        print "\tDeleted meet type"
        curs.execute("""DELETE FROM swimapp_stroke;""")
        print "\tDeleted stroke"
        curs.execute("""DELETE FROM swimapp_teamregistration""")
        print "\tDeleted team registration"
        curs.execute("""DELETE FROM swimapp_teamtype""")
        print "\tDeleted team type"
    
except Exception as e:
    print "Failed to clean out database"
    print e
    sys.exit()
    
print "Cleaned out DB"

if createDomainTables:
    
    #========================================
    #Team Types
    #========================================
    
    #table
    #   swimapp_teamtype
    #columns
    #   id                  (primary key, auto increment)
    #   type_abbr           (varchar(3), not null)
    #   type_name           (varchar(50), not null)
    
    teamtypes = [
        {'abbr':'AGE',      'name':'Age Group'},
        {'abbr':'COL',      'name':'College'},
        {'abbr':'HS',       'name':'High School'},
        {'abbr':'MAS',      'name':'Masters'},
        {'abbr':'OTH',      'name':'Other'},
        {'abbr':'REC',      'name':'Recreation'}
    ]
    
    try:
        #add data
        curs.executemany("""INSERT INTO swimapp_teamtype (type_abbr, type_name)""" \
        """ VALUES (%(abbr)s, %(name)s);""", teamtypes)
    except Exception as e:
        print "Failed to execute many on swimapp_teamtype"
        print e
        sys.exit()
        
    print "Team types complete"
    
    #========================================
    #Team Registrations
    #========================================
    
    #table
    #   swimapp_teamregistration
    #columns
    #   id                  (primary key, auto increment)
    #   type_abbr           (varchar(4), not null)
    #   type_name           (varchar(50), not null)
    
    teamregistrations = [
        {'abbr':'AUST',     'name':'Australia'},
        {'abbr':'BCSS',     'name':'Canada'},
        {'abbr':'BS',       'name':'British Swimming'},
        {'abbr':'NZSF',     'name':'New Zealand'},
        {'abbr':'OTH',      'name':'Other'},
        {'abbr':'SSA',      'name':'South Africa'},
        {'abbr':'USS',      'name':'United States Swimming'}
    ]
    
    try:
        #add data
        curs.executemany("""INSERT INTO swimapp_teamregistration (type_abbr, type_name)""" \
        """ VALUES (%(abbr)s, %(name)s);""", teamregistrations)
    except Exception as e:
        print "Failed to execute many on swimapp_teamregistration"
        print e
        sys.exit()
        
    print "Team registrations complete"
    
    #========================================
    #Strokes
    #========================================
    
    #table
    #   swimapp_stroke
    #columns
    #   id                  (primary key, auto increment)
    #   type_abbr           (varchar(1), not null)
    #   type_name           (varchar(50), not null)
    
    #(A=Free, B=Back, C=Breast, D=Fly, E=Medley)
    strokes = [
        {'abbr':'A',        'name':'Free'},
        {'abbr':'B',        'name':'Back'},
        {'abbr':'C',        'name':'Breast'},
        {'abbr':'D',        'name':'Fly'},
        {'abbr':'E',        'name':'Medley'}
    ]
    
    try:
        #add data
        curs.executemany("""INSERT INTO swimapp_stroke (type_abbr, type_name)""" \
        """ VALUES (%(abbr)s, %(name)s);""", strokes)
    except Exception as e:
        print "Failed to execute many on swimapp_stroke"
        print e
        sys.exit()
        
    print "Strokes complete"
    
    #========================================
    #Meet Types
    #========================================
    
    #table
    #   swimapp_meettype
    #columns
    #   id                  (primary key, auto increment)
    #   type_abbr           (varchar(2), not null)
    #   type_name           (varchar(50), not null)
    
    meetTypes = [
        {'abbr':'AG',   'name':'Age Group'},
        {'abbr':'HS',   'name':'High School'},
        {'abbr':'SR',   'name':'Senior'}
    ]
    
    try:
        curs.executemany("""INSERT INTO swimapp_meettype (type_abbr, type_name)""" \
        """ VALUES (%(abbr)s, %(name)s);""", meetTypes)
    except Exception as e:
        print "Failed to execute many on swimapp_meettype"
        print e
        sys.exit()
        
    print "Meet Types complete"
    
    #========================================
    #Meet Config (ignore for now) Intrasquad, Dual, Championship, etc.
    #========================================
    
    #table
    #   swimapp_meetconfig
    #columns
    #   id                  (primary key, auto increment)
    #   type_name           (varchar(50), not null)
    
    meetConfigs = [
        ('Intrasquad',),
        ('Dual',),
        ('Championship',)
    ]
    
    try:
        curs.executemany("""INSERT INTO swimapp_meetconfig (type_name)""" \
        """ VALUES (%s);""", meetConfigs)
    except Exception as e:
        print "Failed to execute many on swimapp_meetconfig"
        print e
        sys.exit()
        
    print "Meet Configs complete"
    
    #========================================
    #Course Codes
    #========================================
    
    #table
    #   swimapp_coursecode
    #columns
    #   id                  (primary key, auto increment)
    #   type_abbr           (varchar(1), not null)
    #   type_name           (varchar(50), not null)
    
    courseCodes = [
        {'abbr':'Y',    'name':'Yards'},
        {'abbr':'S',    'name':'Short Course Meters'},
        {'abbr':'L',    'name':'Long Course Meters'}
    ]
    
    try:
        curs.executemany("""INSERT INTO swimapp_coursecode (type_abbr, type_name)""" \
        """ VALUES (%(abbr)s, %(name)s);""", courseCodes)
    except Exception as e:
        print "Failed to execute many on swimapp_coursecode"
        print e
        sys.exit()
        
    print "Course Codes complete"
    
#end of domain tables
    
if createTeamsAndAthletes:
    
    #========================================
    #Teams
    #========================================
    
    #table
    #   swimapp_team
    #columns
    #   id                  (primary key, auto increment)
    #   team_abbr           (varchar(5), not null)
    #   team_name           (varchar(30), not null)
    #   team_short_name     (varchar(16), not null)
    #   team_type_id        (integer, not null)
    #   team_color1         (varchar(10))
    #   team_color2         (varchar(10))
    #   addr_name           (varchar(30), not null)
    #   addr                (varchar(30), not null)
    #   addr_city           (varchar(30), not null)
    #   addr_state          (varchar(2), not null)
    #   addr_zip            (varchar(10), not null)
    #   addr_country        (varchar(3), not null)
    #   latitude            (double)
    #   longitude           (double)
    #   team_reg_id         (integer, not null)
    #   daytime_phone       (varchar(20), not null)
    #   evening_phone       (varchar(20), not null)
    #   fax                 (varchar(20), not null)
    #   email               (varchar(36), not null)
    #   time_entered        (timestamp, not null)
    #   time_modified       (timestamp, not null)
    
    try:
        curs.execute("SELECT id FROM swimapp_teamtype WHERE type_abbr = 'AGE'")
        ageTypeId = curs.fetchone()[0]
        
        curs.execute("SELECT id FROM swimapp_teamregistration WHERE type_abbr = 'OTH';")
        otherRegistrationId = curs.fetchone()[0]
    except Exception as e:
        print "Failed to attain team type and registration"
        print e
        sys.exit()
    
    teams = [
        {
            'team_abbr':'GSP',
            'team_name':'Gardenside Penguins',
            'team_short_name':'Penguins',
            'team_type_id':ageTypeId,
            'team_color1':None,
            'team_color2':None,
            'addr_name':'Pool',
            'addr':'957 Lane Allen Rd.',
            'addr_city':'Lexington',
            'addr_state':'KY',
            'addr_zip':'40504',
            'addr_country':'USA',
            'team_reg_id':otherRegistrationId,
            'daytime_phone':'(859)312-3013',
            'evening_phone':'(859)224-8529',
            'fax':'(859)312-3013',
            'email':'benkant@gmail.com',
            'time_entered':now,
            'time_modified':now
        },
        {
            'team_abbr':'WOS',
            'team_name':'Willow Oak Sharks',
            'team_short_name':'Sharks',
            'team_type_id':ageTypeId,
            'team_color1':None,
            'team_color2':None,
            'addr_name':'Pool',
            'addr':'636 Twin Pines Way',
            'addr_city':'Lexington',
            'addr_state':'KY',
            'addr_zip':'40514',
            'addr_country':'USA',
            'team_reg_id':otherRegistrationId,
            'daytime_phone':'(859)533-9917',
            'evening_phone':'(859)533-9917',
            'fax':'(859)533-9917',
            'email':'matthewbasanta@gmail.com',
            'time_entered':now,
            'time_modified':now
        },
        {
            'team_abbr':'CWH',
            'team_name':'Crestwood Hills Wahoos',
            'team_short_name':'Wahoos',
            'team_type_id':ageTypeId,
            'team_color1':None,
            'team_color2':None,
            'addr_name':'Pool',
            'addr':'8740 Fox Lonas Rd.',
            'addr_city':'Knoxville',
            'addr_state':'TN',
            'addr_zip':'37923',
            'addr_country':'USA',
            'team_reg_id':otherRegistrationId,
            'daytime_phone':'(865)690-2509',
            'evening_phone':'(865)690-2509',
            'fax':'(865)690-2509',
            'email':'jeffallentn@gmail.com',
            'time_entered':now,
            'time_modified':now
        }
    ]
    
    
    try:
        curs.executemany("""INSERT INTO swimapp_team (team_abbr, team_name,""" \
        """ team_short_name, team_type_id, addr_name, addr, addr_city, addr_state,""" \
        """ addr_zip, addr_country, team_reg_id, daytime_phone, evening_phone,""" \
        """ fax, email, time_entered, time_modified) VALUES (%(team_abbr)s,""" \
        """ %(team_name)s, %(team_short_name)s, %(team_type_id)s, %(addr_name)s,""" \
        """ %(addr)s, %(addr_city)s, %(addr_state)s, %(addr_zip)s, %(addr_country)s,""" \
        """ %(team_reg_id)s, %(daytime_phone)s, %(evening_phone)s, %(fax)s, """ \
        """ %(email)s, %(time_entered)s, %(time_modified)s)""", teams)
    except Exception as e:
        print "Failed to execute many on swimapp_team"
        print e
        sys.exit()
    
    print "Teams complete"
    
    #========================================
    #Team Users (ignore for now)
    #========================================
    
    #table
    #   swimapp_team_users
    #columns
    #   id                  (primary key, auto increment)
    #   team_id             (int, not null)
    #   appuser_id          (int, not null)
    
    
    #========================================
    #Facilities
    #========================================
    
    #table
    #   swimapp_facility
    #columns
    #   id                  (primary key, auto increment)
    #   facility_name       (varchar(45), not null)
    #   elevation           (int, nullable)
    #   length_1_id         (int, nullable)
    #   length_2_id         (int, nullable)
    #   addr_name           (varchar(30), nullable)
    #   addr                (varchar(30), nullable)
    #   addr_city           (varchar(30), nullable)
    #   addr_state          (varchar(2), nullable)
    #   addr_zip            (varchar(10), nullable)
    #   addr_country        (varchar(3), nullable)
    #   latitude            (double, nullable)
    #   longitude           (double, nullable)
    #   time_entered        (timestamp, not null)
    #   time_modified       (timestamp, not null)
    
    try:
        curs.execute("""SELECT team_short_name FROM swimapp_team;""")
        teamNames = curs.fetchall()
        
        curs.execute("""SELECT id FROM swimapp_coursecode WHERE type_abbr='Y';""")
        yardsCourseId = curs.fetchone()
        
        for teamName in teamNames:
            facilityName = teamName[0] + ' Home'
            curs.execute("""INSERT INTO swimapp_facility (facility_name, length_1_id,""" \
            """ time_entered, time_modified) VALUES (%s, %s, %s, %s);""", (facilityName, yardsCourseId, now, now))
            
    except Exception as e:
        print "Failed to create Facilities"
        print e
        sys.exit()
        
    print "Facilities complete"
    
    #========================================
    #Athletes
    #========================================
    
    #table
    #   swimapp_athlete
    #columns
    #   id                  (primary key, auto increment)
    #   first_name          (varchar(30), not null)
    #   last_name           (varchar(30), not null)
    #   date_of_birth       (date, not null)
    #   time_entered        (timestamp, not null)
    #   time_modified       (timestamp, not null)
    #   gender              (varchar(1), nullable)
    
    athletes = []
    
    maleFid = open('Male Athletes.csv','r')
    maleFid.readline()
    
    for line in maleFid:
        athletes.append(athleteFromProps(line))
    
    femaleFid = open('Female Athletes.csv','r')
    femaleFid.readline()
    
    for line in femaleFid:
        athletes.append(athleteFromProps(line))
    
    try:
        curs.executemany("""INSERT INTO swimapp_athlete (first_name, last_name,""" \
        """ date_of_birth, time_entered, time_modified, gender) VALUES (%(first_name)s,""" \
        """ %(last_name)s, %(date_of_birth)s, %(time_entered)s, %(time_modified)s,""" \
        """ %(gender)s);""", athletes)
    except Exception as e:
        print "Failed to execute many on swimapp_athlete"
        print e
        sys.exit()
        
    print "Athletes complete"
    
    #========================================
    #Athletes Teams
    #========================================
    
    #table
    #   swimapp_athlete_teams
    #columns
    #   id                  (primary key, auto increment)
    #   athlete_id          (int, not null)
    #   team_id             (int, not null)
    
    try:
        curs.execute("""SELECT id FROM swimapp_team;""")
        teamIds = curs.fetchall()
        
        curs.execute("""SELECT id FROM swimapp_athlete;""")
        athleteIds = curs.fetchall()
        
        for teamId in teamIds:
            #assign 100 swimmers to each team
            for i in range(100):
                #randomly select athlete id
                athleteId = athleteIds.pop(random.randint(0, len(athleteIds)))
                curs.execute("""INSERT INTO swimapp_athlete_teams (athlete_id, team_id)""" \
                """ VALUES (%s, %s)""", (athleteId, teamId))
    except Exception as e:
        print "Failed to associate athletes with teams"
        print e
        sys.exit()
    
    print "Athlete teams complete"

#end of teams and athletes

#========================================
#Meets
#========================================

#table
#   swimapp_meet
#columns
#   id                  (primary key, auto increment)
#   meet_name           (varchar(45), not null)
#   facility_id         (int, not null)
#   start_date          (timestamp, nullable)
#   end_date            (timestamp, nullable)
#   age_up_date         (date, nullable)
#   course_code_1_id    (int, nullable)
#   course_code_2_id    (int, nullable)
#   meet_config_id      (int, nullable)
#   team_id             (int, nullable)
#   time_entered        (timestamp, not null)
#   time_modified       (timestamp, not null)
#   meet_masters        (bool, not null)
#   meet_type_id        (int, nullable)

#========================================
#Meet Teams
#========================================

#table
#   swimapp_meet_teams
#columns
#   id                  (primary key, auto increment)
#   meet_id             (int, not null)
#   team_id             (int, not null)

#create a dual meet between each team created
try:
    curs.execute("""SELECT (swimapp_team.id, swimapp_team.team_short_name,""" \
    """ swimapp_facility.id) FROM swimapp_facility JOIN swimapp_team ON""" \
    """ swimapp_facility.facility_name = swimapp_team.team_short_name || ' Home'""")
    tmpTeams = curs.fetchall()
    
    #print "\ttmpTeams: " + str(tmpTeams)
    
    teams = []
    for tmpTeam in tmpTeams:
        teams.append(tmpTeam[0][1:-1].split(','))
    
    #print "\tteams: " + str(teams)
    
    startDate = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=14, hours=19)
    ageUpDate = datetime.date(2014, 5, 1)
    
    curs.execute("""SELECT id FROM swimapp_coursecode WHERE type_abbr = 'Y';""")
    yardsCourseCodeId = curs.fetchone()[0]
    
    #print "\tYards course code id: " + str(yardsCourseCodeId)
    
    curs.execute("""SELECT id FROM swimapp_meetconfig WHERE type_name = 'Dual';""")
    dualMeetConfigId = curs.fetchone()[0]
    
    #print "\tDual meet config id: " + str(dualMeetConfigId)
    
    curs.execute("""SELECT id FROM swimapp_meettype WHERE type_abbr = 'AG';""")
    ageGroupMeetTypeId = curs.fetchone()[0]
    
    #print "\tAge group meet type id: " + str(ageGroupMeetTypeId)
    
    #keep track of how many meets a team is hosting
    teamIdHostCount = {}
    for team in teams:
        teamIdHostCount[team[0]] = 0
    
    #print "\tteamIdHostCount: " + str(teamIdHostCount)
    
    meetIds = []
    while len(teams) > 0:
        team1 = teams.pop()
        for team2 in teams:
            if (teamIdHostCount[team1[0]] <= teamIdHostCount[team2[0]]):
                hostTeam = team1
                visitorTeam = team2
            else:
                hostTeam = team2
                visitorTeam = team1
                
            meet = {
                'name' : visitorTeam[1] + ' at ' + hostTeam[1],
                'facility_id' : hostTeam[2],
                'start' : startDate,
                'age_up' : ageUpDate,
                'course_code' : yardsCourseCodeId,
                'meet_config' : dualMeetConfigId,
                'host_id' : hostTeam[0],
                'visitor_id' : visitorTeam[0],
                'time_entered' : now,
                'time_modified' : now,
                'meet_masters' : False,
                'meet_type' : ageGroupMeetTypeId
            }          
            
            #keep track of number of meets hosted by team to keep them relatively even
            teamIdHostCount[hostTeam[0]] += 1
            
            #print "\tmeet: " + str(meet)
            
            curs.execute("""INSERT INTO swimapp_meet (meet_name, facility_id,""" \
            """ start_date, age_up_date, course_code_1_id, meet_config_id,""" \
            """ team_id, time_entered, time_modified, meet_masters, meet_type_id)""" \
            """ VALUES (%(name)s, %(facility_id)s, %(start)s, %(age_up)s,""" \
            """ %(course_code)s, %(meet_config)s, %(host_id)s, %(time_entered)s,""" \
            """ %(time_modified)s, %(meet_masters)s, %(meet_type)s) RETURNING id;""", meet)
            meetId = curs.fetchone()[0]
            
            meetIds.append(meetId)
            
            curs.execute("""INSERT INTO swimapp_meet_teams (meet_id, team_id)""" \
            """ VALUES (%s, %s);""", (meetId, meet['host_id']))
            curs.execute("""INSERT INTO swimapp_meet_teams (meet_id, team_id)""" \
            """ VALUES (%s, %s);""", (meetId, meet['visitor_id']))
    
except Exception as e:
    print "Failed to create meets"
    print e
    sys.exit()

print "Meets and Meet Teams complete"

#========================================
#Events
#========================================

#table
#   swimapp_event
#columns
#   id                  (primary key, auto increment)
#   event_name          (varchar(100), not null)
#   event_number        (integer, not null)
#   lower_age           (integer, not null)
#   upper_age           (integer, not null)
#   gender              (varchar(1), not null)
#   stroke_id           (integer, not null)
#   distance            (integer, not null)
#   distance_units      (varchar(1), not null)
#   is_relay            (bool, not null)
#   time_entered        (timestamp, not null)
#   time_modified       (timestamp, not null)

#========================================
#Meet Events
#========================================

#table
#   swimapp_meetevent
#columns
#   id                  (primary key, auto increment)
#   meet_id             (int, not null)
#   event_id            (int, not null)

try:
    curs.execute("""SELECT id FROM swimapp_stroke WHERE type_abbr = 'A';""")
    freeId = curs.fetchone()[0]
    
    #print "\tFree Id: " + str(freeId)
    
    curs.execute("""SELECT id FROM swimapp_stroke WHERE type_abbr = 'B';""")
    backId = curs.fetchone()[0]
    
    #print "\tBack Id: " + str(backId)
    
    curs.execute("""SELECT id FROM swimapp_stroke WHERE type_abbr = 'C';""")
    breastId = curs.fetchone()[0]
    
    #print "\tBreast Id: " + str(breastId)
    
    curs.execute("""SELECT id FROM swimapp_stroke WHERE type_abbr = 'D';""")
    flyId = curs.fetchone()[0]
    
    #print "\tFly Id: " + str(flyId)
    
    curs.execute("""SELECT id FROM swimapp_stroke WHERE type_abbr = 'E';""")
    medleyId = curs.fetchone()[0]
    
    #print "\tMedley Id: " + str(medleyId)

    events = [
        {'name' : '8U Girls 100Y IM'                , 'number' : 1 , 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Boys 100Y IM'                 , 'number' : 2 , 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Girls 100Y IM'              , 'number' : 3 , 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Boys 100Y IM'               , 'number' : 4 , 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Girls 100Y IM'             , 'number' : 5 , 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Boys 100Y IM'              , 'number' : 6 , 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Girls 200Y IM'             , 'number' : 7 , 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Boys 200Y IM'              , 'number' : 8 , 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Girls 200Y IM'             , 'number' : 9 , 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Boys 200Y IM'              , 'number' : 10, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Girls 25Y Free'               , 'number' : 11, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Boys 25Y Free'                , 'number' : 12, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Girls 25Y Free'             , 'number' : 13, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Boys 25Y Free'              , 'number' : 14, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Girls 50Y Free'            , 'number' : 15, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Boys 50Y Free'             , 'number' : 16, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Girls 50Y Free'            , 'number' : 17, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Boys 50Y Free'             , 'number' : 18, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Girls 50Y Free'            , 'number' : 19, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Boys 50Y Free'             , 'number' : 20, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Girls 100Y Medley Relay'      , 'number' : 21, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Boys 100Y Medley Relay'       , 'number' : 22, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Girls 100Y Medley Relay'    , 'number' : 23, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Boys 100Y Medley Relay'     , 'number' : 24, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Girls 200Y Medley Relay'   , 'number' : 25, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Boys 200Y Medley Relay'    , 'number' : 26, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Girls 200Y Medley Relay'   , 'number' : 27, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Boys 200Y Medley Relay'    , 'number' : 28, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Girls 200Y Medley Relay'   , 'number' : 29, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'F', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Boys 200Y Medley Relay'    , 'number' : 30, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'M', 'strokeId' : medleyId, 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Girls 25Y Back'               , 'number' : 31, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'F', 'strokeId' : backId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Boys 25Y Back'                , 'number' : 32, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'M', 'strokeId' : backId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Girls 25Y Back'             , 'number' : 33, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'F', 'strokeId' : backId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Boys 25Y Back'              , 'number' : 34, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'M', 'strokeId' : backId  , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Girls 50Y Back'            , 'number' : 35, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'F', 'strokeId' : backId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Boys 50Y Back'             , 'number' : 36, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'M', 'strokeId' : backId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Girls 50Y Back'            , 'number' : 37, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'F', 'strokeId' : backId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Boys 50Y Back'             , 'number' : 38, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'M', 'strokeId' : backId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Girls 50Y Back'            , 'number' : 39, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'F', 'strokeId' : backId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Boys 50Y Back'             , 'number' : 40, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'M', 'strokeId' : backId  , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Girls 25Y Breast'             , 'number' : 41, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'F', 'strokeId' : breastId, 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Boys 25Y Breast'              , 'number' : 42, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'M', 'strokeId' : breastId, 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Girls 25Y Breast'           , 'number' : 43, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'F', 'strokeId' : breastId, 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Boys 25Y Breast'            , 'number' : 44, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'M', 'strokeId' : breastId, 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Girls 50Y Breast'          , 'number' : 45, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'F', 'strokeId' : breastId, 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Boys 50Y Breast'           , 'number' : 46, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'M', 'strokeId' : breastId, 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Girls 50Y Breast'          , 'number' : 47, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'F', 'strokeId' : breastId, 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Boys 50Y Breast'           , 'number' : 48, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'M', 'strokeId' : breastId, 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Girls 50Y Breast'          , 'number' : 49, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'F', 'strokeId' : breastId, 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Boys 50Y Breast'           , 'number' : 50, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'M', 'strokeId' : breastId, 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Girls 25Y Fly'                , 'number' : 51, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'F', 'strokeId' : flyId   , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Boys 25Y Fly'                 , 'number' : 52, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'M', 'strokeId' : flyId   , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Girls 25Y Fly'              , 'number' : 53, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'F', 'strokeId' : flyId   , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Boys 25Y Fly'               , 'number' : 54, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'M', 'strokeId' : flyId   , 'distance' : 25 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Girls 50Y Fly'             , 'number' : 55, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'F', 'strokeId' : flyId   , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Boys 50Y Fly'              , 'number' : 56, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'M', 'strokeId' : flyId   , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Girls 50Y Fly'             , 'number' : 57, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'F', 'strokeId' : flyId   , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Boys 50Y Fly'              , 'number' : 58, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'M', 'strokeId' : flyId   , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Girls 50Y Fly'             , 'number' : 59, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'F', 'strokeId' : flyId   , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Boys 50Y Fly'              , 'number' : 60, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'M', 'strokeId' : flyId   , 'distance' : 50 , 'units' : 'Y', 'isRelay' : False, 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Girls 100Y Free Relay'        , 'number' : 61, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '8U Boys 100Y Free Relay'         , 'number' : 62, 'lowerAge' : 0 , 'upperAge' : 8 , 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Girls 100Y Free Relay'      , 'number' : 63, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '9/10 Boys 100Y Free Relay'       , 'number' : 64, 'lowerAge' : 9 , 'upperAge' : 10, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 100, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Girls 200Y Free Relay'     , 'number' : 65, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '11/12 Boys 200Y Free Relay'      , 'number' : 66, 'lowerAge' : 11, 'upperAge' : 12, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Girls 200Y Free Relay'     , 'number' : 67, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '13/14 Boys 200Y Free Relay'      , 'number' : 68, 'lowerAge' : 13, 'upperAge' : 14, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Girls 200Y Free Relay'     , 'number' : 69, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'F', 'strokeId' : freeId  , 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
        {'name' : '15/18 Boys 200Y Free Relay'      , 'number' : 70, 'lowerAge' : 15, 'upperAge' : 18, 'gender' : 'M', 'strokeId' : freeId  , 'distance' : 200, 'units' : 'Y', 'isRelay' : True , 'timeEntered' : now, 'timeModified' : now},
    ]
    
    meetOnes = np.ones(len(meetIds), dtype=int)
    for event in events:
        curs.execute("""INSERT INTO swimapp_event (event_name, lower_age,""" \
        """ upper_age, gender, stroke_id, distance, distance_units, is_relay,""" \
        """ time_entered, time_modified) VALUES (%(name)s, %(lowerAge)s,""" \
        """ %(upperAge)s, %(gender)s, %(strokeId)s, %(distance)s, %(units)s,""" \
        """ %(isRelay)s, %(timeEntered)s, %(timeModified)s) RETURNING id;""",
        event)
        eventId = curs.fetchone()[0]
        
        data = zip(eventId * meetOnes, event['number'] * meetOnes, meetIds)
        curs.executemany("""INSERT INTO swimapp_meetevent (event_id, event_number,""" \
        """ meet_id) VALUES (%s,%s,%s);""", data)
        
except Exception as e:
    print "Failed to create events"
    print e
    sys.exit()
    
print "Events complete"

#try:
#    eventIds = []
#    for event in events:
#        curs.execute("""SELECT id FROM swimapp_event WHERE event_name = %s;""", (event['name'],))
#        eventIds.append(curs.fetchone()[0])
#    
#    for meetId in meetIds:
#        data = zip(meetId * np.ones(len(eventIds), dtype=int), eventIds)
#        curs.executemany("""INSERT INTO swimapp_meetevent (meet_id, event_id)""" \
#        """ VALUES (%s, %s);""", data);
#    
#except Exception as e:
#    print "Failed to create meet events"
#    print e
#    sys.exit()
#    
#print "Meet Events complete"

#========================================
#Entries
#========================================

#table
#   swimapp_entry
#columns
#   id                  (primary key, auto increment)
#   lane_number         (int)
#   result_time         (double)
#   seed_time           (double)
#   heat                (int)
#   meetevent_id        (int, not null)
#   time_entered        (timestamp, not null)
#   time_modified       (timestamp, not null)

#========================================
#Athlete Entries
#========================================

#table
#   swimapp_entry
#columns
#   id                  (primary key, auto increment)
#   athlete_id          (int, not null)
#   entry_id            (int, not null)
#   order               (int, not null)

ageGroups = [(0,8), (9,10), (11,12), (13,14), (15,18)]
genders = ['M','F']
strokeIds = [freeId, backId, breastId, flyId, medleyId]

#iterate through meets
for meetId in meetIds:
    print "\tMeet Id: " + str(meetId)
    #get meet age up and start date
    curs.execute("""SELECT age_up_date, start_date FROM swimapp_meet WHERE id = %s;""", (meetId,))
    ageUpDate, startDate = curs.fetchone()
    
    #iterate through teams in a given meet
    curs.execute("""SELECT team_id FROM swimapp_meet_teams WHERE meet_id = %s;""", (meetId,))
    meetTeamIds = curs.fetchall()
    
    for meetTeamId in meetTeamIds:
        print "\t\tTeam Id: " + str(meetTeamId[0])
        #iterate through athletes in a given team, randomly assign 2 individual events and 2 relays where possible
        
        for ageGroup in ageGroups:
            print "\t\t\tAge Group: " + str(ageGroup)          
            
            lowerAgeGroupDate = ageUpDate.replace(year = ageUpDate.year - ageGroup[0])
            upperAgeGroupDate = ageUpDate.replace(year = ageUpDate.year - ageGroup[1])
            
            for gender in genders:
                print "\t\t\t\tGender: " + gender
                
                curs.execute("""SELECT swimapp_athlete.* FROM swimapp_athlete_teams""" \
                """ JOIN swimapp_athlete ON swimapp_athlete_teams.athlete_id =""" \
                """ swimapp_athlete.id WHERE (swimapp_athlete_teams.team_id = %s)""" \
                """ AND (swimapp_athlete.date_of_birth < %s) AND (swimapp_athlete."""  \
                """ date_of_birth > %s) AND (swimapp_athlete.gender = %s);""",
                (meetTeamId[0], lowerAgeGroupDate, upperAgeGroupDate, gender))
                ageGroupAthletes = curs.fetchall()
                
                print "Age group athlete count: " + str(len(ageGroupAthletes))
                
                maxNumRelay = int(np.floor(len(ageGroupAthletes)/4))
                freeRelayAthletes = random.sample(ageGroupAthletes, maxNumRelay*4)
                medleyRelayAthletes = random.sample(ageGroupAthletes, maxNumRelay*4)
                
                #enter individual events
                for ageGroupAthlete in ageGroupAthletes:
                    print "Age group athlete id: " + str(ageGroupAthlete)
                    
                    #check if this athlete is in a free relay
                    try:
                        freeRelayAthletes.index(ageGroupAthlete)
                        inFreeRelay = True
                    except ValueError:
                        inFreeRelay = False
                    
                    #check if this athlete is in a medley relay
                    try:
                        medleyRelayAthletes.index(ageGroupAthlete)
                        inMedleyRelay = True
                    except ValueError:
                        inMedleyRelay = False
                    
                    numIndividualEvents = 2
                    if not inFreeRelay:
                        numIndividualEvents += 1
                    
                    if not inMedleyRelay:
                        numIndividualEvents += 1
                    
                    individualStrokeIds = random.sample(strokeIds, numIndividualEvents)
                    for individualStrokeId in individualStrokeIds:
                        print "Individual event id: " + str(individualStrokeId)
                        
                        #get event_id (needs to be changed to meetevent_id)
                        curs.execute("""SELECT swimapp_meetevent.id FROM""" \
                        """ swimapp_meetevent JOIN swimapp_event ON""" \
                        """ swimapp_meetevent.event_id = swimapp_event.id WHERE""" \
                        """ (lower_age = %s) AND (upper_age = %s) AND""" \
                        """ (gender = %s) AND (stroke_id = %s) AND (is_relay = %s);""",
                        (ageGroup[0], ageGroup[1], gender, individualStrokeId, False))
                        meeteventId = curs.fetchone()[0]
                        
                        print "MeetEvent id: " + str(meeteventId)
                        
                        curs.execute("""INSERT INTO swimapp_entry (meetevent_id,""" \
                        """ time_entered, time_modified) VALUES (%s,%s,%s)""" \
                        """ RETURNING id;""", (meeteventId, now, now))
                        entryId = curs.fetchone()[0]
                        
                        print "Entry id: " + str(entryId)
                        
                        curs.execute("""INSERT INTO swimapp_athleteentry""" \
                        """ (athlete_id, entry_id, athlete_order) VALUES (%s,%s,%s);""",
                        (ageGroupAthlete[0], entryId, 1))
                
                #enter relay events
                
                #get free relay event id
                curs.execute("""SELECT swimapp_meetevent.id FROM swimapp_meetevent""" \
                """ JOIN swimapp_event ON swimapp_meetevent.event_id = swimapp_event.id""" \
                """ WHERE (lower_age = %s) AND (upper_age = %s) AND (gender = %s)""" \
                """ AND (stroke_id = %s) AND (is_relay = %s);""", (ageGroup[0], ageGroup[1], gender, freeId, True))
                freeRelayMeetEventId = curs.fetchone()[0]                
                
                for i in range(maxNumRelay):
                    freeRelay = freeRelayAthletes[i:i+4]
                    
                    curs.execute("""INSERT INTO swimapp_entry (meetevent_id,""" \
                    """ time_entered, time_modified) VALUES (%s,%s,%s)""" \
                    """ RETURNING id;""", (freeRelayMeetEventId, now, now))
                    freeRelayEntryId = curs.fetchone()[0]
                    
                    for j in range(4):
                        curs.execute("""INSERT INTO swimapp_athleteentry""" \
                        """ (athlete_id, entry_id, athlete_order) VALUES (%s,%s,%s);""",
                        (freeRelay[j][0], freeRelayEntryId, j))
                
                #get medley relay event id
                curs.execute("""SELECT swimapp_meetevent.id FROM swimapp_meetevent""" \
                """ JOIN swimapp_event ON swimapp_meetevent.event_id = swimapp_event.id""" \
                """ WHERE (lower_age = %s) AND (upper_age = %s) AND (gender = %s)""" \
                """ AND (stroke_id = %s) AND (is_relay = %s);""", (ageGroup[0], ageGroup[1], gender, medleyId, True))
                medleyRelayMeetEventId = curs.fetchone()[0]                
                
                for i in range(maxNumRelay):
                    medleyRelay = medleyRelayAthletes[i:i+4]
                    
                    curs.execute("""INSERT INTO swimapp_entry (meetevent_id,""" \
                    """ time_entered, time_modified) VALUES (%s,%s,%s)""" \
                    """ RETURNING id;""", (medleyRelayMeetEventId, now, now))
                    medleyRelayEntryId = curs.fetchone()[0]
                    
                    for j in range(4):
                        curs.execute("""INSERT INTO swimapp_athleteentry""" \
                        """ (athlete_id, entry_id, athlete_order) VALUES (%s,%s,%s);""", \
                        (medleyRelay[j][0], medleyRelayEntryId, j))

conn.commit()
conn.close()