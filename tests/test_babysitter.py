import pytest
import datetime

import babysitter


class TestBabySitter:

    earliest_billable_start_time = datetime.time(17, 0)

    on_times = [
        earliest_billable_start_time,
        datetime.time(17, 1),
        datetime.time(17, 29),
        datetime.time(18, 29),
    ]

    @pytest.mark.parametrize("start_time", on_times)
    def test_babysitter_starttime_ontime(self, start_time):
        doubtfire = babysitter.BabySitter(start_time)

        assert doubtfire.start_time == start_time

    early_times = [
        datetime.time(16, 59),
        datetime.time(16, 29),
    ]

    @pytest.mark.parametrize("start_time", early_times)
    def test_babysitter_starttime_early(self, start_time):
        doubtfire = babysitter.BabySitter(start_time)

        assert doubtfire.start_time == self.earliest_billable_start_time
