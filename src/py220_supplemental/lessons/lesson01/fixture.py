#!/USr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def supplied_test_data():
    return {
        'aa': 25,
        'bb': 35,
        'cc': 45,
    }


def test_compare_with_aa(supplied_test_data):
    assert supplied_test_data["aa"] != 35, "aa and zz failed"


def test_compare_with_bb(supplied_test_data):
    assert supplied_test_data["bb"] == 35, "bb and zz comparison failed"


def test_compare_with_cc(supplied_test_data):
    assert supplied_test_data["cc"] != 35, "cc and zz comparison failed"
