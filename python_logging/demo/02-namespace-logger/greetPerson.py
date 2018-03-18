import logging


def greet_person(name):
    logging.info("greeting the prisoner!")
    return "Hello {name}, Looking good today!".format(name=name)
