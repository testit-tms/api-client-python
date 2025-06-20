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
from pydantic import BaseModel, Field, StrictStr, conlist
from testit_api_client.models.parameter_short_api_result import ParameterShortApiResult

class IterationApiResult(BaseModel):
    """
    IterationApiResult
    """
    id: StrictStr = Field(...)
    parameters: Optional[conlist(ParameterShortApiResult)] = None
    __properties = ["id", "parameters"]

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
    def from_json(cls, json_str: str) -> IterationApiResult:
        """Create an instance of IterationApiResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        # set to None if parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.parameters is None and "parameters" in self.__fields_set__:
            _dict['parameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IterationApiResult:
        """Create an instance of IterationApiResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IterationApiResult.parse_obj(obj)

        _obj = IterationApiResult.parse_obj({
            "id": obj.get("id"),
            "parameters": [ParameterShortApiResult.from_dict(_item) for _item in obj.get("parameters")] if obj.get("parameters") is not None else None
        })
        return _obj


