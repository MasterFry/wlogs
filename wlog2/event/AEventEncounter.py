
from ..types import EventType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder
from ..encode.SizeType import SizeType

from ..EventParser import EventParser

from .AEvent import AEvent
from .AEvent import string

# 1/22 19:39:52.829  ENCOUNTER_START,663,"Lucifron",9,40,409
# 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class AEventEncounter(AEvent):
    def __init__(self, time, eventType, parser):
        AEvent.__init__(self, time, eventType)
        
        if isinstance(parser, EventParser):
            self.encounterId = parser.getInt()
            self.encounterName = parser.getString()
            self.difficultyId = parser.getInt()
            self.playerCount = parser.getInt()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.encounterId = decoder.integer(size=SizeType.ENCOUNTER_ID)
        self.encounterName = decoder.string()
        self.difficultyId = decoder.integer(size=SizeType.DIFFICULTY_ID)
        self.playerCount = decoder.integer(size=SizeType.PLAYER_COUNT)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEvent.encode(self, encoder) + \
               encoder.integer(self.encounterId, size=SizeType.ENCOUNTER_ID) + \
               encoder.string(self.encounterName) + \
               encoder.integer(self.difficultyId, size=SizeType.DIFFICULTY_ID) + \
               encoder.integer(self.playerCount, size=SizeType.PLAYER_COUNT)

    def __str__(self):
        return AEvent.__str__(self) + ',{0:d},{1:s},{2:d},{3:d}'.format(
            self.encounterId,
            string(self.encounterName),
            self.difficultyId,
            self.playerCount
        )

    def __eq__(self, other):
        return AEvent.__eq__(self, other) and \
               self.encounterId == other.encounterId and \
               self.difficultyId == other.difficultyId and \
               self.playerCount == other.playerCount

    def __ne__(self, other):
        return not self.__eq__(other)