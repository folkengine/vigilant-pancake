import datetime

class BabySitter():
    earliest_billable_start_time = datetime.time(17, 0)

    def __init__(self, start_time):
        self.start_time = max(start_time, self.earliest_billable_start_time)

