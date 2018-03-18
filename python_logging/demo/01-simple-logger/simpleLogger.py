






import logging

logger = logging.basicConfig(filename='01-simple-logger.log',
                             level=logging.INFO)


class Person:
    """Creates a Person"""
    
    def __init__(self, name):
        if name is '':
            logging.error("Name is empty")
            return None

        self.name = name
        logging.info("A person named %s is created", name)
        logging.debug("What is Life?")

    def __str__(self):
        return "Name: {}".format(self.name)


def main():
    Person('Boris the Animal')
    Person('Agent Kay')
    Person('')


if __name__ == '__main__':
    main()