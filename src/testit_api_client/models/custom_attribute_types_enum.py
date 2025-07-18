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





class CustomAttributeTypesEnum(str, Enum):
    """
    CustomAttributeTypesEnum
    """

    """
    allowed enum values
    """
    STRING = 'string'
    DATETIME = 'datetime'
    OPTIONS = 'options'
    USER = 'user'
    MULTIPLEOPTIONS = 'multipleOptions'
    CHECKBOX = 'checkbox'

    @classmethod
    def from_json(cls, json_str: str) -> CustomAttributeTypesEnum:
        """Create an instance of CustomAttributeTypesEnum from a JSON string"""
        return CustomAttributeTypesEnum(json.loads(json_str))


