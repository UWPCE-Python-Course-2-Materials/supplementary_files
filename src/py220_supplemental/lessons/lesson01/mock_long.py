import py220_supplemental.lessons.lesson01.sut as sut


def test_big_long_func(mocker):
    mocker.patch("py220_supplemental.lessons.lesson01.sut"
                 ".big_long_func", return_value=True)
    done = sut.do_something()
    assert sut.do_something() is True
