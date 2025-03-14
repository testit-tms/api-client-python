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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.auto_test_filter_api_model import AutoTestFilterApiModel
from testit_api_client.models.auto_test_search_include_api_model import AutoTestSearchIncludeApiModel
from typing import Optional, Set
from typing_extensions import Self

class AutoTestSearchApiModel(BaseModel):
    """
    AutoTestSearchApiModel
    """ # noqa: E501
    filter: Optional[AutoTestFilterApiModel] = Field(default=None, description="Object containing different filters to adjust search")
    includes: Optional[AutoTestSearchIncludeApiModel] = Field(default=None, description="Object specifying data to be included")
    __properties: ClassVar[List[str]] = ["filter", "includes"]

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
        """Create an instance of AutoTestSearchApiModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of includes
        if self.includes:
            _dict['includes'] = self.includes.to_dict()
        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        # set to None if includes (nullable) is None
        # and model_fields_set contains the field
        if self.includes is None and "includes" in self.model_fields_set:
            _dict['includes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutoTestSearchApiModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filter": AutoTestFilterApiModel.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "includes": AutoTestSearchIncludeApiModel.from_dict(obj["includes"]) if obj.get("includes") is not None else None
        })
        return _obj


