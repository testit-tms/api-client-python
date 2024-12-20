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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.test_plan_changed_fields_view_model import TestPlanChangedFieldsViewModel
from typing import Optional, Set
from typing_extensions import Self

class TestPlanChangeModel(BaseModel):
    """
    TestPlanChangeModel
    """ # noqa: E501
    id: StrictStr
    test_plan_id: StrictStr = Field(alias="testPlanId")
    test_plan_changed_fields: TestPlanChangedFieldsViewModel = Field(alias="testPlanChangedFields")
    created_by_id: StrictStr = Field(alias="createdById")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    __properties: ClassVar[List[str]] = ["id", "testPlanId", "testPlanChangedFields", "createdById", "createdDate"]

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
        """Create an instance of TestPlanChangeModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of test_plan_changed_fields
        if self.test_plan_changed_fields:
            _dict['testPlanChangedFields'] = self.test_plan_changed_fields.to_dict()
        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestPlanChangeModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "testPlanId": obj.get("testPlanId"),
            "testPlanChangedFields": TestPlanChangedFieldsViewModel.from_dict(obj["testPlanChangedFields"]) if obj.get("testPlanChangedFields") is not None else None,
            "createdById": obj.get("createdById"),
            "createdDate": obj.get("createdDate")
        })
        return _obj


