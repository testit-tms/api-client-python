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
from pydantic import BaseModel, Field, StrictBool, conlist
from testit_api_client.models.background_job_state import BackgroundJobState
from testit_api_client.models.background_job_type import BackgroundJobType
from testit_api_client.models.date_time_range_selector_model import DateTimeRangeSelectorModel

class BackgroundJobFilterModel(BaseModel):
    """
    BackgroundJobFilterModel
    """
    types: Optional[conlist(BackgroundJobType)] = None
    states: Optional[conlist(BackgroundJobState)] = None
    is_deleted: Optional[StrictBool] = Field(default=None, alias="isDeleted")
    start_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, alias="startDate")
    end_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, alias="endDate")
    __properties = ["types", "states", "isDeleted", "startDate", "endDate"]

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
    def from_json(cls, json_str: str) -> BackgroundJobFilterModel:
        """Create an instance of BackgroundJobFilterModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of start_date
        if self.start_date:
            _dict['startDate'] = self.start_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_date
        if self.end_date:
            _dict['endDate'] = self.end_date.to_dict()
        # set to None if types (nullable) is None
        # and __fields_set__ contains the field
        if self.types is None and "types" in self.__fields_set__:
            _dict['types'] = None

        # set to None if states (nullable) is None
        # and __fields_set__ contains the field
        if self.states is None and "states" in self.__fields_set__:
            _dict['states'] = None

        # set to None if is_deleted (nullable) is None
        # and __fields_set__ contains the field
        if self.is_deleted is None and "is_deleted" in self.__fields_set__:
            _dict['isDeleted'] = None

        # set to None if start_date (nullable) is None
        # and __fields_set__ contains the field
        if self.start_date is None and "start_date" in self.__fields_set__:
            _dict['startDate'] = None

        # set to None if end_date (nullable) is None
        # and __fields_set__ contains the field
        if self.end_date is None and "end_date" in self.__fields_set__:
            _dict['endDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BackgroundJobFilterModel:
        """Create an instance of BackgroundJobFilterModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BackgroundJobFilterModel.parse_obj(obj)

        _obj = BackgroundJobFilterModel.parse_obj({
            "types": obj.get("types"),
            "states": obj.get("states"),
            "is_deleted": obj.get("isDeleted"),
            "start_date": DateTimeRangeSelectorModel.from_dict(obj.get("startDate")) if obj.get("startDate") is not None else None,
            "end_date": DateTimeRangeSelectorModel.from_dict(obj.get("endDate")) if obj.get("endDate") is not None else None
        })
        return _obj


