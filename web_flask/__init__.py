# __init__.py

import logging

logger = logging.getLogger(__name__)

def init():
    logger.info("Initializing package")

init()

