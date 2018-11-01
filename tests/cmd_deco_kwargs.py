#!coding:utf-8

from sys import path as sys_path
from os import path as os_path

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), "../")))
import autoargparse

cmd = autoargparse.cmd("cmd deco kwargs test.")


@cmd.kwargs(ne="--negative", action="store_true")
@cmd.kwargs(ma="--max", action="store_true")
@cmd.args("-s", "--sum", "*", type=int)
def add(*args, ma, ne):
    d = 0
    if ma:
        d = max(args)
    else:
        d = sum(args)
    if ne:
        d = -d
    print(d)


cmd.run()
