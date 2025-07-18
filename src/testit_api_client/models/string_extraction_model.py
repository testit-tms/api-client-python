# coding: utf-8

"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist

class StringExtractionModel(BaseModel):
    """
    StringExtractionModel
    """
    include: Optional[conlist(StrictStr)] = None
    exclude: Optional[conlist(StrictStr)] = None
    __properties = ["include", "exclude"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> StringExtractionModel:
        """Create an instance of StringExtractionModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if include (nullable) is None
        # and __fields_set__ contains the field
        if self.include is None and "include" in self.__fields_set__:
            _dict['include'] = None

        # set to None if exclude (nullable) is None
        # and __fields_set__ contains the field
        if self.exclude is None and "exclude" in self.__fields_set__:
            _dict['exclude'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StringExtractionModel:
        """Create an instance of StringExtractionModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StringExtractionModel.parse_obj(obj)

        _obj = StringExtractionModel.parse_obj({
            "include": obj.get("include"),
            "exclude": obj.get("exclude")
        })
        return _obj


