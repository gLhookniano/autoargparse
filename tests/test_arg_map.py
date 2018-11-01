#!coding:utf-8

from sys import path as sys_path
from os import path as os_path
import copy

import pytest

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), "../")))
import autoargparse


l_args = [
    {"name": "asdf", "fun": 1, "foo": 34},
    {"name": "fdas", "fun": 2, "foo": 78},
    {"name": "zxcv", "boo": 3, "hoo": 88},
]


@pytest.fixture(scope="function")
def map():
    m = autoargparse.arg_map().set_all(l_args)
    yield copy.deepcopy(m)
    del m


def test_argMap_set():
    m1 = autoargparse.arg_map().set(**l_args[0])
    assert m1.map[0] == l_args[0]
    del m1


def test_argMap_setAll_function(map):
    assert map.map == l_args


def test_argMap_setAll_property():
    m2 = autoargparse.arg_map()
    m2.map = l_args
    assert m2.map == l_args
    del m2


def test_argMap_search(map):
    assert map.search("boo")[0] == l_args[2]


def test_argMap_searchLeaf(map):
    assert map.search_leaf(88)[0] == l_args[2]


def test_argMap_get_no_value_no_boolFunc(map):
    assert map.get() == l_args


def test_argMap_get_has_value_no_boolFunc(map):
    assert map.get("name", "asdf")[0] == l_args[0]


def test_argMap_get_no_value_has_boolFunc(map):
    assert (
        map.get("name", boolFunc=lambda x: "hoo" in x and x["hoo"] == 88)[0]
        == l_args[2]
    )


def test_argMap_get_has_value_has_boolFunc(map):
    assert (
        map.get("name", "asdf", boolFunc=lambda x: "hoo" in x and x["hoo"] == 88) == []
    )


def test_argMap_getLeaf_key(map):
    assert map.get_leaf("name") == [["asdf", 1, 34], ["fdas", 2, 78], ["zxcv", 3, 88]]


def test_argMap_getLeaf_key_value(map):
    assert map.get_leaf("name", "asdf") == [["asdf", 1, 34]]


def test_argMap_getLeaf_leaf(map):
    assert map.get_leaf(leaf="foo") == [34, 78]


def test_argMap_getLeaf_key_leaf(map):
    assert map.get_leaf("name", leaf="hoo") == [88]


def test_argMap_getLeaf_key_value_leaf(map):
    assert map.get_leaf("name", "asdf", leaf="foo") == [34]


def test_argMap_add_to_exist(map):
    assert map.add("name", "asdf", "coo", 11).map[0] == {
        "name": "asdf",
        "fun": 1,
        "foo": 34,
        "coo": 11,
    }


def test_argMap_changeType(map):
    assert map.change_type("name", "asdf", "foo", str).map[0] == {
        "name": "asdf",
        "fun": 1,
        "foo": "34",
    }


def test_argMap_sort(map):
    assert map.sort(key=lambda x: x["name"])[0] == {"name": "asdf", "fun": 1, "foo": 34}
    assert map.sort(key=lambda x: x["name"], reverse=True)[0] == {
        "name": "zxcv",
        "boo": 3,
        "hoo": 88,
    }
