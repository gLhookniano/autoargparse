#!coding:utf-8

from sys import path as sys_path
from os import path as os_path

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), "../")))
import autoargparse


cmd = autoargparse.cmd("cmd deco args test.")


@cmd.args("-d", "--d", "*", type=int, help="d")
@cmd.args("-c", action="store_true")
@cmd.args("-b")
@cmd.args("a", type=int)
def func(a, b, c, *d):
    print(a, b, c, d)


cmd.run()
