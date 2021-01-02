#!/usr/bin/env python
import os
import sys


def main(args=None):
    import pytest

    if not args:
        args = []

    major, minor = sys.version_info[:2]

    python35 = False

    extras = ["xxhash"]

    # aiohttp available on Python >=3.5
    if major == 3 and minor >= 5:
        python35 = True

        extras += ["aiohttp", "async_timeout"]

    os.system("pipenv run pip install {}".format(" ".join(extras)))

    if not any(a for a in args[1:] if not a.startswith("-")):
        args.append("tests/main")
        args.append("mocket")

        if python35:
            args.append("tests/tests35")

        if major == 3 and minor >= 8:
            args.append("tests/tests38")

    sys.exit(pytest.main(args))


if __name__ == "__main__":
    main(sys.argv)