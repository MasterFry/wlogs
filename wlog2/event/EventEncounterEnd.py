
from ..types import EventType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder

from ..EventParser import EventParser

from .AEventEncounter import AEventEncounter

# 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class EventEncounterEnd(AEventEncounter):
    def __init__(self, time, parser):
        AEventEncounter.__init__(self, time, EventType.ENCOUNTER_END, parser)
        
        if isinstance(parser, EventParser):
            self.success = True if parser.readValue() == '1' else False
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.success = decoder.boolean()

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventEncounter.encode(self, encoder) + encoder.boolean(self.success)

    def getEventType(self) -> EventType:
        return EventType.ENCOUNTER_END

    def __str__(self):
        return AEventEncounter.__str__(self) + (',1' if self.success else ',0')

    def __eq__(self, other):
        return AEventEncounter.__eq__(other) and \
               self.success == other.success

    def __ne__(self, other):
        return not self.__eq__(other)