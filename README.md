# reltb

Relative file names in Python tracebacks.


## Usage:

```python
import reldb

reldb.install()

def div(a, b):
    return a / b

div(1, 0)
```
