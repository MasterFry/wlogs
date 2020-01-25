#pragma once

#include "stdint.h"

#define UNITFLAG_TYPE_OBJECT          0x10
#define UNITFLAG_TYPE_GUARDIAN        0x08
#define UNITFLAG_TYPE_PET             0x04
#define UNITFLAG_TYPE_NPC             0x02
#define UNITFLAG_TYPE_PLAYER          0x01

#define UNITFLAG_CONTROL_NPC          0x2
#define UNITFLAG_CONTROL_PLAYER       0x1

#define UNITFLAG_REACTION_HOSTILE     0x4
#define UNITFLAG_REACTION_NEUTRAL     0x2
#define UNITFLAG_REACTION_FRIENDLY    0x1

#define UNITFLAG_AFFILIATION_OUTSIDER 0x8
#define UNITFLAG_AFFILIATION_RAID     0x4
#define UNITFLAG_AFFILIATION_PARTY    0x2
#define UNITFLAG_AFFILIATION_MINE     0x1

#define UNITFLAG_SPECIAL_NONE         0x8000
#define UNITFLAG_SPECIAL_RAIDTARGET8  0x0800
#define UNITFLAG_SPECIAL_RAIDTARGET7  0x0400
#define UNITFLAG_SPECIAL_RAIDTARGET6  0x0200
#define UNITFLAG_SPECIAL_RAIDTARGET5  0x0100
#define UNITFLAG_SPECIAL_RAIDTARGET4  0x0080
#define UNITFLAG_SPECIAL_RAIDTARGET3  0x0040
#define UNITFLAG_SPECIAL_RAIDTARGET2  0x0020
#define UNITFLAG_SPECIAL_RAIDTARGET1  0x0010
#define UNITFLAG_SPECIAL_MAINASSIST   0x0008
#define UNITFLAG_SPECIAL_MAINTANK     0x0004
#define UNITFLAG_SPECIAL_FOCUS        0x0002
#define UNITFLAG_SPECIAL_TARGET       0x0001

typedef struct __unitflag_t__
{
  uint32_t special     :16;
  uint32_t type        :6;
  uint32_t controller  :2;
  uint32_t reaction    :4;
  uint32_t affiliation :4;
} __attribute__((__packed__)) unitflag_t;

inline bool operator==(const struct __unitflag_t__& self, const struct __unitflag_t__& other)
{
  return *((uint32_t*) &self) == *((uint32_t*) &other);
}

inline bool operator!=(const struct __unitflag_t__& self, const struct __unitflag_t__& other)
{
  return *((uint32_t*) &self) != *((uint32_t*) &other);
}