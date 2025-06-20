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
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from testit_api_client.models.autotest_result_outcome import AutotestResultOutcome
from testit_api_client.models.int64_range_selector_model import Int64RangeSelectorModel

class AutoTestResultHistorySelectApiModel(BaseModel):
    """
    AutoTestResultHistorySelectApiModel
    """
    outcomes: Optional[conlist(AutotestResultOutcome, unique_items=True)] = None
    status_codes: Optional[conlist(StrictStr, unique_items=True)] = Field(default=None, alias="statusCodes")
    test_plan_ids: Optional[conlist(StrictStr, unique_items=True)] = Field(default=None, alias="testPlanIds")
    test_run_ids: Optional[conlist(StrictStr, unique_items=True)] = Field(default=None, alias="testRunIds")
    configuration_ids: Optional[conlist(StrictStr, unique_items=True)] = Field(default=None, alias="configurationIds")
    launch_source: Optional[constr(strict=True, max_length=255, min_length=0)] = Field(default=None, alias="launchSource")
    user_ids: Optional[conlist(StrictStr, unique_items=True)] = Field(default=None, alias="userIds")
    duration: Optional[Int64RangeSelectorModel] = None
    __properties = ["outcomes", "statusCodes", "testPlanIds", "testRunIds", "configurationIds", "launchSource", "userIds", "duration"]

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
    def from_json(cls, json_str: str) -> AutoTestResultHistorySelectApiModel:
        """Create an instance of AutoTestResultHistorySelectApiModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # set to None if outcomes (nullable) is None
        # and __fields_set__ contains the field
        if self.outcomes is None and "outcomes" in self.__fields_set__:
            _dict['outcomes'] = None

        # set to None if status_codes (nullable) is None
        # and __fields_set__ contains the field
        if self.status_codes is None and "status_codes" in self.__fields_set__:
            _dict['statusCodes'] = None

        # set to None if test_plan_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.test_plan_ids is None and "test_plan_ids" in self.__fields_set__:
            _dict['testPlanIds'] = None

        # set to None if test_run_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.test_run_ids is None and "test_run_ids" in self.__fields_set__:
            _dict['testRunIds'] = None

        # set to None if configuration_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.configuration_ids is None and "configuration_ids" in self.__fields_set__:
            _dict['configurationIds'] = None

        # set to None if launch_source (nullable) is None
        # and __fields_set__ contains the field
        if self.launch_source is None and "launch_source" in self.__fields_set__:
            _dict['launchSource'] = None

        # set to None if user_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.user_ids is None and "user_ids" in self.__fields_set__:
            _dict['userIds'] = None

        # set to None if duration (nullable) is None
        # and __fields_set__ contains the field
        if self.duration is None and "duration" in self.__fields_set__:
            _dict['duration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AutoTestResultHistorySelectApiModel:
        """Create an instance of AutoTestResultHistorySelectApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AutoTestResultHistorySelectApiModel.parse_obj(obj)

        _obj = AutoTestResultHistorySelectApiModel.parse_obj({
            "outcomes": obj.get("outcomes"),
            "status_codes": obj.get("statusCodes"),
            "test_plan_ids": obj.get("testPlanIds"),
            "test_run_ids": obj.get("testRunIds"),
            "configuration_ids": obj.get("configurationIds"),
            "launch_source": obj.get("launchSource"),
            "user_ids": obj.get("userIds"),
            "duration": Int64RangeSelectorModel.from_dict(obj.get("duration")) if obj.get("duration") is not None else None
        })
        return _obj


