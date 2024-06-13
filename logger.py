import logging
import sys

LOGGER = logging.getLogger("fit_pro")
LOGGER.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(asctime)s] %(levelname)4s %(name)4s %(filename)s:%(lineno)d %(funcName)4s: %(message)4s")
stream_handler.setFormatter(formatter)
LOGGER.addHandler(stream_handler)
