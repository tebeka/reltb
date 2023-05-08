from os import environ
from pathlib import Path
from subprocess import PIPE, run
from sys import executable

here = Path(__file__).absolute().parent
root = here.parent


def test_tb():
    app = 'app.py'
    py_file = here / app
    cmd = [executable, str(py_file)]

    env = environ.copy()
    key = 'PYTHONPATH'
    pp = env.get(key, '')
    env[key] = f'{root}:{pp}'

    out = run(cmd, stderr=PIPE, encoding='UTF-8', env=env)
    assert out.returncode != 0
    assert app in out.stderr
    assert str(here) not in out.stderr
