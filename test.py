#!/usr/bin/env python3

PARAM_COUNT = {
    'DAMAGE_SHIELD'           : 43 ,
    'DAMAGE_SHIELD_MISSED'    : 20 ,
    'DAMAGE_SPLIT'            : 43 ,
    'ENCHANT_APPLIED'         : 17 ,
    'ENCHANT_REMOVED'         : 17 ,
    'ENVIRONMENTAL_DAMAGE'    : 41 ,
    'PARTY_KILL'              : 14 ,
    'RANGE_DAMAGE'            : 43 ,
    'RANGE_MISSED'            : 20 ,
    'SPELL_ABSORBED'          : 26 ,
    'SPELL_AURA_APPLIED'      : 18 ,
    'SPELL_AURA_APPLIED_DOSE' : 19 ,
    'SPELL_AURA_BROKEN'       : 18 ,
    'SPELL_AURA_BROKEN_SPELL' : 21 ,
    'SPELL_AURA_REFRESH'      : 18 ,
    'SPELL_AURA_REMOVED'      : 18 ,
    'SPELL_AURA_REMOVED_DOSE' : 19 ,
    'SPELL_CAST_FAILED'       : 18 ,
    'SPELL_CAST_START'        : 17 ,
    'SPELL_CAST_SUCCESS'      : 33 ,
    'SPELL_CREATE'            : 17 ,
    'SPELL_DAMAGE'            : 43 ,
    'SPELL_DURABILITY_DAMAGE' : 19 ,
    'SPELL_DISPEL'            : 21 ,
    'SPELL_DRAIN'             : 37 ,
    'SPELL_ENERGIZE'          : 37 ,
    'SPELL_EXTRA_ATTACKS'     : 18 ,
    'SPELL_HEAL'              : 38 ,
    'SPELL_INSTAKILL'         : 17 ,
    'SPELL_INTERRUPT'         : 20 ,
    'SPELL_MISSED'            : 20 ,
    'SPELL_PERIODIC_DAMAGE'   : 43 ,
    'SPELL_PERIODIC_DRAIN'    : 37 ,
    'SPELL_PERIODIC_ENERGIZE' : 37 ,
    'SPELL_PERIODIC_HEAL'     : 38 ,
    'SPELL_PERIODIC_LEECH'    : 37 ,
    'SPELL_PERIODIC_MISSED'   : 19 ,
    'SPELL_RESURRECT'         : 17 ,
    'SPELL_SUMMON'            : 17 ,
    'SWING_DAMAGE'            : 40 ,
    'SWING_DAMAGE_LANDED'     : 40 ,
    'SWING_MISSED'            : 16 ,
    'UNIT_DIED'               : 14 ,
    'UNIT_LOYALTY'            : 15 
}

BASE_TEMPLATE = """from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventParser import EventParser

class Event{0:s}(EventBase):
    def __init__(self, time, parser: EventParser):
        EventBase.__init__(self, time)

    def getEventType(self) -> EventType:
        return EventType.{1:s}

    def __str__(self):
        return EventBase.__str__(self) +

    def __eq__(self, other):
        return EventBase.__eq__(other) and \

    def __ne__(self, other):
        return not self.__eq__(other)

"""

ADV_TEMPLATE = """from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventAdvanced import EventAdvanced
from .EventParser import EventParser

class {0:s}(EventAdvanced):
    def __init__(self, time, parser: EventParser):
        EventBase.__init__(self, time)
        EventAdvanced.__init__(self, time)

    def getEventType(self) -> EventType:
        return EventType.{1:s}

    def __str__(self):
        return EventBase.__str__(self) + EventAdvanced.__str__(self)

    def __eq__(self, other):
        return EventAdvanced.__eq__(other) and \

    def __ne__(self, other):
        return not self.__eq__(other)

"""

def getClassName(event: str):
    return 'Event' + ''.join([x.capitalize() for x in event.split('_')])

# self.has_advanced_params = PARAM_COUNT[self.event] >= 31
for event in PARAM_COUNT:
    className = getClassName(event)
    with open('te/%s.py' % className, 'w') as file:
        if PARAM_COUNT[event] >= 32:
            file.write(ADV_TEMPLATE.format(className, event))
        else:
            file.write(BASE_TEMPLATE.format(className, event))
