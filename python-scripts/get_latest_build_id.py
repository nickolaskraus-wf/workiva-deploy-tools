import pprint
import argparse
import base64
import json

import requests

from settings import (EMAIL_ADDRESS, SMITHY_API_TOKEN)


def parse_args():
    # configure command line argument parser
    parser = argparse.ArgumentParser(
        description='Get the latest build ID for the workiva-deploy '
                    'repository')

    # specify the reference of workiva-deploy
    parser.add_argument('-r', '--reference', type=str,
                        help='refernce of workiva-deploy')

    return parser.parse_args()


def main():
    args = parse_args()

    reference = args.reference

    branch = 'refs/heads/' + reference
    if '.' in reference:
        branch = 'refs/tags/' + reference

    headers = {
        'Authorization':
            'Basic ' + base64.b64encode(EMAIL_ADDRESS + ':' + SMITHY_API_TOKEN)
    }

    params = {'ref': branch}

    url = create_url(
        'https://ci.webfilings.com', '/api/v1/Workiva/workiva-deploy', params)

    response = requests.get(url, headers=headers)

    payload = json.loads(response.content)

    pprint.pprint(payload.get('latest_build'))

    print payload.get('latest_build').get('id')

    return


def create_url(base, path, params=None):
    """
    Create a valid URL using base, path, and parameters.

    :param base: protocol, domain, and port
    :type base: str
    :param path: path to resource
    :type path: str
    :param params: optional parameters
    :type params: dict
    :return: url
    :rtype: str
    """
    if not params:
        return base + path
    else:
        url = base + path + '?'
        for key, value in sorted(params.iteritems()):
            url += key + '=' + str(value) + '&'
        return url[:-1]


if __name__ == '__main__':
    main()
