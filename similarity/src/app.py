import logging
import sys

import falcon

from .NetworkTrainingResource import NetworkTrainingResource
from .SimilarityResource import SimilarityResource

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

api = application = falcon.API()

api.add_route('/similarity', SimilarityResource())
api.add_route('/train', NetworkTrainingResource())