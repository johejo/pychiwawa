import json
import time
import os

import requests

from .common import AttributeDict
from .exceptions import ChiwawaResponseError


def build_response(resp):
    if resp.status_code != 200:
        raise ChiwawaResponseError(resp.content)

    return json.loads(resp.content, object_hook=AttributeDict)


class ChiwawaClient(object):
    def __init__(self, company_id, token):
        self.base_url = 'https://{}.chiwawa.one/api/public/v1'.format(company_id)
        self.headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': token,
        }

    def post_message(self, group_id, text, *,
                     to=None, from_info=None, to_all=False, attachments=None):
        data = {
            'text': text
        }

        if to is not None:
            data['to'] = to

        if from_info is True:
            data['from'] = from_info

        data['toAll'] = to_all

        if attachments is not None:
            data['attachments'] = attachments

        url = '{0}/groups/{1}/messages'.format(self.base_url, group_id)
        resp = requests.post(url, headers=self.headers, data=json.dumps(data))

        return build_response(resp)

    def get_message_list(self, group_id, *,
                         created_at_from=0, created_at_to=int(time.time()),
                         max_results=20):
        params = {
            'createdAtFrom': created_at_from,
            'createdAtTo': created_at_to,
            'maxResults': max_results,
        }

        url = '{0}/groups/{1}/messages'.format(self.base_url, group_id)
        resp = requests.get(url, headers=self.headers, params=params)

        return build_response(resp)

    def get_message_info(self, group_id, message_id):
        url = '{0}/groups/{1}/messages/{2}'.format(self.base_url, group_id,
                                                   message_id)
        resp = requests.get(url, headers=self.headers)

        return build_response(resp)

    def delete_message(self, group_id, message_id):
        url = '{0}/groups/{1}/messages/{2}'.format(self.base_url, group_id,
                                                   message_id)
        resp = requests.delete(url, headers=self.headers)

        return build_response(resp)

    def update_message_attachments(self, group_id, message_id, attachments):
        url = '{0}/groups/{1}/messages/{2}/attachments'.format(self.base_url,
                                                               group_id,
                                                               message_id)
        data = {'attachments': attachments}
        resp = requests.put(url, headers=self.headers, data=json.dumps(data))

        return build_response(resp)

    def get_file_info(self, group_id, message_id):
        url = '{0}/groups/{1}/files/{2}'.format(self.base_url, group_id,
                                                message_id)
        resp = requests.get(url, headers=self.headers)

        return build_response(resp)

    def post_file(self, group_id, file_path, file_type, *, file_name=None):
        url = '{0}/groups/{1}/files'.format(self.base_url, group_id)

        binary = open(file_path, 'rb')

        if file_name is None:
            file_name = os.path.basename(file_path)

        files = {
            'file': (file_name, binary, file_type)
        }

        data = {
            'fileName': file_name
        }

        resp = requests.post(url, headers=self.headers, files=files, data=data)

        return build_response(resp)

    def get_group_user_list(self, group_id):
        url = '{0}/groups/{1}/users'.format(self.base_url, group_id)
        resp = requests.get(url, headers=self.headers)

        return build_response(resp)

    def get_group_list(self):
        url = '{0}/groups'.format(self.base_url)
        resp = requests.get(url, headers=self.headers)

        return build_response(resp)

    def get_group_info(self, group_id):
        url = '{0}/groups/{1}'.format(self.base_url, group_id)
        resp = requests.get(url, headers=self.headers)

        return build_response(resp)
