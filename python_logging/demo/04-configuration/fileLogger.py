import logging
import logging.config


def happyMessage():
    return "Your smile is wonderful!"

def main():

    logging.config.fileConfig('logging.cfg')
    logger = logging.getLogger("app")
 
    logger.info("Program started")
    print(happyMessage())
    logger.info("Done!")


if __name__ == "__main__":
    main()