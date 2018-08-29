import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import json
from rpc_apiserver import app, methods, InvalidParams

@methods.add
def list_processes():
    return []