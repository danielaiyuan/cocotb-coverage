
import sys

__version__ = '1.2.0.dev0'

if sys.version_info[0] < 3:
    raise Exception("cocotb-coverage package requies Python 3")
