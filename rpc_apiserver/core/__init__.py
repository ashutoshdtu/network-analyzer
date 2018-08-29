import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from ..core.function_mapper import FunctionMapper 
function_map = FunctionMapper()

from ..core.utils import *