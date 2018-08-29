import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import json
from bson import json_util
from bson.objectid import ObjectId
from eve.utils import str_to_date, date_to_rfc1123
from rpc_apiserver import app


def bson_to_json(_object):
    return json.loads(json.dumps(_object, default=json_util.default))

def json_to_bson(_object):
    return json_util.loads(json.dumps(_object))