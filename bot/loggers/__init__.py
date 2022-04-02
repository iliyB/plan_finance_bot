import logging.config
from os import path

import yaml  # type: ignore


def setup() -> None:
    log_path = path.join(path.dirname(path.abspath(__file__)), "settings.yml")

    with open(log_path, "r") as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)

    logging.config.dictConfig(config)
    logging.getLogger("aiogram").setLevel(logging.WARNING)
