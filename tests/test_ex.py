# in test_users.py
import pytest


def fake_get_user_data(username, passwprd):
    return [["andy", "xyz"], "fred", "abc"]


@pytest.fixture
def patch_get(monkeypatch):
    from project.lessons.lesson01.extras import users
    monkeypatch.setattr(users, 'get_user_data', fake_get_user_data)


def test_get_user_data(patch_get):
    from project.lessons.lesson01.extras.users import get_user_data
    assert get_user_data('andy', 'mypw') == [["andy", "xyz"], "fred", "abc"]
