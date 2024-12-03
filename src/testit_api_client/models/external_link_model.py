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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ExternalLinkModel(BaseModel):
    """
    ExternalLinkModel
    """ # noqa: E501
    url: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    issue_type_name: Optional[StrictStr] = Field(default=None, alias="issueTypeName")
    issue_type_icon_url: Optional[StrictStr] = Field(default=None, alias="issueTypeIconUrl")
    priority_name: Optional[StrictStr] = Field(default=None, alias="priorityName")
    priority_icon_url: Optional[StrictStr] = Field(default=None, alias="priorityIconUrl")
    status_name: Optional[StrictStr] = Field(default=None, alias="statusName")
    assignee_display_name: Optional[StrictStr] = Field(default=None, alias="assigneeDisplayName")
    __properties: ClassVar[List[str]] = ["url", "title", "issueTypeName", "issueTypeIconUrl", "priorityName", "priorityIconUrl", "statusName", "assigneeDisplayName"]

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
        """Create an instance of ExternalLinkModel from a JSON string"""
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
        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if issue_type_name (nullable) is None
        # and model_fields_set contains the field
        if self.issue_type_name is None and "issue_type_name" in self.model_fields_set:
            _dict['issueTypeName'] = None

        # set to None if issue_type_icon_url (nullable) is None
        # and model_fields_set contains the field
        if self.issue_type_icon_url is None and "issue_type_icon_url" in self.model_fields_set:
            _dict['issueTypeIconUrl'] = None

        # set to None if priority_name (nullable) is None
        # and model_fields_set contains the field
        if self.priority_name is None and "priority_name" in self.model_fields_set:
            _dict['priorityName'] = None

        # set to None if priority_icon_url (nullable) is None
        # and model_fields_set contains the field
        if self.priority_icon_url is None and "priority_icon_url" in self.model_fields_set:
            _dict['priorityIconUrl'] = None

        # set to None if status_name (nullable) is None
        # and model_fields_set contains the field
        if self.status_name is None and "status_name" in self.model_fields_set:
            _dict['statusName'] = None

        # set to None if assignee_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.assignee_display_name is None and "assignee_display_name" in self.model_fields_set:
            _dict['assigneeDisplayName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalLinkModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "title": obj.get("title"),
            "issueTypeName": obj.get("issueTypeName"),
            "issueTypeIconUrl": obj.get("issueTypeIconUrl"),
            "priorityName": obj.get("priorityName"),
            "priorityIconUrl": obj.get("priorityIconUrl"),
            "statusName": obj.get("statusName"),
            "assigneeDisplayName": obj.get("assigneeDisplayName")
        })
        return _obj

