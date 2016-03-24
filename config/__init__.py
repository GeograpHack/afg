from config.default import *
try:
    from config.config import *
except ImportError:
    print('Using default settings.')
