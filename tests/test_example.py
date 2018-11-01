#!coding:utf-8

from sys import path as sys_path
from os import path as os_path
import subprocess

import pytest

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), "../")))
import autoargparse


@pytest.mark.example
@pytest.mark.parametrize(
    "input,expected",
    [
        ("python ./example/calculator.py 1", ["!!!"]),
        ("python ./example/calculator.py 2", ["Great !!!"]),
        ("python ./example/calculator.py 1 -m 2 3", ["!!!", "6"]),
        ("python ./example/calculator.py 1 -m 2 3 -v", ["!!!", "a * b = 6"]),
        (
            "python ./example/calculator.py 1 -m 2 3 -vv",
            ["!!!", "func = mul args = 2 3 2", "a * b = 6"],
        ),
        ("python ./example/calculator.py 1 -s 1 2 3 4", ["!!!", "10"]),
        ("python ./example/calculator.py 1 -s 1 2 3 4 --max", ["!!!", "4"]),
        ("python ./example/calculator.py 1 -s 1 2 3 4 --negative", ["!!!", "-10"]),
    ],
)
def test_example(input, expected):
    obj = subprocess.Popen(
        input.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = obj.communicate()

    assert out.decode('utf-8').splitlines() == expected
