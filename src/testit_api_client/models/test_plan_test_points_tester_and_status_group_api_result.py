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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class TestPlanTestPointsTesterAndStatusGroupApiResult(BaseModel):
    """
    TestPlanTestPointsTesterAndStatusGroupApiResult
    """
    user_id: Optional[StrictStr] = Field(default=..., alias="userId")
    status: StrictStr = Field(...)
    value: StrictInt = Field(...)
    __properties = ["userId", "status", "value"]

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
    def from_json(cls, json_str: str) -> TestPlanTestPointsTesterAndStatusGroupApiResult:
        """Create an instance of TestPlanTestPointsTesterAndStatusGroupApiResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['userId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TestPlanTestPointsTesterAndStatusGroupApiResult:
        """Create an instance of TestPlanTestPointsTesterAndStatusGroupApiResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TestPlanTestPointsTesterAndStatusGroupApiResult.parse_obj(obj)

        _obj = TestPlanTestPointsTesterAndStatusGroupApiResult.parse_obj({
            "user_id": obj.get("userId"),
            "status": obj.get("status"),
            "value": obj.get("value")
        })
        return _obj


