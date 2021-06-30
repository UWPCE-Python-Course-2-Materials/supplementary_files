
import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

print(f"before mock datetime.datetime is {type(datetime.datetime)}")

# Mock datetime to control today's date
datetime = Mock()
print(f"after mock datetime.datetime is {type(datetime.datetime)}")


def is_weekday():
    # this next line uses the mocked return value set on lines 24 then 30
    today = datetime.datetime.today()
    print(f"in is_weekday() datetime.datetime is {type(datetime.datetime)}")
    print("here are its properties:")
    print(dir(today))
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday

# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday

datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()
