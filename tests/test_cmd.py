#!coding:utf-8

from sys import path as sys_path
from os import path as os_path
import subprocess

import pytest

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), "../")))
import autoargparse


@pytest.mark.inner
@pytest.mark.parametrize(
    "input,stdin,expected",
    [
        ("python ./cmd_inner_function.py 1 -b 2", "func_args", "[1, '2', False]"),
        (
            "python ./cmd_inner_function.py 1 -b 2 -c -d 3 4",
            "cmd_args",
            "{'a': '1', 'b': '2', 'c': True, 'd': [3, 4]}",
        ),
        (
            "python ./cmd_inner_function.py 1 -b 2 -c -d 3 4",
            "func_args",
            "[1, '2', True, 3, 4]",
        ),
    ],
)
def test_cmd_inner_function(input, stdin, expected):
    obj = subprocess.Popen(
        input.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        cwd="./tests",
    )
    obj.stdin.writelines(stdin)
    out, err = obj.communicate()

    # [6:-7] hide 'debug>'
    assert out.strip()[6:-7] == expected


@pytest.mark.cmd
@pytest.mark.parametrize(
    "input,expected",
    [
        ("python ./cmd_no_deco_use.py 1 2 3 4", "4"),
        ("python ./cmd_no_deco_use.py --sum 1 2 3 4", "10"),
    ],
)
def test_cmd_no_deco_use(input, expected):
    obj = subprocess.Popen(
        input.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        cwd="./tests",
    )
    out, err = obj.communicate()

    assert err == ""
    assert out.strip() == expected


@pytest.mark.cmd
@pytest.mark.parametrize(
    "input,expected",
    [
        ("python ./cmd_deco_args.py 1 -b 2", "1 2 False ()"),
        ("python ./cmd_deco_args.py 1 -b 2 -c -d 3 4", "1 2 True (3, 4)"),
    ],
)
def test_cmd_deco_args(input, expected):
    obj = subprocess.Popen(
        input.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        cwd="./tests",
    )
    out, err = obj.communicate()

    assert err == ""
    assert out.strip() == expected


@pytest.mark.cmd
@pytest.mark.parametrize(
    "input,expected",
    [
        ("python ./cmd_deco_kwargs.py -s 1 2 3 4 ", "10"),
        ("python ./cmd_deco_kwargs.py --max -s 1 2 3 4", "4"),
        ("python ./cmd_deco_kwargs.py --negative -s 1 2 3 4 --max", "-4"),
    ],
)
def test_cmd_deco_kwargs(input, expected):
    obj = subprocess.Popen(
        input.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        cwd="./tests",
    )
    out, err = obj.communicate()

    assert err == ""
    assert out.strip() == expected


@pytest.mark.cmd
@pytest.mark.parametrize(
    "input,expected", [("python ./cmd_deco_mark.py -a 1 -b 2 -c 3 -d 4 ", "1\n4\n3\n2")]
)
def test_cmd_deco_mark_run_order(input, expected):
    obj = subprocess.Popen(
        input.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        cwd="./tests",
    )
    out, err = obj.communicate()

    assert err == ""
    assert out.strip() == expected


@pytest.mark.cmd
@pytest.mark.parametrize(
    "input,expected",
    [("python ./cmd_deco_in_class.py 1 -b 2 -c -d 3 4", "1 2 True (3, 4)")],
)
def test_cmd_deco_in_class(input, expected):
    obj = subprocess.Popen(
        input.split(),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        cwd="./tests",
    )
    out, err = obj.communicate()

    assert err == ""
    assert out.strip() == expected
