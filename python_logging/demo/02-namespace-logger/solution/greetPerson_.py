import logging

logger = logging.getLogger(__name__)


def greet_person(name):
    logger.info("greeting the prisoner!")
    return "Hello {name}, Looking good today!".format(name=name)