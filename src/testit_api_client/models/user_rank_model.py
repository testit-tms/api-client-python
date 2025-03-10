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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class UserRankModel(BaseModel):
    """
    UserRankModel
    """ # noqa: E501
    score: StrictInt
    work_items_created: StrictInt = Field(alias="workItemsCreated")
    passed_test_points: StrictInt = Field(alias="passedTestPoints")
    failed_test_points: StrictInt = Field(alias="failedTestPoints")
    skipped_test_points: StrictInt = Field(alias="skippedTestPoints")
    blocked_test_points: StrictInt = Field(alias="blockedTestPoints")
    level_avatar_enabled: StrictBool = Field(alias="levelAvatarEnabled")
    __properties: ClassVar[List[str]] = ["score", "workItemsCreated", "passedTestPoints", "failedTestPoints", "skippedTestPoints", "blockedTestPoints", "levelAvatarEnabled"]

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
        """Create an instance of UserRankModel from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserRankModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "score": obj.get("score"),
            "workItemsCreated": obj.get("workItemsCreated"),
            "passedTestPoints": obj.get("passedTestPoints"),
            "failedTestPoints": obj.get("failedTestPoints"),
            "skippedTestPoints": obj.get("skippedTestPoints"),
            "blockedTestPoints": obj.get("blockedTestPoints"),
            "levelAvatarEnabled": obj.get("levelAvatarEnabled")
        })
        return _obj


