#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pysia
----------------------------------

Tests for `pysia` module.
"""

import pytest

@pytest.fixture
def sia():
    from pysia import Sia
    return Sia()

def test_basic_methods_exist(sia):
    assert (hasattr(sia, 'get_consensus')), "A sia client should have a get_consensus method."
