""" Settings for webapp """

import sys
from .base import *
try:
    from .local import *
    if 'test' in sys.argv:
        from .test import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-dist.py?)' % exc.args[0]])
    raise exc
