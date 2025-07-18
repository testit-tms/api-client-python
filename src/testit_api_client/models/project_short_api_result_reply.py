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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from testit_api_client.models.project_short_api_result import ProjectShortApiResult

class ProjectShortApiResultReply(BaseModel):
    """
    ProjectShortApiResultReply
    """
    data: conlist(ProjectShortApiResult) = Field(...)
    total_count: StrictInt = Field(default=..., alias="totalCount")
    __properties = ["data", "totalCount"]

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
    def from_json(cls, json_str: str) -> ProjectShortApiResultReply:
        """Create an instance of ProjectShortApiResultReply from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectShortApiResultReply:
        """Create an instance of ProjectShortApiResultReply from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProjectShortApiResultReply.parse_obj(obj)

        _obj = ProjectShortApiResultReply.parse_obj({
            "data": [ProjectShortApiResult.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "total_count": obj.get("totalCount")
        })
        return _obj


