from .Event import Event
from .EventType import EventType
from .EventParser import EventParser
from .EventParser import EventParsingError

# 1/22 19:26:49.388  COMBAT_LOG_VERSION,9,ADVANCED_LOG_ENABLED,1,BUILD_VERSION,1.13.3,PROJECT_ID,2

class EventCombatLogVersion(Event):
    def __init__(self, time, parser: EventParser):
        Event.__init__(self, time)
        self.version = parser.getInt()
        if parser.readValue() != 'ADVANCED_LOG_ENABLED':
            raise EventParsingError('Field missing: ADVANCED_LOG_ENABLED')
        self.advancedLogEnabled = parser.readValue() == '1'
        if parser.readValue() != 'BUILD_VERSION':
            raise EventParsingError('Field missing: BUILD_VERSION')
        self.build = parser.readValue()
        if parser.readValue() != 'PROJECT_ID':
            raise EventParsingError('Field missing: PROJECT_ID')
        self.projectId = parser.getInt()

    def getEventType(self) -> EventType:
        return EventType.COMBAT_LOG_VERSION

    def __str__(self):
        return Event.__str__(self) + ',{0:d},ADVANCED_LOG_ENABLED,{1:s},BUILD_VERSION,{2:s},PROJECT_ID,{3:d}'.format(
            self.version,
            '1' if self.advancedLogEnabled else '0',
            self.build,
            self.projectId
        )
    
    def __eq__(self, other):
        return Event.__eq__(self, other) and \
               self.version == other.version and \
               self.advancedLogEnabled == other.advancedLogEnabled and \
               self.build == other.build and \
               self.projectId == other.projectId

    def __ne__(self, other):
        return not self.__eq__(other)
