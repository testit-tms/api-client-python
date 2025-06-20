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





class TestPlanStatusModel(str, Enum):
    """
    TestPlanStatusModel
    """

    """
    allowed enum values
    """
    NEW = 'New'
    INPROGRESS = 'InProgress'
    PAUSED = 'Paused'
    COMPLETED = 'Completed'

    @classmethod
    def from_json(cls, json_str: str) -> TestPlanStatusModel:
        """Create an instance of TestPlanStatusModel from a JSON string"""
        return TestPlanStatusModel(json.loads(json_str))


