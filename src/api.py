import mimetypes
import os
from ast import literal_eval
import requests


class Api(object):

    def __init__(self, url, private_token, proxy=None):
        self.url = url
        mimetypes.add_type('text/plain', '.log')
        mimetypes.add_type('application/octet-stream', '')
        self.request = requests.Session()
        self.request.headers = {'Authorization': 'PrivateToken ' + private_token}
        self.request.proxies = literal_eval(proxy) if proxy else {}

    # AutoTests
    def create_autotest(self, json):
        response = self.request.post(
            self.url + '/api/v2/autoTests',
            json=json
        )
        print(f"Autotest: {json['name']}")
        if response.status_code != 201:
            raise Exception(f"Create autotest error: {response.json()['error']['key']}")
        print('\nCreate autotest passed!')
        return response.json()['id']

    def link_autotest(self, autotest_id, workitem_id):
        response = self.request.post(
            f'{self.url}/api/v2/autoTests/{autotest_id}/workItems',
            json={'id': workitem_id}
        )
        if response.status_code == 204:
            print('Link autoTest with workItems passed!')
        else:
            print(f"Link autoTest with workItems error: {response.json()['error']['key']}")

    def get_autotest(self, external_id, project_id):
        response = self.request.get(
            f'{self.url}/api/v2/autoTests?projectId={project_id}&externalId={external_id}'
        )
        if response.status_code != 200:
            raise Exception(f"Get autoTest error: {response.json()['error']['key']}")
        print('\nGet autoTest passed!')
        return response

    def update_autotest(self, json):
        response = self.request.put(
            self.url + '/api/v2/autoTests',
            json=json
        )
        print(f"AutoTest: {json['name']}")
        if response.status_code == 204:
            print('Update passed!')
        else:
            raise Exception(f"Update error: {response.json()['error']['key']}")

    # TestRuns
    def create_testrun(self, json):
        response = self.request.post(
            self.url + '/api/v2/testRuns',
            json=json
        )
        if response.status_code != 201:
            raise Exception(f"Create testRun error: {response.json()['error']['key']}")
        print('Create testRun passed!')
        return response.json()['id']

    def get_testrun(self, testrun_id):
        response = self.request.get(
            f'{self.url}/api/v2/testRuns/{testrun_id}'
        )
        if response.status_code != 200:
            raise Exception(f"Get testRun error: {response.json()['error']['key']}")
        print('Get testRun passed!')
        return response.json()['projectId'], response.json()['testResults']

    def set_results_for_testrun(self, testrun_id, json):
        response = self.request.post(
            f'{self.url}/api/v2/testRuns/{testrun_id}/testResults',
            json=json
        )
        if response.status_code == 200:
            print('Set results passed!')
        else:
            raise Exception(f"Set results error: {response.json()['error']['key']}")

    def testrun_activity(self, testrun_id, action):
        response = self.request.post(
            f'{self.url}/api/v2/testRuns/{testrun_id}/{action}'
        )
        if response.status_code == 204:
            print(f'TestRun {action} passed!')
        else:
            raise Exception(f"TestRun {action} error: {response.json()['error']['key']}")

    def load_attachment(self, file):
        response = self.request.post(
            f'{self.url}/api/Attachments',
            files={
                'file': (os.path.basename(file.name),
                         file,
                         mimetypes.guess_type(file.name)[0])
            }
        )
        if response.status_code == 201:
            print(f'Attachment {file.name} loaded!')
            return response.json()['id']
        else:
            print(f"Attachment {file.name} error: {response.json()['error']['key']}")
            return None
