"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import testit_api_client
from testit_api_client.api.attachments_api import AttachmentsApi  # noqa: E501


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_attachments_id_delete(self):
        """Test case for api_v2_attachments_id_delete

        Delete attachment file  # noqa: E501
        """
        pass

    def test_api_v2_attachments_id_get(self):
        """Test case for api_v2_attachments_id_get

        Download attachment file  # noqa: E501
        """
        pass

    def test_api_v2_attachments_occupied_file_storage_size_get(self):
        """Test case for api_v2_attachments_occupied_file_storage_size_get

        """
        pass

    def test_api_v2_attachments_post(self):
        """Test case for api_v2_attachments_post

        Upload new attachment file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
