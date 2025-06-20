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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class GetXlsxTestPointsByTestPlanModel(BaseModel):
    """
    GetXlsxTestPointsByTestPlanModel
    """
    include_name: StrictBool = Field(default=..., alias="includeName")
    include_section: StrictBool = Field(default=..., alias="includeSection")
    include_priority: StrictBool = Field(default=..., alias="includePriority")
    include_source_type: StrictBool = Field(default=..., alias="includeSourceType")
    include_automated: StrictBool = Field(default=..., alias="includeAutomated")
    include_status: StrictBool = Field(default=..., alias="includeStatus")
    include_duration: StrictBool = Field(default=..., alias="includeDuration")
    include_creation_date: StrictBool = Field(default=..., alias="includeCreationDate")
    include_author: StrictBool = Field(default=..., alias="includeAuthor")
    include_modification_date: StrictBool = Field(default=..., alias="includeModificationDate")
    include_modified_by: StrictBool = Field(default=..., alias="includeModifiedBy")
    include_tags: StrictBool = Field(default=..., alias="includeTags")
    include_iterations: StrictBool = Field(default=..., alias="includeIterations")
    custom_attributes_ids: Optional[conlist(StrictStr)] = Field(default=None, alias="customAttributesIds")
    configuration_ids: Optional[conlist(StrictStr)] = Field(default=None, alias="configurationIds")
    __properties = ["includeName", "includeSection", "includePriority", "includeSourceType", "includeAutomated", "includeStatus", "includeDuration", "includeCreationDate", "includeAuthor", "includeModificationDate", "includeModifiedBy", "includeTags", "includeIterations", "customAttributesIds", "configurationIds"]

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
    def from_json(cls, json_str: str) -> GetXlsxTestPointsByTestPlanModel:
        """Create an instance of GetXlsxTestPointsByTestPlanModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if custom_attributes_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.custom_attributes_ids is None and "custom_attributes_ids" in self.__fields_set__:
            _dict['customAttributesIds'] = None

        # set to None if configuration_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.configuration_ids is None and "configuration_ids" in self.__fields_set__:
            _dict['configurationIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetXlsxTestPointsByTestPlanModel:
        """Create an instance of GetXlsxTestPointsByTestPlanModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetXlsxTestPointsByTestPlanModel.parse_obj(obj)

        _obj = GetXlsxTestPointsByTestPlanModel.parse_obj({
            "include_name": obj.get("includeName"),
            "include_section": obj.get("includeSection"),
            "include_priority": obj.get("includePriority"),
            "include_source_type": obj.get("includeSourceType"),
            "include_automated": obj.get("includeAutomated"),
            "include_status": obj.get("includeStatus"),
            "include_duration": obj.get("includeDuration"),
            "include_creation_date": obj.get("includeCreationDate"),
            "include_author": obj.get("includeAuthor"),
            "include_modification_date": obj.get("includeModificationDate"),
            "include_modified_by": obj.get("includeModifiedBy"),
            "include_tags": obj.get("includeTags"),
            "include_iterations": obj.get("includeIterations"),
            "custom_attributes_ids": obj.get("customAttributesIds"),
            "configuration_ids": obj.get("configurationIds")
        })
        return _obj


