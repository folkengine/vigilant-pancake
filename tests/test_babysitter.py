import pytest
import datetime

import babysitter


class TestBabySitter:

    billable_start_time = datetime.time(17, 0)

    on_times = [
        billable_start_time, datetime.time(17, 1), datetime.time(17, 29), datetime.time(18, 29)
    ]

    @pytest.mark.parametrize("start", on_times)
    def test_babysitter_starttime_ontime(self, start):
        doubtfire = babysitter.BabySitter(start)

        assert doubtfire.start_time == start

    early_times = [
        datetime.time(16, 59), datetime.time(16, 29)
    ]

    @pytest.mark.parametrize("start", early_times)
    def test_babysitter_starttime_early(self, start):
        doubtfire = babysitter.BabySitter(start)

        assert doubtfire.start_time == self.billable_start_time
