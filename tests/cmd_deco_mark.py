#!coding:utf-8

from sys import path as sys_path
from os import path as os_path

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), "../")))
import autoargparse


cmd = autoargparse.cmd("cmd deco mark test.")


@cmd.mark(run_order=4)
@cmd.args("-a")
def a(x):
    print(x)


@cmd.mark(run_order=1)
@cmd.args("-b")
def b(x):
    print(x)


@cmd.mark(run_order=2)
@cmd.args("-c")
def c(x):
    print(x)


@cmd.mark(run_order=3)
@cmd.args("-d")
def d(x):
    print(x)


cmd.run()
