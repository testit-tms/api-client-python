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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WorkItemLikeModel(BaseModel):
    """
    WorkItemLikeModel
    """ # noqa: E501
    work_item_id: StrictStr = Field(alias="workItemId")
    created_date: datetime = Field(alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    created_by_id: StrictStr = Field(alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    id: StrictStr = Field(description="Unique ID of the entity")
    is_deleted: StrictBool = Field(description="Indicates if the entity is deleted", alias="isDeleted")
    __properties: ClassVar[List[str]] = ["workItemId", "createdDate", "modifiedDate", "createdById", "modifiedById", "id", "isDeleted"]

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
        """Create an instance of WorkItemLikeModel from a JSON string"""
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
        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkItemLikeModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workItemId": obj.get("workItemId"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "id": obj.get("id"),
            "isDeleted": obj.get("isDeleted")
        })
        return _obj

