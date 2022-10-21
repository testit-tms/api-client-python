"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import testit_api_client
from testit_api_client.api.parameters_api import ParametersApi  # noqa: E501


class TestParametersApi(unittest.TestCase):
    """ParametersApi unit test stubs"""

    def setUp(self):
        self.api = ParametersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_parameters_bulk_post(self):
        """Test case for api_v2_parameters_bulk_post

        Create multiple parameters  # noqa: E501
        """
        pass

    def test_api_v2_parameters_bulk_put(self):
        """Test case for api_v2_parameters_bulk_put

        Update multiple parameters  # noqa: E501
        """
        pass

    def test_api_v2_parameters_groups_get(self):
        """Test case for api_v2_parameters_groups_get

        Get parameters as group  # noqa: E501
        """
        pass

    def test_api_v2_parameters_key_name_name_exists_get(self):
        """Test case for api_v2_parameters_key_name_name_exists_get

        Check existence parameter key in system  # noqa: E501
        """
        pass

    def test_api_v2_parameters_key_values_get(self):
        """Test case for api_v2_parameters_key_values_get

        Get all parameter key values  # noqa: E501
        """
        pass

    def test_api_v2_parameters_keys_get(self):
        """Test case for api_v2_parameters_keys_get

        Get all parameter keys  # noqa: E501
        """
        pass

    def test_create_parameter(self):
        """Test case for create_parameter

        Create parameter  # noqa: E501
        """
        pass

    def test_delete_by_name(self):
        """Test case for delete_by_name

        Delete parameter by name  # noqa: E501
        """
        pass

    def test_delete_by_parameter_key_id(self):
        """Test case for delete_by_parameter_key_id

        Delete parameters by parameter key identifier  # noqa: E501
        """
        pass

    def test_delete_parameter(self):
        """Test case for delete_parameter

        Delete parameter  # noqa: E501
        """
        pass

    def test_get_all_parameters(self):
        """Test case for get_all_parameters

        Get all parameters  # noqa: E501
        """
        pass

    def test_get_parameter_by_id(self):
        """Test case for get_parameter_by_id

        Get parameter by ID  # noqa: E501
        """
        pass

    def test_obsolete_delete_by_name(self):
        """Test case for obsolete_delete_by_name

        """
        pass

    def test_update_parameter(self):
        """Test case for update_parameter

        Update parameter  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
