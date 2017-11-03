import pytest
import datetime

import babysitter

class TestBabySitter:

    def test_babysitter_starttime_ontime(self):
        start_time = datetime.time(17,0)
        doubtfire = babysitter.BabySitter(start_time)

        assert doubtfire.start_time == start_time
