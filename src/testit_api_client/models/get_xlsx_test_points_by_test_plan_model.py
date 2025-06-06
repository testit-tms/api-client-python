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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetXlsxTestPointsByTestPlanModel(BaseModel):
    """
    GetXlsxTestPointsByTestPlanModel
    """ # noqa: E501
    include_name: StrictBool = Field(alias="includeName")
    include_section: StrictBool = Field(alias="includeSection")
    include_priority: StrictBool = Field(alias="includePriority")
    include_source_type: StrictBool = Field(alias="includeSourceType")
    include_automated: StrictBool = Field(alias="includeAutomated")
    include_status: StrictBool = Field(alias="includeStatus")
    include_duration: StrictBool = Field(alias="includeDuration")
    include_creation_date: StrictBool = Field(alias="includeCreationDate")
    include_author: StrictBool = Field(alias="includeAuthor")
    include_modification_date: StrictBool = Field(alias="includeModificationDate")
    include_modified_by: StrictBool = Field(alias="includeModifiedBy")
    include_tags: StrictBool = Field(alias="includeTags")
    include_iterations: StrictBool = Field(alias="includeIterations")
    custom_attributes_ids: Optional[List[StrictStr]] = Field(default=None, alias="customAttributesIds")
    configuration_ids: Optional[List[StrictStr]] = Field(default=None, alias="configurationIds")
    __properties: ClassVar[List[str]] = ["includeName", "includeSection", "includePriority", "includeSourceType", "includeAutomated", "includeStatus", "includeDuration", "includeCreationDate", "includeAuthor", "includeModificationDate", "includeModifiedBy", "includeTags", "includeIterations", "customAttributesIds", "configurationIds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetXlsxTestPointsByTestPlanModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if custom_attributes_ids (nullable) is None
        # and model_fields_set contains the field
        if self.custom_attributes_ids is None and "custom_attributes_ids" in self.model_fields_set:
            _dict['customAttributesIds'] = None

        # set to None if configuration_ids (nullable) is None
        # and model_fields_set contains the field
        if self.configuration_ids is None and "configuration_ids" in self.model_fields_set:
            _dict['configurationIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetXlsxTestPointsByTestPlanModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includeName": obj.get("includeName"),
            "includeSection": obj.get("includeSection"),
            "includePriority": obj.get("includePriority"),
            "includeSourceType": obj.get("includeSourceType"),
            "includeAutomated": obj.get("includeAutomated"),
            "includeStatus": obj.get("includeStatus"),
            "includeDuration": obj.get("includeDuration"),
            "includeCreationDate": obj.get("includeCreationDate"),
            "includeAuthor": obj.get("includeAuthor"),
            "includeModificationDate": obj.get("includeModificationDate"),
            "includeModifiedBy": obj.get("includeModifiedBy"),
            "includeTags": obj.get("includeTags"),
            "includeIterations": obj.get("includeIterations"),
            "customAttributesIds": obj.get("customAttributesIds"),
            "configurationIds": obj.get("configurationIds")
        })
        return _obj


