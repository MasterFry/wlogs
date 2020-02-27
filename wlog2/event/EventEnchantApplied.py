
from ..types import EventType
from ..encode.AEncoder import AEncoder

from ..EventParser import EventParser

from .A2EventEnchant import A2EventEnchant
from .AEventBase import AEventBase

# 2/24 20:25:53.313  ENCHANT_APPLIED,Player-4701-0171E041,"Relay-Mograine",0x511,0x0,Player-4701-0171E041,"Relay-Mograine",0x511,0x0,"Instant Poison VI",24222,"The Shadowfoot Stabber"

class EventEnchantApplied(AEventBase, A2EventEnchant):
    def __init__(self, time, parser):
        AEventBase.__init__(self, time, EventType.ENCHANT_APPLIED, parser)
        A2EventEnchant.__init__(self, EventType.ENCHANT_APPLIED, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBase.encode(self, encoder) + A2EventEnchant.encode(self, encoder)

    def __str__(self):
        return AEventBase.__str__(self) + A2EventEnchant.__str__(self)

    def __eq__(self, other):
        return AEventBase.__eq__(self, other) and A2EventEnchant.__eq__(self, other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

