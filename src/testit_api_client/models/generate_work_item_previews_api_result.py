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
from pydantic import BaseModel, Field, conlist
from testit_api_client.models.previews_issue_link_api_result import PreviewsIssueLinkApiResult
from testit_api_client.models.work_item_preview_api_model import WorkItemPreviewApiModel

class GenerateWorkItemPreviewsApiResult(BaseModel):
    """
    GenerateWorkItemPreviewsApiResult
    """
    previews: conlist(WorkItemPreviewApiModel) = Field(...)
    link: Optional[PreviewsIssueLinkApiResult] = None
    __properties = ["previews", "link"]

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
    def from_json(cls, json_str: str) -> GenerateWorkItemPreviewsApiResult:
        """Create an instance of GenerateWorkItemPreviewsApiResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in previews (list)
        _items = []
        if self.previews:
            for _item in self.previews:
                if _item:
                    _items.append(_item.to_dict())
            _dict['previews'] = _items
        # override the default output from pydantic by calling `to_dict()` of link
        if self.link:
            _dict['link'] = self.link.to_dict()
        # set to None if link (nullable) is None
        # and __fields_set__ contains the field
        if self.link is None and "link" in self.__fields_set__:
            _dict['link'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GenerateWorkItemPreviewsApiResult:
        """Create an instance of GenerateWorkItemPreviewsApiResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GenerateWorkItemPreviewsApiResult.parse_obj(obj)

        _obj = GenerateWorkItemPreviewsApiResult.parse_obj({
            "previews": [WorkItemPreviewApiModel.from_dict(_item) for _item in obj.get("previews")] if obj.get("previews") is not None else None,
            "link": PreviewsIssueLinkApiResult.from_dict(obj.get("link")) if obj.get("link") is not None else None
        })
        return _obj


