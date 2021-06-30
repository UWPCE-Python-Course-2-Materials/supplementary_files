# pytest -v test_mark.py -m dicttest

import pytest


@pytest.mark.dicttest
def test_something():
    a = ["a", "b"]
    assert a == a


def test_something_else():
    assert False


"""pytest-xdist
can use auto instaed of number
--numprocesses 4
"""


@pytest.fixture
def database():
    db = "<some database connection>"
    yield db
    db.close()


def test_insert(database):
    database.insert(123)


# autouse
import os
import pytest


@pytest.fixture(autouse=True)
def change_user_env():
    curuser = os.environ.get("USER")
    os.environ["USER"] = "xyz"
    yield
    os.environ["USER"] = curuser


def test_user():
    assert os.getenv("USER") == "xyz"
