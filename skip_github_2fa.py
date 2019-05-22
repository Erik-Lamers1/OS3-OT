#!/usr/bin/env python

from seleniumrequests import Firefox
from argparse import ArgumentParser


def parse_args(args=None):
    parser = ArgumentParser(description='Script for OT demo qith searchable 2FA codes. '
                                        'Currently configured to work on serverdensity.io')
    parser.add_argument('-u', '--username', required=True, help='The username')
    parser.add_argument('-p', '--password', required=True, help='The password')
    return parser.parse_args()


def main(args=None):
    args = parse_args(args)
    webdriver = Firefox()
    webdriver.request('GET', 'https://serverdensity.io')


if __name__ == '__main__':
    main()
