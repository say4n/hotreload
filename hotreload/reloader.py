#! /usr/bin/env python3

import os
import importlib
import time
import hashlib
import threading
import logging

logger = logging.getLogger("hot_reload")

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

        self.changed = False

        monitor = Monitor(self)
        monitor.start()

    def notify(self, fingerprint):
        self.fingerprint = fingerprint
        try:
            logger.info(f"Fingerprint changed to {fingerprint[:7]}, reloading.")
            self.module = importlib.reload(self.module)
            self.changed = True
        except Exception as e:
            logger.error(f"Reload failed. {e}")

    def has_changed(self):
        logger.info(f"Loader.has_changed called, self.changed is {self.changed}")
        if self.changed:
            self.changed = False
            return True
        else:
            return False

    def __getattr__(self, attr):
        return getattr(self.module, attr)
