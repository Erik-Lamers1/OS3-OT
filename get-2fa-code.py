#!/usr/bin/env python3

import logging
from argparse import ArgumentParser
from subprocess import check_output

from settings import VALID_BROWSERS, GOOGLE_CHROME_CONFIG_DIR, MOZILLA_FIREFOX_CONFIG_DIR
from utils.logger import configure_logging
from utils.filesystem import get_json_from_file, read_lines_from_file

"""
This script will combine some bash commands to look for TOTP secrets in either Chrome or Firefox
Only works with plain text TOTP codes atm.

Author: Erik Lamers <erik.lamers@os3.nl>
"""

logger = configure_logging(__name__)


def parse_args(args=None):
    parser = ArgumentParser(description='Tries to find TOTP codes for a account '
                                        'and generates the corresponding 2FA codes')

    parser.add_argument('browser', help='The browser to try to find TOTP secrets for, '
                                        'valid options are {}'.format(', '.join(VALID_BROWSERS)))

    parser.add_argument('--override-config-dir', help='Override the default config dir for browser')
    parser.add_argument('--override-search-extensions', nargs='*', help='A list of extension which to '
                                                                        'consider for TOTP codes (separated by spaces)')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')

    args = parser.parse_args(args)

    # Validate arguments
    if args.browser.lower() not in VALID_BROWSERS:
        parser.error('{} is not a supported browser'.format(args.browser))

    return args


def search_config_dir_for_totp_secrets(path):
    possibilities = list()
    logger.info('Searching {} for TOTP secrets'.format(path))
    results = check_output('utils/find_totp_secrets.sh {}'.format(path), shell=True).decode('utf-8')
    # Skip first line
    for line in results.splitlines()[1:]:
        possibilities.append({
            'path': line.split(':')[0],
            'secret': line.split(':')[1]
        })
    return possibilities


def get_totp_codes_from_leveldb_file(path):
    logger.info('Trying to import {}'.format(path))



def get_applicable_files_from_results(results, extensions):
    for path, secret in results.items():
        # Split the path on . and get the last item
        if path.split('.')[-1] in extensions:
            logger.debug('{} has a valid extension looking for TOTP codes'.format(path))



def chrome_totp_search(override=None):
    path = override if override else GOOGLE_CHROME_CONFIG_DIR
    return search_config_dir_for_totp_secrets(path)


def main(args=None):
    args = parse_args(args)
    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)
    logger.info('Argument validation successful')

    if args.browser.lower() == 'chrome':
        logger.info('Selecting Google Chrome as target browser')
        results = chrome_totp_search(args.override_config_dir)
        if args.debug:
            logger.debug('Found the following results:')
            print(results)


if __name__ == '__main__':
    main()

