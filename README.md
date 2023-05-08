# reltb

Relative file names in Python tracebacks.


## Usage

```python
import reldb

reldb.install()

def div(a, b):
    return a / b

div(1, 0)
```

## Installing

Copy over [reldb.py](https://raw.githubusercontent.com/tebeka/reltb/main/reltb.py) to somewhere in your PYTHONPATH.
