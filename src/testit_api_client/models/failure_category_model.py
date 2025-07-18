# coding: utf-8

"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class FailureCategoryModel(str, Enum):
    """
    FailureCategoryModel
    """

    """
    allowed enum values
    """
    INFRASTRUCTUREDEFECT = 'InfrastructureDefect'
    PRODUCTDEFECT = 'ProductDefect'
    TESTDEFECT = 'TestDefect'
    NODEFECT = 'NoDefect'
    NOANALYTICS = 'NoAnalytics'

    @classmethod
    def from_json(cls, json_str: str) -> FailureCategoryModel:
        """Create an instance of FailureCategoryModel from a JSON string"""
        return FailureCategoryModel(json.loads(json_str))


