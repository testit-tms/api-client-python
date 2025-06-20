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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from testit_api_client.models.test_status_api_type import TestStatusApiType

class WorkflowStatusApiResult(BaseModel):
    """
    WorkflowStatusApiResult
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    code: StrictStr = Field(...)
    type: TestStatusApiType = Field(default=..., description="Collection of possible status types")
    description: Optional[StrictStr] = None
    is_system: StrictBool = Field(default=..., alias="isSystem")
    priority: StrictInt = Field(...)
    __properties = ["id", "name", "code", "type", "description", "isSystem", "priority"]

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
    def from_json(cls, json_str: str) -> WorkflowStatusApiResult:
        """Create an instance of WorkflowStatusApiResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowStatusApiResult:
        """Create an instance of WorkflowStatusApiResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkflowStatusApiResult.parse_obj(obj)

        _obj = WorkflowStatusApiResult.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "code": obj.get("code"),
            "type": obj.get("type"),
            "description": obj.get("description"),
            "is_system": obj.get("isSystem"),
            "priority": obj.get("priority")
        })
        return _obj


