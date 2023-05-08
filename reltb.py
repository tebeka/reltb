from os.path import relpath
import sys
import traceback

_prev_hook = None


# Inspired by https://stackoverflow.com/a/69925677/7650
def hook(typ, val, tb):
    """Prints traceback with relative file names."""
    exc = traceback.TracebackException(typ, val, tb)

    for frame in exc.stack:
        frame.filename = relpath(frame.filename)

    print(''.join(exc.format()), file=sys.stderr)


def install():
    """Install hook as global exception handler."""
    global _prev_hook

    _prev_hook = sys.excepthook
    sys.excepthook = hook


def uninstall():
    sys.excepthook = _prev_hook
