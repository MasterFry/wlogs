from wlog2.encode import ADecoder

TIME_EPSILON_INIT = 5000
TIME_EPSILON_CMP_ENCOUNTER = 10000
TIME_EPSILON = TIME_EPSILON_INIT

# month 12     -> 4b
# day 31       -> 5b
# hour 24      -> 5b
# minute 60    -> 6b
# second 60000 -> 16b
#              -> + = 36 -> 40b = 5B
# 12 * 31 * 24 * 60 * 60000

class Time:
    def __init__(self, params):
        if isinstance(params, list):
            self.month  = int(params[0])
            self.day    = int(params[1])
            self.hour   = int(params[2])
            self.minute = int(params[3])
            self.second = float(params[4])
            self.time   = int(self.second * 1000) + 60000 * (self.minute + 60 * self.hour)
        elif isinstance(params, ADecoder):
            self.decode(params)
        else:
            raise ValueError('Invalid argument for Time.__init__(params): ' + str(params))

    def decode(self, decoder):
        time = int.from_bytes(decoder.read(5), byteorder='little')
        self.time = time % (24 * 60 * 60000)
        stime = self.time
        time //= 24 * 60 * 60000
        self.second = float(stime % 60000) / 1000
        stime //= 60000
        self.minute = stime % 60
        self.hour = (stime // 60) % 60
        self.day = time % 31
        self.month = time // 31

    def encode(self) -> bytes:
        t = (self.month * 31 + self.day) * 24 * 60 * 60000 + self.time
        return t.to_bytes(length=5, byteorder='little')

    def __lt__(self, other):
        assert(isinstance(other, Time))
        if self.month == other.month:
            if self.day == other.day:
                return self.time < other.time - TIME_EPSILON
            return self.day < other.day
        return self.month < other.month
    
    def __le__(self, other):
        assert(isinstance(other, Time))
        if self.month == other.month:
            if self.day == other.day:
                return self.time < other.time + TIME_EPSILON
            return self.day < other.day
        return self.month < other.month

    def __eq__(self, other):
        assert(isinstance(other, Time))
        return self.month == other.month and \
               self.day == other.day and \
               abs(self.time - other.time) < TIME_EPSILON

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        assert(isinstance(other, Time))
        if self.month == other.month:
            if self.day == other.day:
                return self.time > other.time - TIME_EPSILON
            return self.day > other.day
        return self.month > other.month

    def __gt__(self, other):
        assert(isinstance(other, Time))
        if self.month == other.month:
            if self.day == other.day:
                return self.time > other.time + TIME_EPSILON
            return self.day > other.day
        return self.month > other.month


    def __add__(self, other):
        if isinstance(other, Time):
            return Time([
                self.month + other.month,
                self.day + other.day,
                self.hour + other.hour,
                self.minute + other.minute,
                self.second + other.second
            ])
        elif isinstance(other, float) or isinstance(other, int):
            second = self.second + float(other) / 1000
            minute = self.minute + second // 60
            hour = self.hour + minute // 60
            assert(hour < 24 and "day overflow not supported when adding time")
            return Time([
                self.month,
                self.day,
                hour,
                minute % 60,
                second % 60 # TODO check % with float
            ])
        assert(False)

    def __sub__(self, other):
        if isinstance(other, Time):
            return Time([
                self.month - other.month,
                self.day - other.day,
                self.hour - other.hour,
                self.minute - other.minute,
                self.second - other.second
            ])
        elif isinstance(other, float) or isinstance(other, int):
            second = self.second - float(other) / 1000
            minute = self.minute - second // 60
            hour = self.hour - minute // 60
            assert(hour >= 0 and "day underflow not supported when adding time")
            return Time([
                self.month,
                self.day,
                hour,
                minute % 60,
                second % 60 # TODO check % with float
            ])
        assert(False)

    def __str__(self):
        return '%d/%d %02d:%02d:%06.03f' % (self.month, self.day, self.hour, self.minute, self.second)

    @staticmethod
    def resetEpsilon():
        global TIME_EPSILON
        global TIME_EPSILON_INIT
        TIME_EPSILON = TIME_EPSILON_INIT
        
    @staticmethod
    def setEpsilon(epsilon):
        global TIME_EPSILON
        TIME_EPSILON = epsilon
