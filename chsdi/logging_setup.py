import logging
import logging.config
import os
from os import path

import yaml

logger = logging.getLogger(__name__)


def get_logging_cfg():
    cfg_file = os.getenv('LOGGING_CFG', './chsdi/config/logging-cfg-local.yml')
    if 'LOGS_DIR' in os.environ:
        print(f"LOGS_DIR is {os.environ['LOGS_DIR']}")
    print(f"LOGGING_CFG is {cfg_file}")

    config = {}
    with open(cfg_file, 'rt', encoding='utf-8') as fd:
        config = yaml.safe_load(path.expandvars(fd.read()))

    logger.debug('Load logging configuration from file %s', cfg_file)
    return config


def setup_logging():
    config = get_logging_cfg()
    logging.config.dictConfig(config)
