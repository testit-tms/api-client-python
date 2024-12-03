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
from testit_api_client.models.custom_attribute_types_enum import CustomAttributeTypesEnum
from typing import Optional, Set
from typing_extensions import Self

class ProjectAttributesFilterModel(BaseModel):
    """
    ProjectAttributesFilterModel
    """ # noqa: E501
    name: StrictStr = Field(description="Specifies an attribute name to search for")
    is_required: Optional[StrictBool] = Field(default=None, description="Specifies an attribute mandatory status to search for", alias="isRequired")
    is_global: Optional[StrictBool] = Field(default=None, description="Specifies an attribute global status to search for", alias="isGlobal")
    types: List[CustomAttributeTypesEnum] = Field(description="Specifies an attribute types to search for")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Specifies an attribute enabled status to search for", alias="isEnabled")
    __properties: ClassVar[List[str]] = ["name", "isRequired", "isGlobal", "types", "isEnabled"]

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
        """Create an instance of ProjectAttributesFilterModel from a JSON string"""
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
        # set to None if is_required (nullable) is None
        # and model_fields_set contains the field
        if self.is_required is None and "is_required" in self.model_fields_set:
            _dict['isRequired'] = None

        # set to None if is_global (nullable) is None
        # and model_fields_set contains the field
        if self.is_global is None and "is_global" in self.model_fields_set:
            _dict['isGlobal'] = None

        # set to None if is_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.is_enabled is None and "is_enabled" in self.model_fields_set:
            _dict['isEnabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectAttributesFilterModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "isRequired": obj.get("isRequired"),
            "isGlobal": obj.get("isGlobal"),
            "types": obj.get("types"),
            "isEnabled": obj.get("isEnabled")
        })
        return _obj

