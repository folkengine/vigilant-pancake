import pytest
import datetime


class TestBabySitter:

    def test_babysitter_starttime_ontime(self):
        start_time = datetime.time(17,0)
        babysitter = babysitter.BabySitter(start_time)

        assert babysitter.start_time == start_time
