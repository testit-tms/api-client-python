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
from testit_api_client.models.test_run_statistics_error_categories_get_model import TestRunStatisticsErrorCategoriesGetModel
from testit_api_client.models.test_run_statistics_statuses_get_model import TestRunStatisticsStatusesGetModel
from typing import Optional, Set
from typing_extensions import Self

class TestResultsStatisticsGetModel(BaseModel):
    """
    TestResultsStatisticsGetModel
    """ # noqa: E501
    statuses: TestRunStatisticsStatusesGetModel = Field(description="Test results counts aggregated by outcome")
    failure_categories: TestRunStatisticsErrorCategoriesGetModel = Field(description="Test results counts aggregated by result failure categories", alias="failureCategories")
    __properties: ClassVar[List[str]] = ["statuses", "failureCategories"]

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
        """Create an instance of TestResultsStatisticsGetModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "statuses",
            "failure_categories",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of statuses
        if self.statuses:
            _dict['statuses'] = self.statuses.to_dict()
        # override the default output from pydantic by calling `to_dict()` of failure_categories
        if self.failure_categories:
            _dict['failureCategories'] = self.failure_categories.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestResultsStatisticsGetModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "statuses": TestRunStatisticsStatusesGetModel.from_dict(obj["statuses"]) if obj.get("statuses") is not None else None,
            "failureCategories": TestRunStatisticsErrorCategoriesGetModel.from_dict(obj["failureCategories"]) if obj.get("failureCategories") is not None else None
        })
        return _obj


