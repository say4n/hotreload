#! /usr/bin/env python3

import time
from hotreload import Loader


if __name__ == "__main__":
    loader = Loader("script.py")

    while True:
        loader.f1()
        loader.f2()

        time.sleep(1)