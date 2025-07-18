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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from testit_api_client.models.parameter_short_model import ParameterShortModel

class PublicTestPointModel(BaseModel):
    """
    PublicTestPointModel
    """
    configuration_id: StrictStr = Field(default=..., alias="configurationId")
    configuration_global_id: StrictInt = Field(default=..., alias="configurationGlobalId")
    auto_test_ids: Optional[conlist(StrictStr)] = Field(default=None, alias="autoTestIds")
    iteration_id: StrictStr = Field(default=..., alias="iterationId")
    parameter_models: Optional[conlist(ParameterShortModel)] = Field(default=None, alias="parameterModels")
    id: StrictStr = Field(...)
    __properties = ["configurationId", "configurationGlobalId", "autoTestIds", "iterationId", "parameterModels", "id"]

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
    def from_json(cls, json_str: str) -> PublicTestPointModel:
        """Create an instance of PublicTestPointModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in parameter_models (list)
        _items = []
        if self.parameter_models:
            for _item in self.parameter_models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameterModels'] = _items
        # set to None if auto_test_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_test_ids is None and "auto_test_ids" in self.__fields_set__:
            _dict['autoTestIds'] = None

        # set to None if parameter_models (nullable) is None
        # and __fields_set__ contains the field
        if self.parameter_models is None and "parameter_models" in self.__fields_set__:
            _dict['parameterModels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublicTestPointModel:
        """Create an instance of PublicTestPointModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PublicTestPointModel.parse_obj(obj)

        _obj = PublicTestPointModel.parse_obj({
            "configuration_id": obj.get("configurationId"),
            "configuration_global_id": obj.get("configurationGlobalId"),
            "auto_test_ids": obj.get("autoTestIds"),
            "iteration_id": obj.get("iterationId"),
            "parameter_models": [ParameterShortModel.from_dict(_item) for _item in obj.get("parameterModels")] if obj.get("parameterModels") is not None else None,
            "id": obj.get("id")
        })
        return _obj


