
from ..types import EventType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder

from ..EventParser import EventParser

from .AEvent import string
from .AEventAdvanced import AEventAdvanced
from .AEventBase import AEventBase

class AEventAdvancedSpell(AEventAdvanced):
    def __init__(self, time, eventType, parser):
        AEventBase.__init__(self, time, eventType, parser)

        if isinstance(parser, EventParser):
            # Prefix Parameters are inbetween Base and Advanced Parameters
            # e.g.: 11682,"Hellfire Effect",0x4
            self.spellId = parser.getInt()
            self.spellName = parser.getString()
            self.spellSchool = parser.getInt(base=16)
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))
        
        AEventAdvanced.__init__(self, parser)

    def decode(self, decoder: ADecoder):
        self.spellId, self.spellName, self.spellSchool = decoder.spell()

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBase.encode(self, encoder) + \
               encoder.spell(self.spellId, self.spellName, self.spellSchool) + \
               AEventAdvanced.encode(self, encoder)

    def __str__(self):
        return AEventBase.__str__(self) + ',{0:d},{1:s},{2:#x}'.format(
            self.spellId,
            string(self.spellName),
            self.spellSchool
        ) + AEventAdvanced.__str__(self)

    def __eq__(self, other):
        return AEventAdvanced.__eq__(self, other) and self.spellId == other.spellId

    def __ne__(self, other):
        return not self.__eq__(other)


