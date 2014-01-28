#!/usr/bin/env python
import argparse
from ConfigParser import ConfigParser

import os
print os.getcwd()


def parse_args():
    """Handle building what we want to do based on the arguments.

    Examples:
        config-update.py --ini=$INI --port=$PORT --dburl=$DBURL

    """
    desc = """Rebuild the ini config file based on updated values from the
    charm.

    """
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        '-i', '--ini',
        action='store',
        required=True,
        help='Name of the ini file to update.'
    )

    parser.add_argument(
        '-p', '--port',
        action='store',
        required=True,
        help='The port to run the web app on.'
    )

    parser.add_argument(
        '-d', '--dburl',
        action='store',
        required=True,
        help='The SQLAlchemy db url to write data to.'
    )

    return parser.parse_args()


def main(args):
    config = ConfigParser()
    config.read(args.ini)

    config.set('app:bookie', 'sqlalchemy.url', args.dburl)
    config.set('server:main', 'port', args.port)

    with open(args.ini, 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    args = parse_args()
    main(args)
