import logging

import greetPerson_

logger = logging.basicConfig(filename='02-namespace-logger.log',
                             level=logging.INFO)
logger = logging.getLogger(__name__)



class Person:
    """Creates a Person"""
    
    def __init__(self, name):
        if name is '':
            logger.error("Name is empty")
            return None

        self.name = name
        logger.info("A person named %s is created", self.name)
    
    def greetPerson(self):
        logger.info("greeting the prisoner!")
        return "Hello {name}, Looking good today!".format(name=self.name)

    def __str__(self):
        return "Name: {}".format(self.name)


def main():
    boris_animal = Person('Boris the Animal')
    boris_animal.greetPerson()
    greetPerson_.greet_person(boris_animal.name)


if __name__ == '__main__':
    main()