#! /usr/bin/env python3

import os
import importlib
import time
import hashlib
import threading


class Monitor(threading.Thread):
    def __init__(self, loader, frequency = 1):
        super().__init__()

        self.frequency = frequency
        self.loader = loader

        self.daemon = True

    def run(self):
        while True:
            with open(self.loader.source) as file:
                fingerprint = hashlib.sha1(file.read().encode('utf-8')).hexdigest()

            if not fingerprint == self.loader.fingerprint:
                self.loader.notify(fingerprint)

            time.sleep(self.frequency)


class Loader:
    def __init__(self, source):
        self.source = source
        self.__name = os.path.splitext(self.source)[0]
        self.module = importlib.import_module(self.__name)
        self.fingerprint = None

        monitor = Monitor(self)
        monitor.start()

    def notify(self, fingerprint):
        self.fingerprint = fingerprint
        self.module = importlib.reload(self.module)

    def __getattr__(self, attr):
        return getattr(self.module, attr)
