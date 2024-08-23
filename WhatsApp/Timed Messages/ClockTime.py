from datetime import datetime


class ClockTime:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0, microsecond: int = 0) -> None:
        if hour < 0 or minute < 0 or second < 0 or microsecond < 0:
            raise ValueError('Time can NOT be in negative!')

        # limit parameters to correct ranges
        self.hour = hour % 24
        self.second = second % 60
        self.minute = minute % 60
        self.microsecond = microsecond % 1000000

    def to_datetime(self):
        return datetime.now().replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond)

    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second + self.microsecond / 1000000

    def to_string(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"