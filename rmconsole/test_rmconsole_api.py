import argparse
import json

import requests

from utils.utils import create_url
from settings import (COOKIE_LOCAL, COOKIE_STAGING)


def parse_args():
    # configure command line argument parser
    parser = argparse.ArgumentParser(
        description='Test the RM Console public API.')

    return parser.parse_args()


def main():
    args = parse_args()

    headers = {
        'Content-Type': 'application/json'
    }

    data = {'payload': 'true'}

    cookies = {
        'dev_appserver_login': COOKIE_LOCAL,
        'SACSID': COOKIE_STAGING
    }

    url = create_url(
        'http://localhost:8080', '/api/v1/deployer/deploy/appengine/')

    response = requests.post(url, headers=headers, json=data, cookies=cookies)

    payload = json.loads(response.content)

    print payload

    return


if __name__ == '__main__':
    main()
