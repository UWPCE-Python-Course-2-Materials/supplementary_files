import os


def rm(filename):
    os.remove(filename)


def test_rm(mocker):
    mocker.patch("os.remove")
    rm("file")
    os.remove.assert_called_once_with('file')
