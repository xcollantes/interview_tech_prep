"""Different ways to split string into list."""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    sentence: str = "Guida una fiat"

    logging.info(list(sentence))

    logging.info([i for i in sentence])

    mylist: list = []
    mylist.extend(sentence)
    logging.info(mylist)


if __name__ == "__main__":
    main()
