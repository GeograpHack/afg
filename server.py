import logging
import os
import sys

import blokskenom
import config

logging.basicConfig(
    level=config.logging_level,
)

logger = logging.getLogger()
logger.addHandler(logging.FileHandler(os.path.join(config.logging_dir, 'blokskenom.log')))
logger.addHandler(logging.StreamHandler())

# Log exceptions
def excepthook(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.getLogger(__name__).error('Uncaught exception',
        exc_info=(exc_type, exc_value, exc_traceback)
    )
sys.excepthook = excepthook

app = blokskenom.create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
