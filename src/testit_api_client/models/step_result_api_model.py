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
from testit_api_client.models.shared_step_result_api_model import SharedStepResultApiModel
from testit_api_client.models.step_comment_api_model import StepCommentApiModel

class StepResultApiModel(BaseModel):
    """
    StepResultApiModel
    """
    step_id: StrictStr = Field(default=..., alias="stepId")
    outcome: StrictStr = Field(...)
    shared_step_version_id: Optional[StrictStr] = Field(default=None, alias="sharedStepVersionId")
    shared_step_results: Optional[conlist(SharedStepResultApiModel)] = Field(default=None, alias="sharedStepResults")
    comment: Optional[StepCommentApiModel] = None
    __properties = ["stepId", "outcome", "sharedStepVersionId", "sharedStepResults", "comment"]

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
    def from_json(cls, json_str: str) -> StepResultApiModel:
        """Create an instance of StepResultApiModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in shared_step_results (list)
        _items = []
        if self.shared_step_results:
            for _item in self.shared_step_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sharedStepResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        # set to None if shared_step_version_id (nullable) is None
        # and __fields_set__ contains the field
        if self.shared_step_version_id is None and "shared_step_version_id" in self.__fields_set__:
            _dict['sharedStepVersionId'] = None

        # set to None if shared_step_results (nullable) is None
        # and __fields_set__ contains the field
        if self.shared_step_results is None and "shared_step_results" in self.__fields_set__:
            _dict['sharedStepResults'] = None

        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StepResultApiModel:
        """Create an instance of StepResultApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StepResultApiModel.parse_obj(obj)

        _obj = StepResultApiModel.parse_obj({
            "step_id": obj.get("stepId"),
            "outcome": obj.get("outcome"),
            "shared_step_version_id": obj.get("sharedStepVersionId"),
            "shared_step_results": [SharedStepResultApiModel.from_dict(_item) for _item in obj.get("sharedStepResults")] if obj.get("sharedStepResults") is not None else None,
            "comment": StepCommentApiModel.from_dict(obj.get("comment")) if obj.get("comment") is not None else None
        })
        return _obj


