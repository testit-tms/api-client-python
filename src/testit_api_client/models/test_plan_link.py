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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.external_link_model import ExternalLinkModel
from testit_api_client.models.link_model import LinkModel
from typing import Optional, Set
from typing_extensions import Self

class TestPlanLink(BaseModel):
    """
    TestPlanLink
    """ # noqa: E501
    bug_link: Optional[LinkModel] = Field(default=None, alias="bugLink")
    work_item_global_id: Optional[StrictInt] = Field(default=None, alias="workItemGlobalId")
    work_item_name: Optional[StrictStr] = Field(default=None, alias="workItemName")
    configuration_name: Optional[StrictStr] = Field(default=None, alias="configurationName")
    created_by_id: Optional[StrictStr] = Field(default=None, alias="createdById")
    comment: Optional[StrictStr] = None
    info: Optional[ExternalLinkModel] = None
    __properties: ClassVar[List[str]] = ["bugLink", "workItemGlobalId", "workItemName", "configurationName", "createdById", "comment", "info"]

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
        """Create an instance of TestPlanLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bug_link
        if self.bug_link:
            _dict['bugLink'] = self.bug_link.to_dict()
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # set to None if bug_link (nullable) is None
        # and model_fields_set contains the field
        if self.bug_link is None and "bug_link" in self.model_fields_set:
            _dict['bugLink'] = None

        # set to None if work_item_global_id (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_global_id is None and "work_item_global_id" in self.model_fields_set:
            _dict['workItemGlobalId'] = None

        # set to None if work_item_name (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_name is None and "work_item_name" in self.model_fields_set:
            _dict['workItemName'] = None

        # set to None if configuration_name (nullable) is None
        # and model_fields_set contains the field
        if self.configuration_name is None and "configuration_name" in self.model_fields_set:
            _dict['configurationName'] = None

        # set to None if created_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_id is None and "created_by_id" in self.model_fields_set:
            _dict['createdById'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if info (nullable) is None
        # and model_fields_set contains the field
        if self.info is None and "info" in self.model_fields_set:
            _dict['info'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestPlanLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bugLink": LinkModel.from_dict(obj["bugLink"]) if obj.get("bugLink") is not None else None,
            "workItemGlobalId": obj.get("workItemGlobalId"),
            "workItemName": obj.get("workItemName"),
            "configurationName": obj.get("configurationName"),
            "createdById": obj.get("createdById"),
            "comment": obj.get("comment"),
            "info": ExternalLinkModel.from_dict(obj["info"]) if obj.get("info") is not None else None
        })
        return _obj


