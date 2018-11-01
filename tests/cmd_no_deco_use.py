#!coding:utf-8

from sys import path as sys_path
from os import path as os_path

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), "../")))
import autoargparse

# "-s|--show|#1|<list:str>|?show all|{color:blue}"

parser = autoargparse.cmd("Process some integers.", debug=True)
parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
)
parser.add_argument(
    "--sum",
    dest="accumulate",
    action="store_const",
    const=sum,
    default=max,
    help="sum the integers (default: find the max)",
)

args = parser.run()

print(args.accumulate(args.integers))
