
#include "events.h"

void A2EventMissed::write(FILE* file)
{
  if(this->missType == MissType::ABSORB)
  {
    fprintf(file, ",%s,%s,%d,%d",
      getCName(this->missType),
      this->isOffHand ? "1" : "nil",
      this->amountMissed,
      this->critical
    );
  }
  else if(this->missType == MissType::RESIST || this->missType == MissType::BLOCK)
  {
    fprintf(file, ",%s,%s,%d",
      getCName(this->missType),
      this->isOffHand ? "1" : "nil",
      this->amountMissed
    );
  }
  else
  {
    fprintf(file, ",%s,%s",
      getCName(this->missType),
      this->isOffHand ? "1" : "nil"
    );
  }
}
