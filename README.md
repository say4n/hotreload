<h1 align="center">
    <img src="assets/hotreload.py.svg" style="background-color:rgba(0,0,0,0);"
    height=230 alt="hotreload: hot reload your python code!">
    <br>
    hotreload.py
    <br>
    <sup><sub><sup>hot reload your python code!</sup></sub></sup>
    <br>
</h1>

Run any arbitrary python script every time the code changes in the file.

## installation

Get the package from PyPI with `pip3 install hotreload`.

## usage

Say you have script (`script.py`) that you want to run every time the code
changes in that file.

To do that, it is as simple as doing this:

```python
import time
import logging
from hotreload import Loader


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    script = Loader("script.py")

    while True:
        # Check if script has been modified since last poll.
        if script.has_changed():
            # Execute a function from script if it has been modified.
            script.main()

        time.sleep(1)
```

### author

Sayan Goswami &copy; 2020
