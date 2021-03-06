# autoargparse
Make CMD arg-parser easy and simple.

## dependency
* python can import argparse

## How to use
1. pip install autoargparse

2. import autoargparse

3. Initialize :           
cmd = autoargparse.cmd()

4. Use functon decorator :  <br>   
    @cmd.args(short_name, long_name, nargs, help, action, type) <br>
    set function argument as args type

    @cmd.kwargs(arg_name=short_name, nargs, help, action, type) <br>
    set function argument as kwargs type

    @cmd.mark(run_order=None) <br>
    set function run order(integer, bigger first run)

5. Run:
cmd.run()

## example
```python
#!coding:utf-8

import autoargparse

cmd = autoargparse.cmd('simple calculator for example.')

@cmd.mark(1)
@cmd.kwargs(ne='--negative', action='store_true')
@cmd.kwargs(ma='--max', action='store_true')
@cmd.args('-s', '--sum', '*', type=int)
def add(*args, ma, ne):
    if args or ma or ne:
        d = 0
        if ma:
            d = max(args)
        else:
            d = sum(args)
        if ne:
            d = -d
        print(d)

@cmd.mark(2)
@cmd.args('-v', action='count')
@cmd.args('-m', '--mul', 2, help='MUL!!!', type=int)
def mul(a,b,v=None):
    if not v:
        print(a*b)
    elif v==1:
        print('a * b =', a*b)
    elif v==2:
        print('func =', mul.__name__, 'args =', a, b, v)
        print('a * b =', a*b)

@cmd.mark(3)
@cmd.args('g', type=int, help='print great')
def great(a):
    if a==1:
        print('!!!')
    else:
        print('Great !!!')



if __name__ == "__main__":
    cmd.run()
```

### OUTPUT

> python .\example.py -h

```
usage: test.py [-h] [-s [SUM [SUM ...]]] [--max] [--negative] [-m MUL MUL]
               [-v]
               g

simple calculator for test.

positional arguments:
  g                     print great

optional arguments:
  -h, --help            show this help message and exit
  -s [SUM [SUM ...]], --sum [SUM [SUM ...]]
  --max
  --negative
  -m MUL MUL, --mul MUL MUL
                        MUL!!!
  -v
```

> python .\example.py 1
```
!!!
```

> python .\example.py 2
```
Great !!!
```

> python .\example.py 1 -m 2 3
```
!!!
6
```

> python .\example.py 1 -m 2 3 -v
```
!!!
a * b = 6
```

> python .\example.py 1 -m 2 3 -vv
```
!!!
func = mul args = 2 3 2
a * b = 6
```

> python .\example.py 1 -s 1 2 3 4
```
!!!
10
```

> python .\example.py 1 -s 1 2 3 4 --max
```
!!!
4
```

> python .\example.py 1 -s 1 2 3 4 --negative
```
!!!
-10
```


## TODO
* add GUI
* more easy to use
