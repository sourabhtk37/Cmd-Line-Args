import logging

logger = logging.basicConfig(filename='01-namespace-logger.log',
                             level=logging.INFO)

import greetPerson

class Person:
    """Creates a Person"""
    
    def __init__(self, name):
        if name is '':
            logging.error("Name is empty")
            return None

        self.name = name
        logging.info("A person named %s is created", self.name)
    
    def greetPerson(self):
        logging.info("greeting the prisoner!")
        return "Hello {name}, Looking good today!".format(name=self.name)

    def __str__(self):
        return "Name: {}".format(self.name)


def main():
    boris_animal = Person('Boris the Animal')
    boris_animal.greetPerson()
    greetPerson.greet_person(boris_animal.name)


if __name__ == '__main__':
    main()