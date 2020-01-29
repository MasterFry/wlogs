from abc import ABC

from ..types import EventType
from ..types import MissType
from ..types import getMissTypeName
from ..encode import AEncoder, ADecoder, SizeType

from ..EventParser import EventParser

class A2EventMissed(ABC):
    def __init__(self, eventType, parser):
        assert(
            eventType == EventType.SWING_MISSED          or \
            eventType == EventType.RANGE_MISSED          or \
            eventType == EventType.SPELL_MISSED          or \
            eventType == EventType.SPELL_PERIODIC_MISSED or \
            eventType == EventType.DAMAGE_SHIELD_MISSED
        )
        if isinstance(parser, EventParser):
            self.missType = parser.getMissType()
            self.isOffHand = parser.readValue() == '1'

            if self.missType == MissType.ABSORB:
                self.amountMissed = parser.getInt()
                self.critical = parser.getInt()

            elif self.missType == MissType.RESIST or \
                self.missType == MissType.BLOCK:
                self.amountMissed = parser.getInt()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.missType = decoder.missType()
        self.isOffHand = decoder.boolean()
        
        if self.missType == MissType.ABSORB:
            self.amountMissed = decoder.integer(size=SizeType.MISSED_AMOUNT)
            self.critical = decoder.integer(size=SizeType.MISSED_CRITICAL)

        elif self.missType == MissType.RESIST or \
             self.missType == MissType.BLOCK:
            self.amountMissed = decoder.integer(size=SizeType.MISSED_AMOUNT)

    def encode(self, encoder: AEncoder) -> bytes:
        if self.missType == MissType.ABSORB:
            return encoder.missType(self.missType) + \
                   encoder.boolean(self.isOffHand) + \
                   encoder.integer(self.amountMissed, size=SizeType.MISSED_AMOUNT) + \
                   encoder.integer(self.critical, size=SizeType.MISSED_CRITICAL)

        elif self.missType == MissType.RESIST or \
             self.missType == MissType.BLOCK:
            return encoder.missType(self.missType) + \
                   encoder.boolean(self.isOffHand) + \
                   encoder.integer(self.amountMissed, size=SizeType.MISSED_AMOUNT)

        else:
            return encoder.missType(self.missType) + \
                   encoder.boolean(self.isOffHand)

    def __str__(self):
        if self.missType == MissType.ABSORB:
            return ',{0:s},{1:s},{2:d},{3:d}'.format(
                getMissTypeName(self.missType),
                '1' if self.isOffHand else 'nil',
                self.amountMissed,
                self.critical
            )
        elif self.missType == MissType.RESIST or \
             self.missType == MissType.BLOCK:
            return ',{0:s},{1:s},{2:d}'.format(
                getMissTypeName(self.missType),
                '1' if self.isOffHand else 'nil',
                self.amountMissed
            )
        else:
            return ',{0:s},{1:s}'.format(
                getMissTypeName(self.missType),
                '1' if self.isOffHand else 'nil'
            )

    def __eq__(self, other):
        if self.missType != other.missType:
            return False

        if self.missType == MissType.ABSORB:
            return self.amountMissed == other.amountMissed and \
                   self.critical == other.critical

        elif self.missType == MissType.RESIST or \
             self.missType == MissType.BLOCK:
            return self.amountMissed == other.amountMissed

        return True
        
    def __ne__(self, other):
        return not self.__eq__(other)

