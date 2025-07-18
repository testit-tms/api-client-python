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
from pydantic import BaseModel, Field, StrictInt

class TestPlanSummaryModel(BaseModel):
    """
    TestPlanSummaryModel
    """
    total_test_points_count: StrictInt = Field(default=..., alias="totalTestPointsCount")
    manual_test_points_count: StrictInt = Field(default=..., alias="manualTestPointsCount")
    automated_test_points_count: StrictInt = Field(default=..., alias="automatedTestPointsCount")
    completed_test_points_count: StrictInt = Field(default=..., alias="completedTestPointsCount")
    defects_count: StrictInt = Field(default=..., alias="defectsCount")
    planned_test_points_duration: StrictInt = Field(default=..., alias="plannedTestPointsDuration")
    spent_test_points_duration: Optional[StrictInt] = Field(default=None, alias="spentTestPointsDuration")
    __properties = ["totalTestPointsCount", "manualTestPointsCount", "automatedTestPointsCount", "completedTestPointsCount", "defectsCount", "plannedTestPointsDuration", "spentTestPointsDuration"]

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
    def from_json(cls, json_str: str) -> TestPlanSummaryModel:
        """Create an instance of TestPlanSummaryModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if spent_test_points_duration (nullable) is None
        # and __fields_set__ contains the field
        if self.spent_test_points_duration is None and "spent_test_points_duration" in self.__fields_set__:
            _dict['spentTestPointsDuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TestPlanSummaryModel:
        """Create an instance of TestPlanSummaryModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TestPlanSummaryModel.parse_obj(obj)

        _obj = TestPlanSummaryModel.parse_obj({
            "total_test_points_count": obj.get("totalTestPointsCount"),
            "manual_test_points_count": obj.get("manualTestPointsCount"),
            "automated_test_points_count": obj.get("automatedTestPointsCount"),
            "completed_test_points_count": obj.get("completedTestPointsCount"),
            "defects_count": obj.get("defectsCount"),
            "planned_test_points_duration": obj.get("plannedTestPointsDuration"),
            "spent_test_points_duration": obj.get("spentTestPointsDuration")
        })
        return _obj


