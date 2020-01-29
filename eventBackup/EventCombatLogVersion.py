from .AEvent import AEvent
from ..EventType import EventType
from ..EventParser import EventParser
from ..EventParser import EventParsingError
from ..Encode import SizeType

# 1/22 19:26:49.388  COMBAT_LOG_VERSION,9,ADVANCED_LOG_ENABLED,1,BUILD_VERSION,1.13.3,PROJECT_ID,2

class EventCombatLogVersion(AEvent):
    def __init__(self, time, parser: EventParser):
        AEvent.__init__(self, time, EventType.COMBAT_LOG_VERSION)
        
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

    def encode(self, encoder) -> bytes:
        return AEvent.encode(encoder) + \
               encoder.integer(self.version, size=SizeType.COMBATLOG_VERSION) + \
               encoder.boolean(self.advancedLogEnabled) + \
               encoder.string(self.build) + \
               encoder.integer(self.projectId, size=SizeType.COMBATLOG_PROJECT_ID)

    def __str__(self):
        return AEvent.__str__(self) + ',{0:d},ADVANCED_LOG_ENABLED,{1:s},BUILD_VERSION,{2:s},PROJECT_ID,{3:d}'.format(
            self.version,
            '1' if self.advancedLogEnabled else '0',
            self.build,
            self.projectId
        )
    
    def __eq__(self, other):
        return AEvent.__eq__(self, other) and \
               self.version == other.version and \
               self.advancedLogEnabled == other.advancedLogEnabled and \
               self.build == other.build and \
               self.projectId == other.projectId

    def __ne__(self, other):
        return not self.__eq__(other)
