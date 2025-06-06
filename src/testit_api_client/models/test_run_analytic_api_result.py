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
from typing import Any, ClassVar, Dict, List
from testit_api_client.models.test_run_group_by_failure_class_api_result import TestRunGroupByFailureClassApiResult
from testit_api_client.models.test_run_group_by_status_api_result import TestRunGroupByStatusApiResult
from testit_api_client.models.test_run_group_by_status_type_api_result import TestRunGroupByStatusTypeApiResult
from typing import Optional, Set
from typing_extensions import Self

class TestRunAnalyticApiResult(BaseModel):
    """
    TestRunAnalyticApiResult
    """ # noqa: E501
    count_group_by_status: List[TestRunGroupByStatusApiResult] = Field(alias="countGroupByStatus")
    count_group_by_status_type: List[TestRunGroupByStatusTypeApiResult] = Field(alias="countGroupByStatusType")
    count_group_by_failure_class: List[TestRunGroupByFailureClassApiResult] = Field(alias="countGroupByFailureClass")
    __properties: ClassVar[List[str]] = ["countGroupByStatus", "countGroupByStatusType", "countGroupByFailureClass"]

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
        """Create an instance of TestRunAnalyticApiResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in count_group_by_status (list)
        _items = []
        if self.count_group_by_status:
            for _item_count_group_by_status in self.count_group_by_status:
                if _item_count_group_by_status:
                    _items.append(_item_count_group_by_status.to_dict())
            _dict['countGroupByStatus'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in count_group_by_status_type (list)
        _items = []
        if self.count_group_by_status_type:
            for _item_count_group_by_status_type in self.count_group_by_status_type:
                if _item_count_group_by_status_type:
                    _items.append(_item_count_group_by_status_type.to_dict())
            _dict['countGroupByStatusType'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in count_group_by_failure_class (list)
        _items = []
        if self.count_group_by_failure_class:
            for _item_count_group_by_failure_class in self.count_group_by_failure_class:
                if _item_count_group_by_failure_class:
                    _items.append(_item_count_group_by_failure_class.to_dict())
            _dict['countGroupByFailureClass'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestRunAnalyticApiResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "countGroupByStatus": [TestRunGroupByStatusApiResult.from_dict(_item) for _item in obj["countGroupByStatus"]] if obj.get("countGroupByStatus") is not None else None,
            "countGroupByStatusType": [TestRunGroupByStatusTypeApiResult.from_dict(_item) for _item in obj["countGroupByStatusType"]] if obj.get("countGroupByStatusType") is not None else None,
            "countGroupByFailureClass": [TestRunGroupByFailureClassApiResult.from_dict(_item) for _item in obj["countGroupByFailureClass"]] if obj.get("countGroupByFailureClass") is not None else None
        })
        return _obj


