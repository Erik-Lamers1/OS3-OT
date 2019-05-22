#!/usr/bin/env python3

from seleniumrequests import Firefox
from argparse import ArgumentParser


DOMAIN = 'https://serverdesity.io'

def parse_args(args=None):
    parser = ArgumentParser(description='Script for OT demo qith searchable 2FA codes. '
                                        'Currently configured to work on {}'.format(DOMAIN))
    parser.add_argument('-u', '--username', required=True, help='The username')
    parser.add_argument('-p', '--password', required=True, help='The password')
    return parser.parse_args()


def main(args=None):
    args = parse_args(args)
    webdriver = Firefox()
    webdriver.get('https://serverdensity.io')
    response = webdriver.request('POST', '{}/sessions'.format(DOMAIN), data={'username': args.username,
                                                 'password': args.password,
                                                 'MFAotpcode': 'blaap',
                                                 'MFAremember': 'false',
                                                 'accountName': args.username}
                      )
    print(response)


if __name__ == '__main__':
    main()
