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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.tag_model import TagModel
from testit_api_client.models.work_item_priority_model import WorkItemPriorityModel
from typing import Optional, Set
from typing_extensions import Self

class SharedStepReferenceModel(BaseModel):
    """
    SharedStepReferenceModel
    """ # noqa: E501
    id: StrictStr
    global_id: StrictInt = Field(alias="globalId")
    name: StrictStr
    entity_type_name: StrictStr = Field(alias="entityTypeName")
    has_this_shared_step_as_step: StrictBool = Field(alias="hasThisSharedStepAsStep")
    has_this_shared_step_as_precondition: StrictBool = Field(alias="hasThisSharedStepAsPrecondition")
    has_this_shared_step_as_postcondition: StrictBool = Field(alias="hasThisSharedStepAsPostcondition")
    created_by_id: StrictStr = Field(alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    state: StrictStr
    priority: WorkItemPriorityModel
    is_deleted: StrictBool = Field(alias="isDeleted")
    version_id: StrictStr = Field(description="used for versioning changes in workitem", alias="versionId")
    is_automated: StrictBool = Field(alias="isAutomated")
    section_id: StrictStr = Field(alias="sectionId")
    tags: Optional[List[TagModel]] = None
    __properties: ClassVar[List[str]] = ["id", "globalId", "name", "entityTypeName", "hasThisSharedStepAsStep", "hasThisSharedStepAsPrecondition", "hasThisSharedStepAsPostcondition", "createdById", "modifiedById", "createdDate", "modifiedDate", "state", "priority", "isDeleted", "versionId", "isAutomated", "sectionId", "tags"]

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
        """Create an instance of SharedStepReferenceModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SharedStepReferenceModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "globalId": obj.get("globalId"),
            "name": obj.get("name"),
            "entityTypeName": obj.get("entityTypeName"),
            "hasThisSharedStepAsStep": obj.get("hasThisSharedStepAsStep"),
            "hasThisSharedStepAsPrecondition": obj.get("hasThisSharedStepAsPrecondition"),
            "hasThisSharedStepAsPostcondition": obj.get("hasThisSharedStepAsPostcondition"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "state": obj.get("state"),
            "priority": obj.get("priority"),
            "isDeleted": obj.get("isDeleted"),
            "versionId": obj.get("versionId"),
            "isAutomated": obj.get("isAutomated"),
            "sectionId": obj.get("sectionId"),
            "tags": [TagModel.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None
        })
        return _obj


